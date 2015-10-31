"""My library of functions for use in aospy.

Except for helper functions, all assume input variables with the first axis
denoting time and the subsequent axes either (pressure, lat, lon) or, if not
vertically defined, (lat, lon).
"""
import scipy.stats
import numpy as np
import xray

from aospy.constants import (c_p, grav, kappa, L_f, L_v, r_e, Omega, p_trip,
                             T_trip, c_va, c_vv, c_vl, c_vs, R_a, R_v,
                             E_0v, E_0s, s_0v, s_0s)
from aospy.utils import (level_thickness, to_pascal, to_radians,
                         integrate, int_dp_g)# weight_by_delta) #vert_coord_name)

# Take advantage of Spencer Hill's numerical functions.
from .numerics import (
    fwd_diff1,
    fwd_diff2,
    # cen_diff2,
    # cen_diff4,
    upwind_scheme,
    latlon_deriv_prefactor,
    wraparound_lon,
    d_dx_from_latlon,
    d_dy_from_lat,
    d_dx_at_const_p_from_eta,
    d_dy_at_const_p_from_eta,
    d_dx_of_vert_int,
    d_dy_of_vert_int,
    d_dp_from_p,
    d_dp_from_eta
)

def vert_coord_name(dp):
    for name in ['level', 'pfull']:
        if name in dp.coords:
            return name
    return None 

def pfull(p):
    """ Returns the pressure at the level midpoints."""
    return to_pascal(p) 

def gz(temp, sphum, dp, p):
    integrand = (R_a.value * (1.0 + 0.608 * sphum) * temp) / p
    integrand = integrand * dp
    gz = integrand.copy()

    v = vert_coord_name_xray(dp)

    for k in range(len(dp[v])):
        gz[{v : k}] = integrand.isel(**{v : slice(k, None)}).sum(dim=v)
    return gz     

def dse(temp, sphum, dp, p):
    """ Returns the dry static energy at each gridbox.
    
    $s = c_p T + gz$
    """
    return (c_p.value * temp + gz(temp, sphum, dp, p))

def mse(temp, sphum, dp, p):
    """ Returns the moist static energy at each gridbox.
    
    $m = c_p T + L_v q + gz$

    Parameters
    ----------
    temp : array
        temperature
    sphum : array
        specific humidity
    p : array
        pressure at sigma levels
    dp : array
        thickness of pressure levels

    Returns
    -------
    mse : array
        moist static energy
    """
    return (dse(temp, sphum, dp, p) + L_v.value*sphum)
 
def msf(vcomp, dp):
    """ Returns the mean meridional mass streamfunction. 
    
    """
    try:
        dp = dp.mean('lon')
    except:
        pass
    dp = to_pascal(dp)
    v = vert_coord_name(dp)
    msf_ = vcomp.mean('lon').copy(deep=True) # Copy the DataArray (so we don't have to
    # set the coords ourselves. We then reassign values in the for loop.
    integrand = dp * vcomp.mean('lon')
    for k in range(len(dp[v])):
        msf_[{v : k}] = integrand.isel(**{v : slice(k, None)}).sum(dim=v)
    msf_ *= 2. * r_e.value * np.pi * np.cos(np.deg2rad(vcomp.lat)) / grav.value
    return msf_
  
def msf_at_500_hPa(vcomp, dp, p):
    """ Returns the time mean meridional mass streamfunction at 500 hPa.
    """
    def eval_at_index(x, axis, indices=None):
        """
        Parameters
        ----------
        x : array
            full numpy array to apply function to
        axis : int
            axis to collapse
        indices : array
            array containing indices in each column you would like to 
            evaluate at (to collapse the array)
        """
        collapse_dim_len = x.shape[axis]
        x = np.swapaxes(x, -1, axis)
        reduced_shape = x.shape[:-1]
        x = np.reshape(x, (-1, collapse_dim_len))
        inds = np.reshape(indices.values, (-1,))
        rows = np.array(np.arange(x.shape[0]), dtype=np.intp)
        cols = inds.astype(np.intp)
        return np.reshape(x[rows, cols], reduced_shape)
    
    v = vert_coord_name(dp)
    try:
        p = p.mean('lon')
    except:
        pass
    
    p = to_pascal(p)
    #p = p.mean('time')
    to_min = np.abs(p/100. - 500)
    try:
        to_min = to_min.mean('time')
    except ValueError:
        pass
    inds = to_min.argmin(v)
    msf_ = msf(vcomp, dp)
    msf_ = msf_.mean('time') # Take the time mean beforehand.
    return msf_.reduce(eval_at_index, dim=v, indices=inds)

