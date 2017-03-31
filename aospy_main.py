"""Main script for executing calculations using aospy.

Before using this script
------------------------

It is best to copy this template into a separate directory before populating it
with the names from your own object library.  You can also always get a fresh
copy from https://github.com/spencerahill/aospy/examples/aospy_main.py

How to use this script
----------------------

On the example library and data
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This script comes pre-populated with names taken from the example aospy object
library that is included in this directory in the `example_obj_lib.py` module.
So you can try it out on the sample data without modifying anything at all.

This simple example library includes only one Proj, one Model, and one Run, but
it also includes multiple Var and Region objects over which you can automate
computations.  The date range, sub-annual averaging period, and output data
types can all also be modified.

On your own library and data
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To use As a user, there are only two places you need to modify the code:

1. (Only done once) Replace 'example_library' with the name of your object
   library.  Consult the documentation for instructions on how to make your
   object library findable by Python if this statement generates errors.

2. (Done as often as desired) Replace the dummy project, model, run, var, and
   region names with the names of your objects that you want to perform
   calculations with.

   Also alter the other parameters -- date_range, etc. -- to your liking.

Running the script
------------------

Once the parameters are all set as desired, execute the script from the command
line ::

  ./aospy_main.py  # after `cd` to the directory where you've made your copy

"""
# C.f. instructions above, replace `example_obj_lib` with your own object
# library if you wish to use this on your own data.
from datetime import datetime

from aospy import submit_mult_calcs
import aospy_user


calc_suite_specs = dict(
    # Consult `CalcInterface` API reference for further explanation
    # of each option and accepted values.

    # The desired library of aospy objects.
    library=aospy_user,
    # List of the project names.
    projects=[aospy_user.projs.projects.itcz],
    # List of the model names.
    models=[aospy_user.models.models.idealized_moist_rad],
    # List of the run names, or 'default', or 'all'.
    # runs=[aospy_user.runs.idealized_moist_rad.control],
    runs=[aospy_user.runs.idealized_moist_rad.control],
    # List of the variable names.
    variables=[aospy_user.variables.idealized_moist.water.precip_im,
               aospy_user.variables.idealized_moist.water.condensation_rain],
    # List of the region names, or 'all'.
    regions=[aospy_user.regions.tropics, aospy_user.regions.sahel],

    # Start and end dates (inclusive).  List of tuples and/or 'default'.
    # If list of tuples, tuples are of form (start_date, end_date), where
    # start_date and end_date are datetime.datetime objects.  Be sure to
    # add `import datetime` above if using `datetime.datetime` objects.
    date_ranges=[(datetime(3, 1, 1), datetime(6, 12, 31))],

    # Sub-annual time-interval to average over.  List of 'ann', seasonal
    # string (e.g. 'djf'), or month integer (1 for Jan, 2 for Feb, etc).
    output_time_intervals=['ann'],
    # List of tuples, each listing the desired spatiotemporal reductions.
    output_time_regional_reductions=['reg.av'],
    # List of desired vertical reductions to perform.
    output_vertical_reductions=[None],

    # List of time spacing of input data.
    input_time_intervals=['monthly'],
    # List of time type of input data.
    input_time_datatypes=['ts'],
    # List the time offset dictionaries (if desired) to apply to the input
    # data (e.g. [{'days': -15}]).
    input_time_offsets=[{'days': -15}],
    # List of vertical data type of input data.
    input_vertical_datatypes=['sigma'],

)

# Submit all calculations in parallel.  Requires 'multiprocess' package
# (which can be obtained e.g. via `pip install multiprocess`).
parallelize = False

# List calculations to be performed and prompt for your verification.
prompt_verify = True


# Don't modify this statement.
if __name__ == '__main__':
    calcs = submit_mult_calcs(calc_suite_specs,
                              parallelize=parallelize,
                              prompt_verify=prompt_verify)
