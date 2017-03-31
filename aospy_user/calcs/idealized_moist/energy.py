"""Module containing methods used for computing energy balance related
quantities in the idealized moist gray radiation model.
"""
from aospy_user.calcs import numerics as shn
from aospy_user.calcs import integration as skcint


def Q_toa(swdn_sfc, olr):
    """Returns the net downward energy flux at the top of the atmosphere.
    Expects all arguments to be positive.

    In the gray atmosphere idealized moist model, there is no absorption of
    shortwave radiation by the atmosphere.  swdn_sfc is the net shortwave
    radiation at TOA (i.e. it is equivalent to swdn_toa - swup_toa).

    In this manner we are computing:
    .. math::

        SW_{dn} - SW_{up} - OLR

    Parameters
    ----------
    swdn_sfc : DataArray
        Net downward shortwave radiation at the surface
    olr : DataArray
        Outgoing longwave radiation at the top of atmosphere

    Returns
    -------
    Q_toa : DataArray
        Net downward energy flux at the top of atmosphere
    """
    return swdn_sfc - olr


def Q_sfc(swdn_sfc, lwdn_sfc, lwup_sfc, flux_t, flux_lhe):
    """Returns the net downward energy flux at the surface.
    Expects all arguments to be positive.

    Here the net shortwave radiation at the surface is given by
    swdn_sfc.

    Parameters
    ----------
    swdn_sfc : DataArray
        Net downward shortwave radiation at the surface
    lwdn_sfc : DataArray
        Downward longwave radiation at the surface
    lwup_sfc : DataArray
        Upwward longwave radiation at the surface
    flux_t : DataArray
        Sensible heat flux into the atmosphere (upward from surface)
    flux_lhe : DataArray
        Latent heat flux into the atmosphere (upward from the surface)

    Returns
    -------
    Q_sfc : DataArray
        Net downward energy flux at the surface
    """
    return swdn_sfc + lwdn_sfc - lwup_sfc - flux_t - flux_lhe


def Q_diff(swdn_sfc, olr, lwdn_sfc, lwup_sfc, flux_t, flux_lhe):
    """Returns the net atmospheric column non-advective heating

    Parameters
    ----------
    swdn_sfc : DataArray
        Net downward shortwave radiation at the surface
    olr : DataArray
        Outgoing longwave radiation at the top of atmosphere
    lwdn_sfc : DataArray
        Downward longwave radiation at the surface
    lwup_sfc : DataArray
        Upwward longwave radiation at the surface
    flux_t : DataArray
        Sensible heat flux into the atmosphere (upward from surface)
    flux_lhe : DataArray
        Latent heat flux into the atmosphere (upward from the surface)

    Returns
    -------
    Q_diff : DataArray
        Net atmospheric column non-advective heating
    """
    return Q_toa(swdn_sfc, olr) - Q_sfc(swdn_sfc, lwdn_sfc, lwup_sfc,
                                        flux_t, flux_lhe)


def Q_diff_sw(swdn_sfc):
    """Returns the net atmospheric column non-advective heating due
    to shortwave radiation alone.  This is by definition zero in the
    gray atmosphere idealized moist model.

    Parameters
    ----------
    swdn_sfc : DataArray
        Net downward shortwave radiation at the surface

    Returns
    -------
    Q_diff_sw : DataArray
        Net atmospheric column non-advective heating due to shortwave
        radiation
    """
    return swdn_sfc - swdn_sfc


def Q_diff_lw(olr, lwdn_sfc, lwup_sfc):
    """Returns the net atmospheric column non-advective heating due to
    longwave radiation alone.

    Parameters
    ----------
    olr : DataArray
        Outgoing longwave radiation at the top of atmosphere
    lwdn_sfc : DataArray
        Downward longwave radiation at the surface
    lwup_sfc : DataArray
        Upwward longwave radiation at the surface

    Returns
    -------
    Q_diff_lw : DataArray
        Net atmospheric column non-advective heating
    """
    return lwup_sfc - olr - lwdn_sfc


def Q_diff_turb(flux_t, flux_lhe):
    """Returns the net atmospheric column non-advective heating due to
    turbulent surface fluxes alone.

    Parameters
    ----------
    flux_t : DataArray
        Sensible heat flux into the atmosphere (upward from surface)
    flux_lhe : DataArray
        Latent heat flux into the atmosphere (upward from the surface)

    Returns
    -------
    Q_diff_turb : DataArray
        Net atmospheric column non-advective heating due to turbelent fluxes
    """
    return flux_t + flux_lhe


def aht(swdn_sfc, olr, lwdn_sfc, lwup_sfc, flux_t, flux_lhe):
    """Returns the implied meridional atmospheric moist static energy transport
    computed from boundary energy fluxes.  This is a zonal mean quantity by
    definition.  The procedure is adapted from Spencer Hill's object library.

    .. math::
         \\left< \\overline{m v}  \\right> =
         \\int_0^{2 \\pi} \\int_{-\\pi / 2}^{\\pi / 2} \\overline{Q_{diff}}
         d \\phi d\\ \lambda

    Parameters
    ----------
    swdn_sfc : DataArray
        Net downward shortwave radiation at the surface
    lwdn_sfc : DataArray
        Downward longwave radiation at the surface
    lwup_sfc : DataArray
        Upwward longwave radiation at the surface
    flux_t : DataArray
        Sensible heat flux into the atmosphere (upward from surface)
    flux_lhe : DataArray
        Latent heat flux into the atmosphere (upward from the surface)

    Returns
    -------
    aht : DataArray
         Atmospheric heat transport
    """
    Q_diff_ = Q_diff(swdn_sfc, olr, lwdn_sfc, lwup_sfc, flux_t, flux_lhe)
    return skcint.meridional_integral(Q_diff_)


def lwup_sfc(net_lw_sfc, lwdn_sfc):
    """Returns the upward flux of longwave radiation at the surface in the
    idealized moist model with gray radiation.

    Parameters
    ----------
    net_lw_sfc : DataArray
        Net longwave radiation at the surface
    lwdn_sfc : DataArray
        Downward flux of longwave radiation at the surface

    Returns
    -------
    lwup_sfc : DataArray
        Upward flux of longwave radiation at the surface
    """
    return net_lw_sfc + lwdn_sfc