def correct_vcomp(vcomp, dp):
    """
    Applies the SH 2015 correction to the meridional velocity to ensure mass 
    balance in the MSE flux. 
    """
    vcomp = vcomp.mean('lon')
    vplus = vcomp.copy(deep=True)
    vminus = vcomp.copy(deep=True)
    vplus.values[vcomp.values < 0] = 0.
    vminus.values[vcomp.values > 0] = 0.

    try:
        dp = dp.mean('lon')
    except:
        pass
    factor = -1. * int_dp_g_xray(vplus, dp) / int_dp_g_xray(vminus, dp)
    return (vplus + factor*vminus)

def mmc_mse_flux(temp, sphum, vcomp, dp, p):
    """ 
    Computes the mean meridional circulation component of the MSE flux.
    """
    mse_ = mse(temp, sphum, dp, p).mean('lon').mean('time')
    v = correct_vcomp(vcomp, dp).mean('time')
    try:
        dp = dp.mean('lon')
    except:
        pass
    return 2. * np.pi * r_e.value * np.cos(np.deg2rad(temp.lat)) * int_dp_g_xray(mse_*v, dp)
    
def signed_max(data, dim):
    """
    Returns the signed maximum value along a given axis.
    """
    def max_(x, axis):
        """
        Returns the signed maximum value along a given axis.
        """
        bools = (-1.*x).max(axis=axis) > x.max(axis=axis)
        return (bools*x.min(axis=axis) + np.invert(bools)*x.max(axis=axis))
    return data.reduce(max_, dim=dim)

def gms(lat, temp, sphum, vcomp, dp, p):
    """
    Returns the gross moist stability as defined in SH 2015.
    """
    return mmc_mse_flux(lat, temp, sphum, vcomp, dp, p) / (c_p.value * signed_max(msf(vcomp, dp), v))

def msf_500_zeros(vcomp, dp, p):
    """
    Returns the linearly interpolated zeros of the 500 mb meridional mass streamfunction.
    These can later be interpreted as Hadley Cell boundaries (but there will sometimes be more than three)
    """
    # Find the streamfunction at 500 mb.
    msf_ = msf_at_500_hPa(vcomp, dp, p)

    # Now find the zeros.
    signs = msf_.copy(deep=True)
    msf_val = np.array(msf_.values)
    signs.values = np.sign(msf_val)

    # Take two diffs, one preserving lower, the other preserving upper for the lat coord.
    # This leaves everything but the values surrounding the zero masked.
    mask = signs.diff('lat', label='lower') != 0
    mask = mask.diff('lat', label='upper')

    # Initialize the mask as all False's.
    mask_full = msf_.copy(deep=True)
    mask_full.values = np.zeros(msf_.values.shape).astype(bool)
    mask_full[dict(lat=slice(1,-1))] = mask

    # Mask msf_ appropriately.
    msf_.values= np.ma.masked_array(msf_.values, np.invert(mask_full))
    
    # For whatever reason you cannot do a diff on a coordinate. Thus we create
    # a DataArray with the lat values renamed as a new variable.
    lat_diff = xray.DataArray(msf_['lat'].values, coords=[msf_['lat'].values],
                                      dims=['lat'])
    b = msf_.diff('lat', label='lower') / lat_diff.diff('lat', label='lower')
    return (msf_['lat'][dict(lat=slice(None,-1))] * b - msf_[dict(lat=slice(None,-1))])/ b

def Q_toa_im(swdn_sfc, olr):
    """
    Heat flux at the top of atmosphere in the idealized moist model.
    """
    return swdn_sfc - olr

def Q_sfc_im(swdn_sfc, lwdn_sfc, lwup_sfc, flux_t, flux_lhe):
    """
    Heat flux at the surface.
    """
    return swdn_sfc + lwdn_sfc - lwup_sfc - flux_t - flux_lhe

def aht(swdn_sfc, olr, lwdn_sfc, lwup_sfc, flux_t, flux_lhe, sfc_area):
    """
    Atmospheric heat transport. Computed from radiative fluxes.
    Procedure adapted from SH's library.
    Parameters
    ----------
    """
    Q_diff = Q_toa_im(swdn_sfc, olr) - Q_sfc_im(swdn_sfc, lwdn_sfc, lwup_sfc, flux_t, flux_lhe)
    global_mean = (sfc_area * Q_diff).sum('lat').sum('lon') / sfc_area.sum('lat').sum('lon')
    zonal_integral = (sfc_area * (Q_diff - global_mean)).sum('lon')
    # Now do a cumulative sum in the latitude dimension.
    aht_ = zonal_integral.copy(deep=True)
    for j in range(zonal_integral['lat'].values.shape[0]):
        aht_[dict(lat=j)] = zonal_integral.isel(lat=slice(None,j)).sum('lat')
    return aht_

