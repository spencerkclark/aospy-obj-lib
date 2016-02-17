from aospy import Run

v_atmos = ['temp', 'sphum', 'ps', 'vcomp',
           'flux_t', 'flux_lhe', 'convection_rain',
           'condensation_rain', 'ucomp', 'omega', 't_surf', 'height', 'vor',
           'div', 'sw_down_sfc', 'lw_down_sfc', 'netrad_toa',
           'vert_int_tdt_rad',
           'vert_int_tdtlw_rad', 'vert_int_tdtsw_rad', 'dt_tg_rad',
           'dt_tg_diffusion', 'dt_qg_diffusion', 'dt_tg_condensation',
           'dt_tg_convection', 'qo3']

rad_atmos = ['tdt_lw', 'tdt_sw', 'allradp']

# New albedo -- last 1860 days of each run; haven't addressed 3 hourly output
# yet.
control = Run(
    name='control',
    description=(
        'Control simulation of idealized moist run with realistic'
        'radiative transfer.'
    ),
    data_in_direc=('/home/skc/archive/imr_skc/'
                   'control/gfdl.ncrc3-default-repro/'
                   'history'),
    default_date_range=('0003-01-01', '0006-12-31'),
    data_in_dir_struc='one_dir',
    data_in_files={'monthly': {v: ['00010101.atmos_month.nc',
                                   '00020101.atmos_month.nc',
                                   '00030101.atmos_month.nc',
                                   '00040101.atmos_month.nc',
                                   '00050101.atmos_month.nc',
                                   '00060101.atmos_month.nc']
                               for v in v_atmos},
                   'rad_month': {v: ['00010101.atmos_rad_month.nc',
                                     '00020101.atmos_rad_month.nc',
                                     '00030101.atmos_rad_month.nc',
                                     '00040101.atmos_rad_month.nc',
                                     '00050101.atmos_rad_month.nc',
                                     '00060101.atmos_rad_month.nc']
                                 for v in rad_atmos},
                   '3-hourly': {v: '{}.8xday.nc'.format(v) for v in []}}
)

conv_off = Run(
    name='conv_off',
    description=(
        'Control simulation of idealized moist run with realistic'
        'radiative transfer, but no moist convection.'
    ),
    data_in_direc=('/home/skc/archive/imr_skc/'
                   'conv_off/gfdl.ncrc3-default-repro/'
                   'history'),
    default_date_range=('0003-01-01', '0006-12-31'),
    data_in_dir_struc='one_dir',
    data_in_files={'monthly': {v: ['00010101.atmos_month.nc',
                                   '00020101.atmos_month.nc',
                                   '00030101.atmos_month.nc',
                                   '00040101.atmos_month.nc',
                                   '00050101.atmos_month.nc',
                                   '00060101.atmos_month.nc']
                               for v in v_atmos},
                   'rad_month': {v: ['00010101.atmos_rad_month.nc',
                                     '00020101.atmos_rad_month.nc',
                                     '00030101.atmos_rad_month.nc',
                                     '00040101.atmos_rad_month.nc',
                                     '00050101.atmos_rad_month.nc',
                                     '00060101.atmos_rad_month.nc']
                                 for v in rad_atmos},
                   '3-hourly': {v: '{}.8xday.nc'.format(v) for v in []}}
)

double_CO2 = Run(
    name='2xCO2',
    description=(
        'Simulation with fully coupled water vapor, dynamics, and'
        ' radiation.  CO2 at twice current levels.'
    ),
    data_in_direc=('/home/skc/archive/imr_skc/'
                   '2xCO2/gfdl.ncrc3-default-repro/'
                   'history'),
    default_date_range=('0003-01-01', '0006-12-31'),
    data_in_dir_struc='one_dir',
    data_in_files={'monthly': {v: ['00010101.atmos_month.nc',
                                   '00020101.atmos_month.nc',
                                   '00030101.atmos_month.nc',
                                   '00040101.atmos_month.nc',
                                   '00050101.atmos_month.nc',
                                   '00060101.atmos_month.nc']
                               for v in v_atmos},
                   'rad_month': {v: ['00010101.atmos_rad_month.nc',
                                     '00020101.atmos_rad_month.nc',
                                     '00030101.atmos_rad_month.nc',
                                     '00040101.atmos_rad_month.nc',
                                     '00050101.atmos_rad_month.nc',
                                     '00060101.atmos_rad_month.nc']
                                 for v in rad_atmos},
                   '3-hourly': {v: '{}.8xday.nc'.format(v) for v in []}}
)

