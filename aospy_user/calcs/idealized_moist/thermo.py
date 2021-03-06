"""Module containing methods used for computing thermodynamic
quantities in the idealized moist gray radiation model.
"""
from aospy.constants import L_v, c_p, grav
from aospy_user.calcs.integration import stationary_eddy


def dse(temp, height_full, sphum):
    """Returns the dry static energy in a model where height_full
    is a model output diagnostic.

    Parameters
    ----------
    temp : DataArray
        Temperature at full pressure levels
    height_full : DataArray
        Geopotential height at full pressure levels
    sphum : DataArray
        Specific humidity

    Returns
    -------
    dse : DataArray
        Dry static energy on full pressure levels
    """
    return (c_p.value * temp) + height_full * grav.value


def mse(temp, height_full, sphum):
    """Returns the moist static energy in a model where height_full
    is a model output diagnostic.

    Parameters
    ----------
    temp : DataArray
        Temperature at full pressure levels
    height_full : DataArray
        Geopotential height at full pressure levels
    sphum : DataArray
        Specific humidity at full pressure levels

    Returns
    -------
    mse : DataArray
        Moist static energy on full pressure levels
    """
    return dse(temp, height_full, sphum) + (L_v.value * sphum)


def mse_stat(temp, height_full, sphum):
    """Returns the stationary eddy component of the moist static energy in
    a model where height_full is a model output diagnostic.

    Parameters
    ----------
    temp : DataArray
        Temperature at full pressure levels
    height_full : DataArray
        Geopotential height at full pressure levels
    sphum : DataArray
        Specific humidity at full pressure levels

    Returns
    -------
    mse : DataArray
        Moist static energy on full pressure levels
    """
    m = dse(temp, height_full, sphum) + (L_v.value * sphum)
    return stationary_eddy(m)