def eddy_mse_flux(temp, sphum, vcomp, swdn_sfc, olr, lwdn_sfc, lwup_sfc, flux_t, flux_lhe, sfc_area, dp, p):
    """
    Eddy contribution to the northward MSE flux. Defined as a residual from the aht.
    """
    return aht(swdn_sfc, olr, lwdn_sfc, lwup_sfc, flux_t, flux_lhe, sfc_area).mean('time') - mmc_mse_flux(temp, sphum, vcomp, dp, p)

def precip_extrema(condensation_rain, convection_rain):
    """
    Find the locations of precipitation extrema in the zonal mean using interpolation method.
    """
    # Take the zonal and time mean of the total.
    total_rain = (condensation_rain + convection_rain).mean('lon').mean('time')
    lats = xray.DataArray(total_rain['lat'].values, coords=[total_rain['lat'].values], dims=['lat'])

    # Take the central difference first derivative.
    dummy = total_rain.diff('lat', n=1, label='upper')
    dummy = dummy.diff('lat', n=1, label='lower')
    
    # Now dummy has the coordinates and dimensions we want for the central difference.
    dummy.values = total_rain[dict(lat=slice(2,None))].values - total_rain[dict(lat=slice(None,-2))].values
    
    # Now we need the denominator.
    lat = dummy.copy(deep=True)
    lat.values = lats[dict(lat=slice(2,None))].values - lats[dict(lat=slice(None,-2))].values

    rain_central_diff = dummy / lat
    
    # Now interpolate to find the zeros of the derivative.
    # Now find the zeros.
    signs = rain_central_diff.copy(deep=True)
    rcd = np.array(rain_central_diff.values)
    signs.values = np.sign(rcd)

    # Take two diffs, one preserving lower, the other preserving upper for the lat coord.
    # This leaves everything but the values surrounding the zero masked.
    mask = signs.diff('lat', label='lower') != 0
    mask = mask.diff('lat', label='upper')

    # Initialize the mask as all False's.
    mask_full = rain_central_diff.copy(deep=True)
    mask_full.values = np.zeros(rain_central_diff.values.shape).astype(bool)
    mask_full[dict(lat=slice(1,-1))] = mask

    # Mask msf_ appropriately.
    rain_central_diff.values= np.ma.masked_array(rain_central_diff.values, np.invert(mask_full))

    # For whatever reason you cannot do a diff on a coordinate. Thus we create
    # a DataArray with the lat values renamed as a new variable.
    lat_diff = xray.DataArray(rain_central_diff['lat'].values, coords=[rain_central_diff['lat'].values],
                                      dims=['lat'])
    b = rain_central_diff.diff('lat', label='lower') / lat_diff.diff('lat', label='lower')
#    print((rain_central_diff['lat'][dict(lat=slice(None,-1))] * b - rain_central_diff[dict(lat=slice(None,-1))]) / b)    
    return (rain_central_diff['lat'][dict(lat=slice(None,-1))] * b - rain_central_diff[dict(lat=slice(None,-1))])/ b

def precip_extrema_gcm(precip):
    """
    Find the locations of precipitation extrema in the zonal mean using interpolation method.
    """
    # Take the zonal and time mean of the total.
    total_rain = precip.mean('lon').mean('time')
    lats = xray.DataArray(total_rain['lat'].values, coords=[total_rain['lat'].values], dims=['lat'])

    # Take the central difference first derivative.
    dummy = total_rain.diff('lat', n=1, label='upper')
    dummy = dummy.diff('lat', n=1, label='lower')
    
    # Now dummy has the coordinates and dimensions we want for the central difference.
    dummy.values = total_rain[dict(lat=slice(2,None))].values - total_rain[dict(lat=slice(None,-2))].values
    
    # Now we need the denominator.
    lat = dummy.copy(deep=True)
    lat.values = lats[dict(lat=slice(2,None))].values - lats[dict(lat=slice(None,-2))].values

    rain_central_diff = dummy / lat
    
    # Now interpolate to find the zeros of the derivative.
    # Now find the zeros.
    signs = rain_central_diff.copy(deep=True)
    rcd = np.array(rain_central_diff.values)
    signs.values = np.sign(rcd)

    # Take two diffs, one preserving lower, the other preserving upper for the lat coord.
    # This leaves everything but the values surrounding the zero masked.
    mask = signs.diff('lat', label='lower') != 0
    mask = mask.diff('lat', label='upper')

    # Initialize the mask as all False's.
    mask_full = rain_central_diff.copy(deep=True)
    mask_full.values = np.zeros(rain_central_diff.values.shape).astype(bool)
    mask_full[dict(lat=slice(1,-1))] = mask

    # Mask msf_ appropriately.
    rain_central_diff.values= np.ma.masked_array(rain_central_diff.values, np.invert(mask_full))

    # For whatever reason you cannot do a diff on a coordinate. Thus we create
    # a DataArray with the lat values renamed as a new variable.
    lat_diff = xray.DataArray(rain_central_diff['lat'].values, coords=[rain_central_diff['lat'].values],
                                      dims=['lat'])
    b = rain_central_diff.diff('lat', label='lower') / lat_diff.diff('lat', label='lower')
