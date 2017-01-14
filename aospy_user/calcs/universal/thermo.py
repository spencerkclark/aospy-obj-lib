from aospy.constants import c_p, L_v
from aospy_user.calcs.universal.dynamics import gz
from aospy.utils.vertcoord import to_pascal
from aospy import PFULL_STR


def dse(temp, sphum, dp, p):
    """ Returns the dry static energy at each gridbox.

    .. math::
        s = c_p T + gz

    Parameters
    ----------
    temp : DataArray
        Temperature
    sphum : DataArray
        Specific humidity
    p : DataArray
        Pressure at sigma levels
    dp : DataArray
        Thickness of pressure levels

    Returns
    -------
    dse : DataArray
        Dry static energy
    """
    return (c_p.value * temp + gz(temp, sphum, dp, p))


def mse(temp, sphum, dp, p):
    """ Returns the moist static energy at each gridbox.

    .. math::
        m = c_p T + L_v q + gz

    Parameters
    ----------
    temp : DataArray
        Temperature
    sphum : DataArray
        Specific humidity
    p : DataArray
        Pressure at sigma levels
    dp : DataArray
        Thickness of pressure levels

    Returns
    -------
    mse : DataArray
        Moist static energy
    """
    return (dse(temp, sphum, dp, p) + L_v.value * sphum)


def mse_b(temp, sphum, dp, p):
    """Average MSE between 20 and 40 hPa from surface.
    From Shekhar and Boos (2016).

    .. math::
        m_b = \\int_{p_s - 40}^{p_s - 20} m d p /
        \\int_{p_s - 40}^{p_s - 20} m d p

    Parameters
    ----------
    temp : DataArray
        Temperature
    sphum : DataArray
        Specific humidity
    p : DataArray
        Pressure at sigma levels
    dp : DataArray
        Thickness of pressure levels

    Returns
    -------
    mse_b : DataArray
        Average below-cloud moist static energy
    """
    p = to_pascal(p)
    dp = to_pascal(dp)
    dp_sfc = p.isel(**{PFULL_STR: -1}) - p
    mask = (dp_sfc >= 2000.0) & (dp_sfc < 4000.0)
    mse_ = mse(temp, sphum, dp, p)
    return ((mse_ * dp).where(mask).sum(PFULL_STR) /
            dp.where(mask).sum(PFULL_STR))


def mse_lower_trop(temp, sphum, dp, p):
    """Average MSE between 20 and 500 hPa from surface.
    From Shekhar and Boos (2016).

    .. math::
        m_b = \\int_{p_s - 500}^{p_s - 20} m d p /
        \\int_{p_s - 500}^{p_s - 20} m d p

    Parameters
    ----------
    temp : DataArray
        Temperature
    sphum : DataArray
        Specific humidity
    p : DataArray
        Pressure at sigma levels
    dp : DataArray
        Thickness of pressure levels

    Returns
    -------
    mse_lower_trop : DataArray
        Average lower-troposphere moist static energy
    """
    p = to_pascal(p)
    dp = to_pascal(dp)
    dp_sfc = p.isel(**{PFULL_STR: -1}) - p
    mask = (dp_sfc >= 2000.0) & (dp_sfc < 50000.0)
    mse_ = mse(temp, sphum, dp, p)
    return ((mse_ * dp).where(mask).sum(PFULL_STR) /
            dp.where(mask).sum(PFULL_STR))


def vert_av_temp(temp, dp):
    """Vertical, mass-weighted average of temperature

    Parameters
    ----------
    temp : DataArray
        Temperature
    dp : DataArray
        Thickness of pressure levels

    Returns
    -------
    vert_av_temp : DataArray
        Vertical, mass-weighted average of temperature
    """
    dp = to_pascal(dp)
    return ((temp * dp)).sum(PFULL_STR) / (dp.sum(PFULL_STR))
