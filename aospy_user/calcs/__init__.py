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
                         integrate, int_dp_g, weight_by_delta, vert_coord_name_xray)

def pfull(p):
    """ Returns the pressure at the level midpoints."""
    return to_pascal(p) 

def gz(temp, sphum, dp, p):
    integrand = (R_a.value * (1.0 + 0.608 * sphum) * temp) / p
    integrand = integrand * dp
    gz = integrand.copy()

    v = vert_coord_name_xray(dp)

    for k in range(len(dp[v])):
        gz[{v : k}] = integrand.isel(**{v : slice(k, None)}).sum(dim=v)
    return gz     

def dse(temp, sphum, dp, p):
    """ Returns the dry static energy at each gridbox.
    
    $s = c_p T + gz$
    """
    return (c_p.value * temp + gz(temp, sphum, dp, p))

def mse(temp, sphum, dp, p):
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
    return (dse(temp, sphum, dp, p) + L_v.value*sphum)
 
def msf(lat, dp, vcomp):
    """ Returns the mean meridional mass streamfunction. 
    
    """
    dp = to_pascal(dp.mean('lon'))
    v = vert_coord_name_xray(dp)
    msf_ = vcomp.mean('lon').copy() # Copy the DataArray (so we don't have to
    # set the coords ourselves. We then reassign values in the for loop.
    integrand = dp * vcomp.mean('lon')
    for k in range(len(dp[v])):
        msf_[{v : k}] = integrand.isel(**{v : slice(k, None)}).sum(dim=v)
    msf_ *= -2. * r_e.value * np.pi * np.cos(np.deg2rad(lat)) / grav.value
    return msf_
  
def msf_at_500_hPa(lat, dp, vcomp, p):
    """ Returns the mean meridional mass streamfunction at 500 hPa.
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
    
    # Use the zonal mean pressure.
    p = to_pascal(p.mean('lon'))
    to_min = np.abs(p/100. - 500.)
    inds = to_min.argmin('pfull')
    msf_ = msf(lat, dp, vcomp)
    return msf_.reduce(eval_at_index, dim='pfull', indices=inds)

    
