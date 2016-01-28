"""Methods for computing general integrals"""

import numpy as np
import xarray as xr

from aospy import LAT_STR, LON_STR, PFULL_STR, PLEVEL_STR


def cumsum(arr, dim):
    """A wrapper for np.cumsum method for application on DataArrays.

    Adapted from https://github.com/pydata/xarray/issues/652

    Parameters
    ----------
    arr : DataArray
        DataArray to preform the cumulative sum on
    dim : str
        Dimension name of axis to preform summation along

    Returns
    -------
    cumsum : DataArray
        DataArray of result
    """
    return xr.DataArray(np.cumsum(arr, axis=arr.get_axis_num(dim)), arr.coords)


def reverse_cumsum(arr, dim):
    """A wrapper for to compute the reverse np.cumsum method
    for application on DataArrays.  This is good for use on
    computing the vertical integral from the bottom of the atmosphere
    up (if index 0 in the vertical is the top of the atmosphere).

    Adapted from https://github.com/pydata/xarray/issues/652

    Parameters
    ----------
    arr : DataArray
        DataArray to preform the cumulative sum on
    dim : str
        Dimension name of axis to preform summation along

    Returns
    -------
    cumsum : DataArray
        DataArray of result
    """
    rev_arr = arr.isel(**{dim: slice(None, None, -1)})
    integral = xr.DataArray(np.cumsum(rev_arr, axis=rev_arr.get_axis_num(dim)),
                            rev_arr.coords)
    return integral.isel(**{dim: slice(None, None, -1)})


def global_integral(arr):
    """Returns the area integral of the array provided.
    Assumes that, per aospy conventions, arr contains a
    coordinate containing the surface area at each gridpoint.

    Parameters
    ----------
    arr : DataArray
        DataArray with at least two dimensions and a surface
        area coordinate

    Returns
    -------
    integral : DataArray
        Global integral of arr
    """
    return (arr.sfc_area * arr).sum(LAT_STR).sum(LON_STR)


def global_average(arr):
    """Returns the area average of the array provided.
    Assumes that, per aospy conventions, arr contains a
    coordinate containing the surface area at each gridpoint.

    Parameters
    ----------
    arr : DataArray
        DataArray with at least two dimensions and a surface
        area coordinate

    Returns
    -------
    global_average : DataArray
        Global average of arr
    """
    return global_integral(arr) / arr.sfc_area.sum(LAT_STR).sum(LON_STR)


def meridional_integral(arr):
    """Returns the meridional integral of a quantity as a function of latitude.
    Assumes that, per aospy conventions, arr contains a coordinate containing
    the surface area at each gridpoint.

    .. math::
        \\int_0^{2 \\pi} \int_{-\\pi / 2}^{\\theta} Q d \\phi d \\lambda

    Parameters
    ----------
    arr : DataArray
        DataArray with at least two dimensions and a surface area
        coordinate

    Returns
    -------
    integral : DataArray
        Meridional integral at each latitude
    """
    mean = global_average(arr)
    zonal_int = (arr.sfc_area * (arr - mean)).sum(LON_STR)
    return cumsum(zonal_int, LAT_STR)