fixed_h2o = Run(
    name='fixed_h2o',
    description=(
        'Simulation with fully coupled water vapor and dynamics.'
        ' Radiation code sees constant climatological water vapor pattern.'
    ),
    data_in_direc=('/home/skc/archive/imr_skc/'
                   'fixed_h2o/gfdl.ncrc3-default-repro/'
                   'history'),
    default_date_range=('0003-01-01', '0006-12-31'),
    data_in_dir_struc='one_dir',
    data_in_files={'monthly': {v: ['00010101.atmos_month.nc',
                                   '00020101.atmos_month.nc',
                                   '00030101.atmos_month.nc',
                                   '00040101.atmos_month.nc',
                                   '00050101.atmos_month.nc',
                                   '00060101.atmos_month.nc']
                               for v in v_atmos},
                   'rad_month': {v: ['00010101.atmos_rad_month.nc',
                                     '00020101.atmos_rad_month.nc',
                                     '00030101.atmos_rad_month.nc',
                                     '00040101.atmos_rad_month.nc',
                                     '00050101.atmos_rad_month.nc',
                                     '00060101.atmos_rad_month.nc']
                                 for v in rad_atmos},
                   '3-hourly': {v: '{}.8xday.nc'.format(v) for v in []}}
)

fixed_h2o_2xCO2 = Run(
    name='fixed_h2o_2xCO2',
    description=(
        'Simulation with fully coupled water vapor and dynamics.'
        ' Radiation code sees constant climatological water vapor pattern'
        ' from 1xCO2 control experiment.  Atmosphere contains double'
        ' modern-day CO2.'
    ),
    data_in_direc=('/home/skc/archive/imr_skc/'
                   'fixed_h2o_2xCO2/gfdl.ncrc3-default-repro/'
                   'history'),
    default_date_range=('0003-01-01', '0006-12-31'),
    data_in_dir_struc='one_dir',
    data_in_files={'monthly': {v: ['00010101.atmos_month.nc',
                                   '00020101.atmos_month.nc',
                                   '00030101.atmos_month.nc',
                                   '00040101.atmos_month.nc',
                                   '00050101.atmos_month.nc',
                                   '00060101.atmos_month.nc']
                               for v in v_atmos},
                   'rad_month': {v: ['00010101.atmos_rad_month.nc',
                                     '00020101.atmos_rad_month.nc',
                                     '00030101.atmos_rad_month.nc',
                                     '00040101.atmos_rad_month.nc',
                                     '00050101.atmos_rad_month.nc',
                                     '00060101.atmos_rad_month.nc']
                                 for v in rad_atmos},
                   '3-hourly': {v: '{}.8xday.nc'.format(v) for v in []}}
)

asym_e5 = Run(
    name='asym_e5',
    description=(
        'Fully coupled water vapor, dynamics, and radiation.'
        ' 10 W m-2 asymmetry in solar forcing imposed in extratropics.'
    ),
    data_in_direc=('/home/skc/archive/imr_skc/'
                   'asym_e5/gfdl.ncrc3-default-repro/'
                   'history'),
    default_date_range=('0003-01-01', '0006-12-31'),
    data_in_dir_struc='one_dir',
    data_in_files={'monthly': {v: ['00010101.atmos_month.nc',
                                   '00020101.atmos_month.nc',
                                   '00030101.atmos_month.nc',
                                   '00040101.atmos_month.nc',
                                   '00050101.atmos_month.nc',
                                   '00060101.atmos_month.nc']
                               for v in v_atmos},
                   'rad_month': {v: ['00010101.atmos_rad_month.nc',
                                     '00020101.atmos_rad_month.nc',
                                     '00030101.atmos_rad_month.nc',
                                     '00040101.atmos_rad_month.nc',
                                     '00050101.atmos_rad_month.nc',
                                     '00060101.atmos_rad_month.nc']
                                 for v in rad_atmos},
                   '3-hourly': {v: '{}.8xday.nc'.format(v) for v in []}}
)

