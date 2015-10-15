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
                         integrate, int_dp_g, weight_by_delta, vert_coord_name)

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
 
def msf(lat, dp, vcomp):
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
    msf_ *= 2. * r_e.value * np.pi * np.cos(np.deg2rad(lat)) / grav.value
    return msf_
  
def msf_at_500_hPa(lat, dp, vcomp, p):
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
    msf_ = msf(lat, dp, vcomp)
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

def mmc_mse_flux(lat, temp, sphum, dp, p, vcomp):
    """ 
    Computes the mean meridional circulation component of the MSE flux.
    """
    mse_ = mse(temp, sphum, dp, p).mean('lon').mean('time')
    v = correct_vcomp(vcomp, dp).mean('time')
    try:
        dp = dp.mean('lon')
    except:
        pass
    return 2. * np.pi * r_e.value * np.cos(np.deg2rad(lat)) * int_dp_g_xray(mse_*v, dp)
    
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

def gms(lat, temp, sphum, dp, p, vcomp):
    """
    Returns the gross moist stability as defined in SH 2015.
    """
    v = vert_coord_name(dp)
    return mmc_mse_flux(lat, temp, sphum, dp, p, vcomp) / (c_p.value * signed_max(msf(lat, dp, vcomp), v))

def msf_500_zeros(lat, dp, vcomp, p):
    """
    Returns the linearly interpolated zeros of the 500 mb meridional mass streamfunction.
    These can later be interpreted as Hadley Cell boundaries (but there will sometimes be more than three)
    """
    # Find the streamfunction at 500 mb.
    msf_ = msf_at_500_hPa(lat, dp, vcomp, p)

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

def eddy_mse_flux(lat, temp, sphum, dp, p, vcomp, swdn_sfc, olr, lwdn_sfc, lwup_sfc, flux_t, flux_lhe, sfc_area):
    """
    Eddy contribution to the northward MSE flux. Defined as a residual from the aht.
    """
    return aht(swdn_sfc, olr, lwdn_sfc, lwup_sfc, flux_t, flux_lhe, sfc_area).mean('time') - mmc_mse_flux(lat, temp, sphum, dp, p, vcomp)

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

def total_precip(condensation_rain, convection_rain):
    """
    Returns the total precipitation rate at a gridbox.
    """
    return condensation_rain + convection_rain

def d_dtheta(field):
    """
    Computes the theta derivative using the central difference method.
    Theta is the polar angle in spherical coordinates.
    """
    upper_bound = field.isel(lat=slice(2,None))
    upper_bound['lat'] = field['lat'].isel(lat=slice(1,-1))
    lower_bound = field.isel(lat=slice(None,-2))
    lower_bound['lat'] = field['lat'].isel(lat=slice(1,-1))

    dtheta_v = field['lat'].isel(lat=slice(2,None)) - field['lat'].isel(lat=slice(None,-2)).values
    dtheta = xray.DataArray(np.deg2rad(dtheta_v), {'lat' : field['lat'].isel(lat=slice(1,-1)).values})
    
    dfield = field.copy(deep=True) # Make a copy for easy dimension preservation.
    dfield[dict(lat=slice(1,-1))] = upper_bound - lower_bound
    #dfield[dict(lat=0)] = 

    return (1./(r_e.value * np.cos(np.deg2rad(field['lat'].isel(lat=slice(1,-1)))))) * (dfield / dtheta)
