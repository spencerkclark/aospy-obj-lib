"""My library of functions for use in aospy."""
from aospy.utils.vertcoord import dp_from_ps, to_pascal
from aospy.internal_names import PFULL_STR
import universal
import idealized_moist
import idealized_moist_rad
import deprecated
#import sah_mse_budget

def dp(ps, bk, pk, arr):
    """Pressure thickness of hybrid coordinate levels from surface pressure.

    Parameters
    ----------
    ps : DataArray
        Surface pressure
    bk : DataArray
        bk coordinate
    pk : DataArray
        pk coordinate
    arr : DataArray
        A DataArray with a pfull coordinate

    Returns
    -------
    dp : DataArray
        Pressure thicknesses in sigma coordinates
    """
    return dp_from_ps(bk, pk, ps, arr[PFULL_STR])


def dp_sigma(temp, dp):
    """Returns the pressure thicknesses on sigma levels.

    This is a function used such that we can save the pressure
    output.

    Parameters
    ----------
    temp : DataArray
        Temperature
    dp : DataArray
        Computed pressure thicknesses

    Returns
    -------
    dp : DataArray
        Pressure thicknesses for sigma levels
    """
    return dp


def pfull(p):
    """Returns the pressure at the level midpoints.

    Parameters
    ----------
    p : DataArray
        Pressure

    Returns
    -------
    p : DataArray
        Pressure in Pa
    """
    return to_pascal(p)
