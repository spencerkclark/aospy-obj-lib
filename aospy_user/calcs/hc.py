"""Diagnostics for investigating the behavior of the Hadley
Circulation.
"""
import xray
import numpy as np

from aospy.constants import r_e
import interpolation as sint
import numerics as shn

# ITCZ Definitions:
def precip_extrema(precip, npoints=18000):
    """Returns the linearly interpolated zeros of the meridional-derivative
    of the precipitation. A proxy for the ITCZ position.

    Parameters
    ----------
    precip: DataArray
         time and zonal mean of precipitation rate

    Returns
    -------
    zeros: DataArray
         linearly interpolated zeros of meridional derivative of precip.
    """
    d_precip_dy = shn.d_dy_from_lat(precip, r_e.value, vec_field=False)
    return sint.zeros_xray(d_precip_dy, 'lat', npoints)