asym_t5 = Run(
    name='asym_t5',
    description=(
        'Fully coupled water vapor, dynamics, and radiation.'
        ' 10 W m-2 asymmetry in solar forcing imposed in tropics.'
    ),
    data_in_direc=('/home/skc/archive/imr_skc/'
                   'asym_t5/gfdl.ncrc3-default-repro/'
                   'history'),
    default_date_range=('0003-01-01', '0006-12-31'),
    data_in_dir_struc='one_dir',
    data_in_files={'monthly': {v: ['00010101.atmos_month.nc',
                                   '00020101.atmos_month.nc',
                                   '00030101.atmos_month.nc',
                                   '00040101.atmos_month.nc',
                                   '00050101.atmos_month.nc',
                                   '00060101.atmos_month.nc']
                               for v in v_atmos},
                   'rad_month': {v: ['00010101.atmos_rad_month.nc',
                                     '00020101.atmos_rad_month.nc',
                                     '00030101.atmos_rad_month.nc',
                                     '00040101.atmos_rad_month.nc',
                                     '00050101.atmos_rad_month.nc',
                                     '00060101.atmos_rad_month.nc']
                                 for v in rad_atmos},
                   '3-hourly': {v: '{}.8xday.nc'.format(v) for v in []}}
)

asym_e15 = Run(
    name='asym_e15',
    description=(
        'Fully coupled water vapor, dynamics, and radiation.'
        ' 30 W m-2 asymmetry in solar forcing imposed in extratropics.'
    ),
    data_in_direc=('/home/skc/archive/imr_skc/'
                   'asym_e15/gfdl.ncrc3-default-repro/'
                   'history'),
    default_date_range=('0003-01-01', '0006-12-31'),
    data_in_dir_struc='one_dir',
    data_in_files={'monthly': {v: ['00010101.atmos_month.nc',
                                   '00020101.atmos_month.nc',
                                   '00030101.atmos_month.nc',
                                   '00040101.atmos_month.nc',
                                   '00050101.atmos_month.nc',
                                   '00060101.atmos_month.nc']
                               for v in v_atmos},
                   'rad_month': {v: ['00010101.atmos_rad_month.nc',
                                     '00020101.atmos_rad_month.nc',
                                     '00030101.atmos_rad_month.nc',
                                     '00040101.atmos_rad_month.nc',
                                     '00050101.atmos_rad_month.nc',
                                     '00060101.atmos_rad_month.nc']
                                 for v in rad_atmos},
                   '3-hourly': {v: '{}.8xday.nc'.format(v) for v in []}}
)

asym_t15 = Run(
    name='asym_t15',
    description=(
        'Fully coupled water vapor, dynamics, and radiation.'
        ' 30 W m-2 asymmetry in solar forcing imposed in tropics.'
    ),
    data_in_direc=('/home/skc/archive/imr_skc/'
                   'asym_t15/gfdl.ncrc3-default-repro/'
                   'history'),
    default_date_range=('0003-01-01', '0006-12-31'),
    data_in_dir_struc='one_dir',
    data_in_files={'monthly': {v: ['00010101.atmos_month.nc',
                                   '00020101.atmos_month.nc',
                                   '00030101.atmos_month.nc',
                                   '00040101.atmos_month.nc',
                                   '00050101.atmos_month.nc',
                                   '00060101.atmos_month.nc']
                               for v in v_atmos},
                   'rad_month': {v: ['00010101.atmos_rad_month.nc',
                                     '00020101.atmos_rad_month.nc',
                                     '00030101.atmos_rad_month.nc',
                                     '00040101.atmos_rad_month.nc',
                                     '00050101.atmos_rad_month.nc',
                                     '00060101.atmos_rad_month.nc']
                                 for v in rad_atmos},
                   '3-hourly': {v: '{}.8xday.nc'.format(v) for v in []}}
)

asym_t20 = Run(
    name='asym_t20',
    description=(
        'Fully coupled water vapor, dynamics, and radiation.'
        ' 40 W m-2 asymmetry in solar forcing imposed in tropics.'
    ),
    data_in_direc=('/home/skc/archive/imr_skc/'
                   'asym_t20/gfdl.ncrc3-default-repro/'
                   'history'),
    default_date_range=('0003-01-01', '0006-12-31'),
    data_in_dir_struc='one_dir',
    data_in_files={'monthly': {v: ['00010101.atmos_month.nc',
                                   '00020101.atmos_month.nc',
                                   '00030101.atmos_month.nc',
                                   '00040101.atmos_month.nc',
                                   '00050101.atmos_month.nc',
                                   '00060101.atmos_month.nc']
                               for v in v_atmos},
                   'rad_month': {v: ['00010101.atmos_rad_month.nc',
                                     '00020101.atmos_rad_month.nc',
                                     '00030101.atmos_rad_month.nc',
                                     '00040101.atmos_rad_month.nc',
                                     '00050101.atmos_rad_month.nc',
                                     '00060101.atmos_rad_month.nc']
                                 for v in rad_atmos},
                   '3-hourly': {v: '{}.8xday.nc'.format(v) for v in []}}
)
