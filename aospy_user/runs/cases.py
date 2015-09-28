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
    default_yr_range=(21,80),
    read_mode='xray',
    nc_start_day=pd.to_datetime(np.datetime64('0021-01-01 00:00:00')),
    nc_end_day=pd.to_datetime(np.datetime64('0100-01-01 00:00:00')),
    default_time_range=(pd.to_datetime(np.datetime64('0021-01-01 00:00:00')), pd.to_datetime(np.datetime64('0081-01-01 00:00:00'))),
    idealized=False
)

am2_tropics = Run(
    name='am2_tropics',
    description=(
        'Anthropogenic sulfate aerosol forcing only in the Northern Hemisphere tropics (EQ to 30N)'
        ),
    direc_nc=('/archive/Yi.Ming/sm2.1_fixed/SM2.1U_Control-1860_lm2_aie2_tropical_rerun6.YIM/pp'),
    nc_dur=20,
    nc_start_yr=1,
    nc_end_yr=80,
    default_yr_range=(21,80),
    read_mode='xray',
    nc_start_day=pd.to_datetime(np.datetime64('0021-01-01 00:00:00')),
    nc_end_day=pd.to_datetime(np.datetime64('0081-01-01 00:00:00')),
    default_time_range=(pd.to_datetime(np.datetime64('0021-01-01 00:00:00')), pd.to_datetime(np.datetime64('0081-01-01 00:00:00'))),
    idealized=False
)

am2_extratropics = Run(
    name='am2_extratropics',
    description=(
        'Anthropogenic sulfate aerosol forcing only in the Northern Hemisphere extratropics (30N to Pole)'
        ),
    direc_nc=('/archive/Yi.Ming/sm2.1_fixed/SM2.1U_Control-1860_lm2_aie2_extropical_rerun6.YIM/pp'),
    nc_dur=20,
    nc_start_yr=1,
    nc_end_yr=80,
    default_yr_range=(21,80),
    read_mode='xray',
    nc_start_day=pd.to_datetime(np.datetime64('0021-01-01 00:00:00')),
    nc_end_day=pd.to_datetime(np.datetime64('0081-01-01 00:00:00')),
    default_time_range=(pd.to_datetime(np.datetime64('0021-01-01 00:00:00')), pd.to_datetime(np.datetime64('0081-01-01 00:00:00'))),
    idealized=False
)

am2_tropics_and_extratropics = Run(
    name='am2_tropics+extratropics',
    description=(
        'Anthropogenic sulfate aerosol forcing everywhere'
        ),
    direc_nc=('/archive/Yi.Ming/sm2.1_fixed/SM2.1U_Control-1860_lm2_aie2_rerun6.YIM/pp'),
    nc_dur=20,
    nc_start_yr=1,
    nc_end_yr=80,
    default_yr_range=(21,80),
    read_mode='xray',
    nc_start_day=pd.to_datetime(np.datetime64('0021-01-01 00:00:00')),
    nc_end_day=pd.to_datetime(np.datetime64('0081-01-01 00:00:00')),
    default_time_range=(pd.to_datetime(np.datetime64('0021-01-01 00:00:00')), pd.to_datetime(np.datetime64('0081-01-01 00:00:00'))),
    idealized=False
)

# REYOI Runs - First year is 1982; we throw that out as spinup; start analysis in 1983.

am2_HadISST_control = Run(
    name='am2_HadISST_control',
    description=(
        '1981-2000 HadISST climatological annual cycle of SSTs and sea '
        'ice repeated annually, with PD atmospheric composition.'
    ),
    direc_nc=('/archive/yim/siena_201203/m45_am2p14_1990/'
              'gfdl.ncrc2-intel-prod/pp'),
    nc_dur=16,
    nc_start_yr=1983,
    nc_end_yr=1998,
    default_yr_range=(1983, 1998),
    read_mode='xray',
    nc_start_day=pd.to_datetime(np.datetime64('1983-01-01 00:00:00')),
    nc_end_day=pd.to_datetime(np.datetime64('1999-01-01 00:00:00')),
    default_time_range=(pd.to_datetime(np.datetime64('1983-01-01 00:00:00')), pd.to_datetime(np.datetime64('1999-01-01 00:00:00'))),
    idealized=False
)

