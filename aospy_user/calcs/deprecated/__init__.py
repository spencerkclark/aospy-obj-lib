"""These functions are deemed 'deprecated'.  What I mean by this is that
they either need to be re-written or are just not intelligently designed.
"""
import numpy as np
import xarray as xr

from aospy.constants import c_p, r_e
from aospy.utils import to_pascal, int_dp_g, vert_coord_name

from aospy_user.calcs.universal.dynamics import (msf,
                                                 vcomp_mb,
                                                 aht)
from aospy_user.calcs.universal.thermo import mse

# Take advantage of Spencer Hill's numerical functions.
from aospy_user.calcs.numerics import (
    d_dx_from_latlon,
    d_dy_from_lat,
    d_dp_from_p,
)

from aospy_user.calcs.interpolation import (
    zeros_xray,
)


def msf_at_500_hPa(vcomp, dp, p):
    """ Returns the time mean meridional mass streamfunction at 500 hPa.
    Use this only in post-processing.
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
    to_min = np.abs(p / 100. - 500)
    try:
        to_min = to_min.mean('time')
    except ValueError:
        pass
    inds = to_min.argmin(v)
    msf_ = msf(vcomp, dp)
    msf_ = msf_.mean('time')  # Take the time mean beforehand.
    return msf_.reduce(eval_at_index, dim=v, indices=inds)


# Deprecated.
def mmc_mse_flux(temp, sphum, vcomp, dp, p):
    """
    Computes the mean meridional circulation component of the MSE flux.
    This should again be a post-processing step.
    """
    mse_ = mse(temp, sphum, dp, p).mean('lon').mean('time')
    v = vcomp_mb(vcomp, dp).mean('time')
    try:
        dp = dp.mean('lon')
    except:
        pass
    return 2. * np.pi * r_e.value * np.cos(np.deg2rad(temp.lat)) * int_dp_g(mse_*v, dp)


# Deprecated.
def signed_max(data, dim):
    """
    Returns the signed maximum value along a given axis.
    """
    def max_(x, axis):
        """
        Returns the signed maximum value along a given axis.
        """
        bools = (-1. * x).max(axis=axis) > x.max(axis=axis)
        return (bools * x.min(axis=axis) + np.invert(bools) * x.max(axis=axis))
    return data.reduce(max_, dim=dim)


# Deprecated.
def gms(lat, temp, sphum, vcomp, dp, p):
    """
    Returns the gross moist stability as defined in SH 2015.
    """
    v = vert_coord_name(dp)
    return mmc_mse_flux(lat, temp, sphum, vcomp, dp, p) / (c_p.value * signed_max(msf(vcomp, dp), v))


# Deprecated.
def msf_500_zeros(vcomp, dp, p):
    """
    Returns the linearly interpolated zeros of the 500 mb meridional mass
    streamfunction. These can later be interpreted as Hadley Cell boundaries
    (but there will sometimes be more than three).
    This is more easily accomplished with the new interpolation module.
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
    lat_diff = xr.DataArray(msf_['lat'].values, coords=[msf_['lat'].values],
                                      dims=['lat'])
    b = msf_.diff('lat', label='lower') / lat_diff.diff('lat', label='lower')
    return (msf_['lat'][dict(lat=slice(None,-1))] * b - msf_[dict(lat=slice(None,-1))])/ b


# Deprecated
def eddy_mse_flux(temp, sphum, vcomp, swdn_sfc, olr,
                  lwdn_sfc, lwup_sfc, flux_t, flux_lhe, sfc_area, dp, p):
    """Eddy contribution to the northward MSE flux.
    Defined as a residual from the aht.
    """
    return aht(swdn_sfc,
               olr,
               lwdn_sfc,
               lwup_sfc,
               flux_t,
               flux_lhe,
               sfc_area).mean('time') - mmc_mse_flux(temp, sphum, vcomp, dp, p)


# Deprecated
def precip_extrema(condensation_rain, convection_rain):
    """Find the locations of precipitation extrema in the zonal mean using an
    interpolation method.
    """
    # Take the zonal and time mean of the total.
    total_rain = (condensation_rain + convection_rain).mean('lon').mean('time')
    return zeros_xray(d_dy_from_lat(total_rain, r_e, vec_field=False),
                      'lat')


# Deprecated
def precip_extrema_gcm(precip):
    """Find the locations of precipitation extrema in the zonal mean using an
    interpolation method.
    """
    # NOTE THIS FUNCTION IS BAD. It takes the mean in time to early.
    total_rain = precip.mean('lon').mean('time')
    return zeros_xray(d_dy_from_lat(total_rain, r_e, vec_field=False),
                      'lat', 360)


# These are fine to remain; however without mass balance adjustments they
# don't necessarily produce valid results.
def field_merid_flux_divg(arr, v, radius):
    """
    Meridional flux divergence of a field.
    """
    return d_dy_from_lat(v * arr, radius, vec_field=True)


def field_zonal_flux_divg(arr, u, radius):
    """
    Zonal flux divergence of a field.
    """
    return d_dx_from_latlon(u * arr, radius)


def field_vert_flux_divg(arr, omega, p):
    """
    Vertical flux divergence of a field.
    """
    return d_dp_from_p(omega * arr, p)


def mse_zonal_flux_divg(u, temp, sphum, dp, p):
    mse_ = mse(temp, sphum, dp, p)
    return field_zonal_flux_divg(mse_, u, r_e.value)


def mse_merid_flux_divg(v, temp, sphum, dp, p):
    mse_ = mse(temp, sphum, dp, p)
    return field_merid_flux_divg(mse_, v, r_e.value)


# IM
def mse_zonal_flux_divg_im(umse):
    return d_dx_from_latlon(umse, r_e.value)


def mse_merid_flux_divg_im(vmse):
    return d_dy_from_lat(vmse, r_e.value, vec_field=True)


def mse_zonal_flux_divg_v_im(umse_vint):
    return d_dx_from_latlon(umse_vint, r_e.value)


def mse_merid_flux_divg_v_im(vmse_vint):
    return d_dy_from_lat(vmse_vint, r_e.value, vec_field=True)
