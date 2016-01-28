"""My library of functions for use in aospy.

Except for helper functions, all assume input variables with the first axis
denoting time and the subsequent axes either (pressure, lat, lon) or, if not
vertically defined, (lat, lon).
"""


import universal
import idealized_moist
import deprecated

def dp(ps, bk, pk, arr):
    """Pressure thickness of hybrid coordinate levels from surface pressure."""
    return dp_from_ps(bk, pk, ps, arr[PFULL_STR])


def dp_sigma(temp, dp):
    return dp

def net_sw(swdn_toa, swup_toa):
    """Net shortwave radiation at TOA"""
    return swdn_toa - swup_toa


def pfull(p):
    """ Returns the pressure at the level midpoints."""
    return to_pascal(p)