am2_reyoi_control = Run(
    name='am2_reyoi_control',
    tags=['reyoi', 'cont'],
    description='PI atmos and Reynolds OI climatological SSTs',
    direc_nc='/archive/Spencer.Hill/am2/am2clim_reyoi/gfdl.ncrc2-default-prod/pp',
    nc_dur=1,
    nc_start_yr=1982,
    nc_end_yr=2012,
    default_yr_range=(1983, 2012),
    read_mode='xray',
    nc_start_day=pd.to_datetime(np.datetime64('1983-01-01 00:00:00')),
    nc_end_day=pd.to_datetime(np.datetime64('1999-01-01 00:00:00')),
    default_time_range=(pd.to_datetime(np.datetime64('1983-01-01 00:00:00')), pd.to_datetime(np.datetime64('1999-01-01 00:00:00'))),
    idealized=False
)

am2_reyoi_extratropics_full = Run(
    name='am2_reyoi_extratropics_full',
    description=(
        'Full SST anomaly pattern applied to REYOI fixed SST climatology.'),
    direc_nc=('/archive/Spencer.Clark/am2/am2clim_reyoi_extratropics_full/gfdl.ncrc2-default-prod/pp'),
    nc_dur=17,
    nc_start_yr=1982,
    nc_end_yr=1998,
    default_yr_range=(1982,1998),
    read_mode='xray',
    nc_start_day=pd.to_datetime(np.datetime64('1983-01-01 00:00:00')),
    nc_end_day=pd.to_datetime(np.datetime64('1999-01-01 00:00:00')),
    default_time_range=(pd.to_datetime(np.datetime64('1983-01-01 00:00:00')), pd.to_datetime(np.datetime64('1999-01-01 00:00:00'))),
    idealized=False
)

am2_reyoi_extratropics_sp = Run(
    name='am2_reyoi_extratropics_sp',
    description=(
        'Spatial Pattern SST anomaly pattern applied to REYOI fixed SST climatology.'),
    direc_nc=('/archive/Spencer.Clark/am2/am2clim_reyoi_extratropics_sp/gfdl.ncrc2-default-prod/pp'),
    nc_dur=17,
    nc_start_yr=1982,
    nc_end_yr=1998,
    default_yr_range=(1982,1998),
    read_mode='xray',
    nc_start_day=pd.to_datetime(np.datetime64('1983-01-01 00:00:00')),
    nc_end_day=pd.to_datetime(np.datetime64('1999-01-01 00:00:00')),
    default_time_range=(pd.to_datetime(np.datetime64('1983-01-01 00:00:00')), pd.to_datetime(np.datetime64('1999-01-01 00:00:00'))),
    idealized=False
)

am2_reyoi_extratropics_u = Run(
    name='am2_reyoi_extratropics_u',
    description=(
        'Uniform SST anomaly pattern applied to REYOI fixed SST climatology.'),
    direc_nc=('/archive/Spencer.Clark/am2/am2clim_reyoi_extratropics_u/gfdl.ncrc2-default-prod/pp'),
    nc_dur=17,
    nc_start_yr=1982,
    nc_end_yr=1998,
    default_yr_range=(1982,1998),
    read_mode='xray',
    nc_start_day=pd.to_datetime(np.datetime64('1983-01-01 00:00:00')),
    nc_end_day=pd.to_datetime(np.datetime64('1999-01-01 00:00:00')),
    default_time_range=(pd.to_datetime(np.datetime64('1983-01-01 00:00:00')), pd.to_datetime(np.datetime64('1999-01-01 00:00:00'))),
    idealized=False
)


# We're going to go with a test case here in the guise of treating an idealized case as OBS.
# Since there is no seasonal cycle, the time is fairly irrelevant -- not entirely true, but 
# for simple things like time averaging we can treat things that way. It is just an equal weighted 
# average of the elements of the sequence.

varia = ['olr', 'temp', 'sphum', 'ps', 'vcomp', 'swdn_sfc', 'olr', 'lwdn_sfc', 'lwup_sfc', 'flux_t', 'flux_lhe',
         'convection_rain', 'condensation_rain']

dargan_control = Run(
    name='dargan_control',
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
