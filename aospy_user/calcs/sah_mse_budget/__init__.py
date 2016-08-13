"""My library of functions for use in aospy.

Historically, these assumed input variables in the form of numpy arrays or
masked numpy arrays.  As of October 2015, I have switched to assuming
xarray.DataArrays, to coincide with the same switch within aospy.  However, not
all of the functions in this module have been converted to support this new
datatype.

2016-03-10 [SKC]: Lifted from Spencer Hill's library in an attempt to port
MSE budget functions for use in the idealized moist model with full radiation.
"""
import energy
