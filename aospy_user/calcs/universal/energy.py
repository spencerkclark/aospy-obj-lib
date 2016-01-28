from aospy.constants import L_v


def Q_diff(swdn_toa, olr, swup_toa, swdn_sfc, lwdn_sfc, swup_sfc, lwup_sfc,
           shflx, evap):
    """Returns the net column heating in a comprehensive GCM.  All inputs have
    units of W m**-2 except evap.

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
    Q_diff : DataArray
        Net column heating
    """
    return (swdn_toa - olr - swup_toa - (swdn_sfc + lwdn_sfc - swup_sfc -
                                         lwup_sfc - shflx - (L_v * evap)))


def Q_diff_sw(swdn_toa, swup_toa, swdn_sfc, swup_sfc):
    """Returns the net column heating due to shortwave radiation.

    Parameters
    ----------
    swdn_toa : DataArray
        Downward flux of shortwave radiation at the top of atmosphere
    swup_toa : DataArray
        Upward flux of shortwave radiation at the top of atmosphere
    swdn_sfc : DataArray
        Downward flux of shortwave radiation at the surface
    swup_sfc : DataArray
        Upward flux of shortwave radiation at the surface

    Returns
    -------
    Q_diff_sw : DataArray
        Net column heating due to shortwave radiation
    """
    return swdn_toa + swup_sfc - swup_toa - swdn_sfc


def Q_diff_lw(olr, lwdn_sfc, lwup_sfc):
    """Returns the net column heating due to longwave radiation.

    Parameters
    ----------
    olr : DataArray
        Outgoing longwave radiation at the top of atmosphere
    lwdn_sfc : DataArray
        Downward flux of longwave radiation at the surface
    lwup_sfc : DataArray
        Upwward longwave radiation at the surface

    Returns
    -------
    Q_diff_lw : DataArray
        Net column heating due to longwave radiation
    """
    return lwup_sfc - olr - lwdn_sfc
