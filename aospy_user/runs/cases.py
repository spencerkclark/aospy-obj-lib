from aospy import Run
import numpy as np
import pandas as pd

am2_control = Run(
    name='am2_control',
    description=(
        'Preindustrial control simulation.'
        ),
    direc_nc=('/archive/Yi.Ming/sm2.1_fixed/SM2.1U_Control-1860_lm2_aie_rerun6.YIM/pp'),
    nc_dur=100,
    nc_start_yr=1,
    nc_end_yr=100,
    default_yr_range=(21,100),
    read_mode='xray',
    nc_start_day=pd.to_datetime(np.datetime64('0021-01-01 00:00:00')),
    nc_end_day=pd.to_datetime(np.datetime64('0100-01-01 00:00:00')),
    default_time_range=(pd.to_datetime(np.datetime64('0021-01-01 00:00:00')), pd.to_datetime(np.datetime64('0100-01-01 00:00:00')))
)

# We're going to go with a test case here in the guise of treating an idealized case as OBS.
# Since there is no seasonal cycle, the time is fairly irrelevant -- not entirely true, but 
# for simple things like time averaging we can treat things that way. It is just an equal weighted 
# average of the elements of the sequence.

varia = ['olr', 'temp', 'sphum', 'ps']

dargan_control = Run(
    name='dargan_control',
    description=(
        'A test case for using aospy + an idealized simulation.'
        ),
    direc_nc='/work/skc/idealized_moist_T85/control_T85',
    nc_dur=2,
    nc_start_yr=0,
    nc_end_yr=1,
    default_yr_range=(1,1),
    nc_dir_struc='one_dir',
    nc_files={v : '00000.1x20days.nc' for v in varia},
    read_mode='netcdf4'
)
