"""Module containing methods used for computing energy balance related
quantities in the idealized moist full radiation model.
"""
from aospy_user.calcs import integration as skcint


def Q_sfc(netrad_toa_imr, vert_int_tdt_rad_imr, flux_lhe, flux_t):
    """Returns the net downward energy flux at the surface.

    Parameters
    ----------
    netrad_toa_imr : DataArray
        Net downward radiation at top of atmosphere
    vert_int_tdt_rad_imr : DataArray
        Net column heating due to radiation
    flux_t : DataArray
        Sensible heat flux into the atmosphere (upward from surface)
    flux_lhe : DataArray
        Latent heat flux into the atmosphere (upward from the surface)

    Returns
    -------
    Q_sfc : DataArray
        Net downward energy flux at the surface
    """
    return netrad_toa_imr - Q_diff(vert_int_tdt_rad_imr, flux_lhe, flux_t)


def Q_diff(vert_int_tdt_rad_imr, flux_lhe, flux_t):
    """Returns the net atmospheric column non-advective heating

    Parameters
    ----------
    vert_int_tdt_rad_imr : DataArray
        Net column heating due to radiation
    flux_t : DataArray
        Sensible heat flux into the atmosphere (upward from surface)
    flux_lhe : DataArray
        Latent heat flux into the atmosphere (upward from the surface)

    Returns
    -------
    Q_diff : DataArray
        Net atmospheric column non-advective heating
    """
    return vert_int_tdt_rad_imr + flux_lhe + flux_t


def aht(vert_int_tdt_rad_imr, flux_lhe, flux_t):
    """Returns the implied meridional atmospheric moist static energy transport
    computed from boundary energy fluxes.  This is a zonal mean quantity by
    definition.  The procedure is adapted from Spencer Hill's object library.

    .. math::
         \\left< \\overline{m v}  \\right> =
         \\int_0^{2 \\pi} \\int_{-\\pi / 2}^{\\pi / 2} \\overline{Q_{diff}}
         d \\phi d\\ \lambda

    Parameters
    ----------
    vert_int_tdt_rad_imr : DataArray
        Net column heating due to radiation
    flux_t : DataArray
        Sensible heat flux into the atmosphere (upward from surface)
    flux_lhe : DataArray
        Latent heat flux into the atmosphere (upward from the surface)

    Returns
    -------
    aht : DataArray
         Atmospheric heat transport
    """
    Q_diff_ = Q_diff(vert_int_tdt_rad_imr, flux_lhe, flux_t)
    return skcint.meridional_integral(Q_diff_)
