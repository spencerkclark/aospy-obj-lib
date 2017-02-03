import numpy as np
import xarray as xr

from aospy.constants import R_a, grav, r_e, L_v
from aospy.internal_names import LON_STR, LAT_STR
from aospy.utils.vertcoord import vert_coord_name, to_radians, to_pascal, int_dp_g
from aospy_user.calcs import integration as skcint
from aospy_user.calcs.universal.energy import Q_diff
from aospy_user.calcs.universal.water import p_minus_e


def gz(temp, sphum, dp, p):
    """Returns the geopotential height as computed using hydrostatic balance
    and the virtual temperature correction.

    Parameters
    ----------
    temp : DataArray
        Temperature
    sphum : DataArray
        Specific humidity
    dp : DataArray
        Pressure level thicknesses
    p : DataArray
        Pressure on full vertical levels

    Returns
    -------
    gz : DataArray
        Geopotential height on full pressure levels
    """
    integrand = dp * (R_a.value * (1.0 + 0.608 * sphum) * temp) / p
    return skcint.reverse_cumsum(integrand, vert_coord_name(dp))


def msf(vcomp, dp):
    """Returns the mean meridional mass streamfunction.  This is by definition
    a zonal mean quantity.  Thus it has no meaning in a regional average.  Time
    reductions still stand.

    Parameters
    ----------
    vcomp : DataArray
        Meridional wind
    dp : DataArray
        Pressure thicknesses

    Returns
    -------
    msf : DataArray
        Mean meridional mass streamfunction
    """
    try:
        dp = dp.mean(LON_STR)
    except AttributeError:
        pass
    dp = to_pascal(dp)
    integrand = dp * vcomp.mean(LON_STR)
    integral = skcint.reverse_cumsum(integrand, vert_coord_name(dp))
    return ((-2.0 * r_e.value * np.pi / grav.value) *
            np.cos(to_radians(vcomp[LAT_STR])) * integral)


def alet(precip, evap):
    """Returns the zonal mean vertically integrated transport of latent
    energy.  Computed via a meridional integral.

    Parameters
    ----------
    precip : DataArray
        Total precipitation rate
    evap : DataArray
        Evaporation rate

    Returns
    -------
    alet : DataArray
        Vertically integrated latent energy transport
    """
    p_minus_e_ = p_minus_e(precip, evap)
    return skcint.meridional_integral(-L_v.value * p_minus_e_)


def aht(swdn_toa, olr, swup_toa, swdn_sfc, lwdn_sfc, swup_sfc, lwup_sfc,
        shflx, evap):
    """Returns the zonal mean vertically integrated northward moist static
    energy transport.  Computed as in Hill et al. (2015).

    Parameters
    ----------
    swdn_toa : DataArray
        Downward flux of shortwave radiation at the top of atmosphere
    olr : DataArray
        Outgoing longwave radiation at the top of atmosphere
    swup_toa : DataArray
        Upward flux of shortwave radiation at the top of atmosphere
    swdn_sfc : DataArray
        Downward flux of shortwave radiation at the surface
    lwdn_sfc : DataArray
        Downward flux of longwave radiation at the surface
    swup_sfc : DataArray
        Upward flux of shortwave radiation at the surface
    lwup_sfc : DataArray
        Upwward longwave radiation at the surface
    shflx : DataArray
        Sensible heat flux into the atmosphere (upward from surface)
    evap : DataArray
        Evaporation rate of water at the surface

    Returns
    -------
    aht : DataArray
        Zonal mean vertically integrated northward moist static energy
        transport
    """
    Q_diff_ = Q_diff(swdn_toa, olr, swup_toa, swdn_sfc, lwdn_sfc, swup_sfc,
                     lwup_sfc, shflx, evap)
    return skcint.meridional_integral(Q_diff_)


def vcomp_mb(vcomp, dp):
    """Returns the mass-balance-corrected zonal mean meridional wind.  Uses the
    method described in Hill et al. (2015).  Not defined for regional
    reductions.

    Parameters
    ----------
    vcomp : DataArray
        Meridional wind
    dp : DataArray
        Pressure thicknesses

    Returns
    -------
    vcomp_mb : DataArray
        Mass balance corrected zonal mean meridional wind
    """
    try:
        dp = dp.mean(LON_STR)
    except AttributeError:
        pass

    vcomp = vcomp.mean(LON_STR)
    vplus = vcomp.copy(deep=True)
    vminus = vcomp.copy(deep=True)
    vplus.values[vcomp.values < 0] = 0.
    vminus.values[vcomp.values > 0] = 0.

    factor = -1. * int_dp_g(vplus, dp) / int_dp_g(vminus, dp)
    return (vplus + factor * vminus)
