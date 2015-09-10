"""My library of functions for use in aospy.

Except for helper functions, all assume input variables with the first axis
denoting time and the subsequent axes either (pressure, lat, lon) or, if not
vertically defined, (lat, lon).
"""
import scipy.stats
import numpy as np

from aospy.constants import (c_p, grav, kappa, L_f, L_v, r_e, Omega, p_trip,
                             T_trip, c_va, c_vv, c_vl, c_vs, R_a, R_v,
                             E_0v, E_0s, s_0v, s_0s)
from aospy.utils import (level_thickness, to_pascal, to_radians,
                         integrate, int_dp_g, weight_by_delta)

def skc_gz(temp, sphum, dp, p):
    integrand = (R_a.value * (1.0 + 0.608 * sphum) * temp) / p
    integrand = integrand * dp
    gz = integrand.copy()
    for k in range(len(dp['level'])):
        gz[dict(level=k)] = integrand.isel(level=slice(k, None)).sum(dim='level')
    return gz     

def skc_mse(temp, sphum, dp, p):
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
    return (c_p*temp + L_v*sphum + skc_gz(temp, sphum, dp, p))

