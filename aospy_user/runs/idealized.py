from aospy import Run
import numpy as np
import pandas as pd
from datetime import datetime, timedelta

# We're going to go with a test case here in the guise of treating an idealized case as OBS.
# Since there is no seasonal cycle, the time is fairly irrelevant -- not entirely true, but 
# for simple things like time averaging we can treat things that way. It is just an equal weighted 
# average of the elements of the sequence.

# S. Clark 10-30-2015: Contrary to what idealized model runs suggest, we start at year 1 NOT 0.
# Also note that it throws things into a 365 day no-leap calendar. So if you want the last
# 360 days you need to be smarter about things. 

varia = ['olr', 'temp', 'sphum', 'ps', 'vcomp', 'swdn_sfc', 'olr', 'lwdn_sfc', 'lwup_sfc', 'flux_t', 'flux_lhe',
         'convection_rain', 'condensation_rain', 'ucomp', 'omega']

# If we run more than four years we'll have to think about leap years, but for now this is OK.
model_start = datetime(1,1,1)
length = timedelta(days=720)
end = model_start + length
analysis_length = timedelta(days=360)
a_start = str(end - analysis_length)
a_end = str(end)

control_T85 = Run(
    name='control_T85',
    description=(
        'A test case for using aospy + an idealized simulation.'
        ),
    data_in_direc='/archive/skc/idealized_moist_T85/control_T85/gfdl.ncrc2-default-prod/1x0m720d_32pe/history',
    data_in_dur=2,
#    data_in_start_date='0000-01-01',
#    data_in_end_date='0001-01-01',
    default_date_range=('0002-01-01', '0003-01-01'),
    data_in_dir_struc='one_dir',
    data_in_files={v : '00000.1x20days.nc' for v in varia},
    idealized=True
)

extratropics_15_T85 = Run(
    name='extratropics_0.15_T85',
    description=(
        'Solar absorption decreased by 15% from 30N to 90N'
        ),
    data_in_direc='/archive/skc/idealized_moist_alb_T85/extratropics_0.15_T85/gfdl.ncrc2-default-prod/1x0m720d_32pe/history',
    data_in_dur=2,
#    data_in_start_date='0000-01-01',
#    data_in_end_date='0001-01-01',
    default_date_range=('0002-01-01','0003-01-01'),
    data_in_dir_struc='one_dir',
    data_in_files={v : '00000.1x20days.nc' for v in varia},
    idealized=True
)

extratropics_037_T85 = Run(
    name='extratropics_0.037_T85',
    description=(
        'Solar absorption decreased by 3.7% from 30N to 90N'
        ),
    data_in_direc='/archive/skc/idealized_moist_alb_T85/extratropics_0.037_T85/gfdl.ncrc2-default-prod/1x0m720d_32pe/history',
    data_in_dur=2,
#    data_in_start_date='0000-01-01',
#    data_in_end_date='0001-01-01',
    default_date_range=('0002-01-01','0003-01-01'),
    data_in_dir_struc='one_dir',
    data_in_files={v : '00000.1x20days.nc' for v in varia},
    idealized=True
)

tropics_10_T85 = Run(
    name='tropics_0.1_T85',
    description=(
        'Solar absorption decreased by 10% from EQ to 30N'
        ),
    data_in_direc='/archive/skc/idealized_moist_alb_T85/tropics_0.1_T85/gfdl.ncrc2-default-prod/1x0m720d_32pe/history',
    data_in_dur=2,
#    data_in_start_date='0000-01-01',
#    data_in_end_date='0001-01-01',
    default_date_range=('0002-01-01','0003-01-01'),
    data_in_dir_struc='one_dir',
    data_in_files={v : '00000.1x20days.nc' for v in varia},
    idealized=True
)

tropics_025_T85 = Run(
    name='tropics_0.025_T85',
    description=(
        'Solar absorption decreased by 2.5% from EQ to 30N'
        ),
    data_in_direc='/archive/skc/idealized_moist_alb_T85/tropics_0.025_T85/gfdl.ncrc2-default-prod/1x0m720d_32pe/history',
    data_in_dur=2,
#    data_in_start_date='0000-01-01',
#    data_in_end_date='0001-01-01',
    default_date_range=('0002-01-01','0003-01-01'),
    data_in_dir_struc='one_dir',
    data_in_files={v : '00000.1x20days.nc' for v in varia},
    idealized=True
)

control_alb_T42 = Run(
    name='control_alb_T42',
    description=(
        'Control case at T42 spectral resolution'
        ),
    data_in_direc='/archive/skc/idealized_moist_alb_T42/control_alb_T42/gfdl.ncrc2-default-prod/1x0m720d_32pe/history',
    data_in_dur=2,
#    data_in_start_date='0000-01-01',
#    data_in_end_date='0001-01-01',
    default_date_range=(a_start,a_end),
    data_in_dir_struc='one_dir',
    data_in_files={v : '00000.1x20days.nc' for v in varia},
    idealized=True
)