#    print((rain_central_diff['lat'][dict(lat=slice(None,-1))] * b - rain_central_diff[dict(lat=slice(None,-1))]) / b)    
    return (rain_central_diff['lat'][dict(lat=slice(None,-1))] * b - rain_central_diff[dict(lat=slice(None,-1))])/ b
    

def total_precip(condensation_rain, convection_rain):
    """
    Returns the total precipitation rate at a gridbox.
    """
    return condensation_rain + convection_rain

def d_dtheta(field, div=False):
    """
    Computes the theta derivative using the central difference method.
    Theta is the latitude angle in spherical coordinates.
    """
    if div:
        field *= np.cos(np.deg2rad(field.lat))

    upper_bound = field.isel(lat=slice(2,None))
    upper_bound['lat'] = field['lat'].isel(lat=slice(1,-1))
    lower_bound = field.isel(lat=slice(None,-2))
    lower_bound['lat'] = field['lat'].isel(lat=slice(1,-1))

    dtheta_v = field['lat'].isel(lat=slice(2,None)) - field.lat.isel(lat=slice(None,-2)).values
    dtheta = xray.DataArray(np.deg2rad(dtheta_v), {'lat' : field.lat.isel(lat=slice(1,-1)).values})
    
    dfield = field.copy(deep=True) # Make a copy for easy dimension preservation.
    dfield[dict(lat=slice(1,-1))] = upper_bound - lower_bound
    #dfield[dict(lat=0)] = 

    return (1./(r_e.value * np.cos(np.deg2rad(field.lat.isel(lat=slice(1,-1)))))) * (dfield / dtheta)

def d_dphi(field):
    """
    Computes the longitude derivative using the central difference method.
    """
    upper_bound = field.isel(lon=slice(2,None))   
    upper_bound['lon'] = field['lon'].isel(lon=slice(1,-1))
    lower_bound = field.isel(lon=slice(None,-2))
    lower_bound['lon'] = field['lon'].isel(lon=slice(1,-1))
    
    dphi_v = field['lon'].isel(lon=slice(2,None)).values - field['lon'].isel(lon=slice(None,-2)).values
    dphi = xray.DataArray(dphi_v, {'lon' : field['lon'].isel(lon=slice(1,-1)).values}) * np.pi / 180.0
    
    dfield = upper_bound - lower_bound
    return (1.0 / r_e.value) * dfield / dphi

def d_dp(field, pf):
    """ Computes the pressure derivative of a quantity using a central difference.
    """
    # Centered difference in the middle.
    lower_bound = field.isel(pfull=slice(2, None))
    lower_bound['pfull'] = field['pfull'].isel(pfull=slice(1,-1))
    upper_bound = field.isel(pfull=slice(None, -2))
    upper_bound['pfull'] = field['pfull'].isel(pfull=slice(1,-1))
    
    dp_u = pf.isel(pfull=slice(None, -2))
    dp_u['pfull'] = field['pfull'].isel(pfull=slice(1,-1))
    dp_l = pf.isel(pfull=slice(2, None))
    dp_l['pfull'] = field['pfull'].isel(pfull=slice(1,-1))

    dp = dp_u - dp_l
    
    dfield = field.copy(deep=True)
    dfield[dict(pfull=slice(1,-1))] = (upper_bound - lower_bound) / dp

    #print(dp)
    dfield[dict(pfull=0)].values = (field[dict(pfull=1)].values - field[dict(pfull=0)].values) /\
                                    (pf[dict(pfull=1)].values - pf[dict(pfull=0)].values)
    dfield[dict(pfull=-1)].values = (field[dict(pfull=-1)].values - field[dict(pfull=-2)].values) /\
                                    (pf[dict(pfull=-1)].values - pf[dict(pfull=-2)].values)
    
    return dfield

def div_v(ucomp, vcomp, omega, p):
    """
    Computes the divergence of the velocity field in spherical coords.
    """
    return d_dphi(ucomp) + d_dtheta(vcomp, div=True) + d_dp(omega, p)
