def p_minus_e(precip, evap):
    """ Returns the precipitation minus evaporation at each gridbox.

    Parameters
    ----------
    precip : DataArray
        Total liquid precipitation rate
    evap : DataArray
        Evaporation rate

    Returns
    -------
    p_minus_e : DataArray
        Precipitation minus evaporation
    """
    return precip - evap
