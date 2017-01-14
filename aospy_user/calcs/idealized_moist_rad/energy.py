"""Module containing methods used for computing energy balance related
quantities in the idealized moist full radiation model.
"""
from aospy_user.calcs import integration as skcint
from aospy_user.calcs.idealized_moist.water import p_minus_e


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


def alet(condensation_rain, convection_rain, flux_lhe):
    """Returns the implied meridional atmospheric latent energy transport
    computed from boundary energy fluxes.  This is a zonal mean quantity by
    definition.  The procedure is adapted from Spencer Hill's object library.

    .. math::
         \\left< \\overline{m v}  \\right> =
         \\int_0^{2 \\pi} \\int_{-\\pi / 2}^{\\pi / 2} \\overline{Q_{diff}}
         d \\phi d\\ \lambda

    Parameters
    ----------
    condensation_rain : DataArray
        Condensation rain
    convection_rain : DataArray
        Convection rain
    flux_lhe : DataArray
        Latent heat flux into atmosphere

    Returns
    -------
    alet : DataArray
         Atmospheric latent energy transport
    """
    p_minus_e_ = -p_minus_e(condensation_rain, convection_rain, flux_lhe)
    return skcint.meridional_integral(p_minus_e_)


def aht_simple(netrad_toa_imr):
    """Returns the implied meridional atmospheric moist static energy transport
    computed from boundary energy fluxes.  This is a zonal mean quantity by
    definition.  The procedure is adapted from Spencer Hill's object library.

    This is a test to see if not relying on the surface flux makes a big
    difference as to where the energy flux equator ends up.

    .. math::
         \\left< \\overline{m v}  \\right> =
         \\int_0^{2 \\pi} \\int_{-\\pi / 2}^{\\pi / 2} \\overline{Q_{diff}}
         d \\phi d\\ \lambda

    Parameters
    ----------
    netrad_toa_imr : DataArray
        Net radiation at the top of the atmosphere

    Returns
    -------
    aht : DataArray
         Atmospheric heat transport
    """
    return skcint.meridional_integral(netrad_toa_imr)


def swnet_toa(swdn_sfc, vert_int_tdtsw_rad_imr):
    """Returns the net shortwave radiation at the top of atmosphere
    in the idealized moist full radiation model.

    Parameters
    ----------
    swdn_sfc : DataArray
        Net shortwave radiation at the surface (not break from GCM
        nomenclature).
    vert_int_tdtsw_rad_imr : DataArray
        Net column heating due to shortwave radiation

    Returns
    -------
    swnet_toa : DataArray
        Net shortwave radiation at the top of atmosphere
    """
    return swdn_sfc + vert_int_tdtsw_rad_imr


def olr(swdn_sfc, vert_int_tdtsw_rad_imr, netrad_toa_imr):
    """Returns the outgoing longwave radiation
    in the idealized moist full radiation model.

    Parameters
    ----------
    swdn_sfc : DataArray
        Net shortwave radiation at the surface (not break from GCM
        nomenclature).
    vert_int_tdtsw_rad_imr : DataArray
        Net column heating due to shortwave radiation
    netrad_toa_imr : DataArray
        Net radiation at top of atmosphere (natively output
        by model)

    Returns
    -------
    olr : DataArray
        Outgoing longwave radiation
    """
    return swnet_toa(swdn_sfc, vert_int_tdtsw_rad_imr) - netrad_toa_imr
