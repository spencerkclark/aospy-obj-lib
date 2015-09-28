from aospy import Run
import numpy as np
import pandas as pd

# We're going to go with a test case here in the guise of treating an idealized case as OBS.
# Since there is no seasonal cycle, the time is fairly irrelevant -- not entirely true, but 
# for simple things like time averaging we can treat things that way. It is just an equal weighted 
# average of the elements of the sequence.

varia = ['olr', 'temp', 'sphum', 'ps', 'vcomp', 'swdn_sfc', 'olr', 'lwdn_sfc', 'lwup_sfc', 'flux_t', 'flux_lhe',
         'convection_rain', 'condensation_rain']

control_T85 = Run(
    name='control_T85',
    description=(
        'A test case for using aospy + an idealized simulation.'
        ),
    direc_nc='/archive/skc/idealized_moist_T85/control_T85/gfdl.ncrc2-default-prod/1x0m720d_32pe/history',
    nc_dur=2,
    nc_start_yr=0,
    nc_end_yr=1,
    default_time_range=(pd.to_datetime(np.datetime64('0001-01-01 00:00:00')),pd.to_datetime(np.datetime64('0002-01-01 00:00:00'))),
    nc_dir_struc='one_dir',
    nc_files={v : '00000.1x20days.nc' for v in varia},
    read_mode='xray',
    idealized=True
)

extratropics_15_T85 = Run(
    name='extratropics_0.15_T85',
    description=(
        'Solar absorption decreased by 15% from 30N to 90N'
        ),
    direc_nc='/archive/skc/idealized_moist_alb_T85/extratropics_0.15_T85/gfdl.ncrc2-default-prod/1x0m720d_32pe/history',
    nc_dur=2,
    nc_start_yr=0,
    nc_end_yr=1,
    default_time_range=(pd.to_datetime(np.datetime64('0001-01-01 00:00:00')),pd.to_datetime(np.datetime64('0002-01-01 00:00:00'))),
    nc_dir_struc='one_dir',
    nc_files={v : '00000.1x20days.nc' for v in varia},
    read_mode='xray',
    idealized=True
)

extratropics_037_T85 = Run(
    name='extratropics_0.037_T85',
    description=(
        'Solar absorption decreased by 3.7% from 30N to 90N'
        ),
    direc_nc='/archive/skc/idealized_moist_alb_T85/extratropics_0.037_T85/gfdl.ncrc2-default-prod/1x0m720d_32pe/history',
    nc_dur=2,
    nc_start_yr=0,
    nc_end_yr=1,
    default_time_range=(pd.to_datetime(np.datetime64('0001-01-01 00:00:00')),pd.to_datetime(np.datetime64('0002-01-01 00:00:00'))),
    nc_dir_struc='one_dir',
    nc_files={v : '00000.1x20days.nc' for v in varia},
    read_mode='xray',
    idealized=True
)

tropics_10_T85 = Run(
    name='tropics_0.1_T85',
    description=(
        'Solar absorption decreased by 10% from EQ to 30N'
        ),
    direc_nc='/archive/skc/idealized_moist_alb_T85/tropics_0.1_T85/gfdl.ncrc2-default-prod/1x0m720d_32pe/history',
    nc_dur=2,
    nc_start_yr=0,
    nc_end_yr=1,
    default_time_range=(pd.to_datetime(np.datetime64('0001-01-01 00:00:00')),pd.to_datetime(np.datetime64('0002-01-01 00:00:00'))),
    nc_dir_struc='one_dir',
    nc_files={v : '00000.1x20days.nc' for v in varia},
    read_mode='xray',
    idealized=True
)

tropics_025_T85 = Run(
    name='tropics_0.025_T85',
    description=(
        'Solar absorption decreased by 2.5% from EQ to 30N'
        ),
    direc_nc='/archive/skc/idealized_moist_alb_T85/tropics_0.025_T85/gfdl.ncrc2-default-prod/1x0m720d_32pe/history',
    nc_dur=2,
    nc_start_yr=0,
    nc_end_yr=1,
    default_time_range=(pd.to_datetime(np.datetime64('0001-01-01 00:00:00')),pd.to_datetime(np.datetime64('0002-01-01 00:00:00'))),
    nc_dir_struc='one_dir',
    nc_files={v : '00000.1x20days.nc' for v in varia},
    read_mode='xray',
    idealized=True
)
