"""Interpolation and zero finding routines.  These are all
dimension agnostic.
"""

import xray
import numpy as np
from scipy.interpolate import interp1d
from collections import OrderedDict


def sorted_coords(da):
    """Returns a list of coordinate names based on axis order."""
    order = {coord:
             da.reset_coords(drop=True).get_axis_num(coord)
             for coord in da.reset_coords(drop=True).coords}
    return zip(*sorted(order.items(), key=lambda (k, v): v))[0]


def replace_dim(da, dim, values):
    """Replaces a dimension in a coords OrderedDict"""

    # Sort the coordinates by axis number. Then fill
    # OrderedDict.
    sorted_coords_ = sorted_coords(da)
    coords = da.reset_coords(drop=True).coords
    new_coords = OrderedDict()
    for coord in sorted_coords_:
        if dim != coord:
            new_coords[coord] = coords[coord]
        else:
            new_coords[dim] = values
    return new_coords


def interp1d_pt_xray(da, dim, value):
    """Interpolates the values of a DataArray at a point
    along the specified dimension.

    Parameters
    ----------
    da : DataArray
         data to interpolate
    dim : str
         dimension name to interpolate along
    value : float
         point to interpolate to

    Returns
    -------
    slice : DataArray
         interpolated data
    """

    function = interp1d(da[dim].values, da.values,
                        axis=da.get_axis_num(dim))
    values_interp = function(value)
    da_interp = xray.DataArray(values_interp,
                               coords=replace_dim(da,
                                                  dim, value))
    return da_interp


def interp1d_xray(da, dim, npoints=18000):
    """Interpolates the DataArray to finer resolution

    Parameters
    ----------
    da : DataArray
         data to interpolate
    dim : str
         dimension name to interpolate along
    npoints : int
         number of points to expand dimension to

    Returns
    -------
    interp : DataArray
         interpolated DataArray
    """
    function = interp1d(da[dim].values, da.values,
                        axis=da.get_axis_num(dim))
    coord_interp = np.linspace(da[dim][0], da[dim][-1],
                               npoints, endpoint=True)
    values_interp = function(coord_interp)
    da_interp = xray.DataArray(values_interp,
                               coords=replace_dim(da,
                                                  dim, coord_interp))
    return da_interp


def zeros_xray(da, dim, npoints=18000):
    """Finds zeros of a DataArray along an axis at the specified
    resolution. A higher value for npoints means higher precision.
    The defualt npoints gives linearly-interpolated
    zeros to within 0.01 degrees latitude.

    Parameters
    ----------
    da : DataArray
         data to find zeros of
    dim : str
         name of dimension in xray
    npoints : int
         (optional) number of points for interpolation

    Returns
    -------
    zeros : DataArray
         zeros of the DataArray along the dimension specified
    """
    da_interp = interp1d_xray(da, dim, npoints)
    signs = np.sign(da_interp)
    mask = signs.diff(dim, label='lower') != 0
    zeros = mask * mask[dim]
    zeros = zeros.where(zeros != 0)

    return zeros
