# from aospy import Run

# v_atmos = ['temp', 'sphum', 'ps', 'vcomp',
#            'flux_t', 'flux_lhe', 'convection_rain',
#            'condensation_rain', 'ucomp', 'omega', 't_surf', 'height', 'vor',
#            'div', 'sw_down_sfc', 'lw_down_sfc', 'netrad_toa',
#            'vert_int_tdt_rad',
#            'vert_int_tdtlw_rad', 'vert_int_tdtsw_rad', 'dt_tg_rad',
#            'dt_tg_diffusion', 'dt_qg_diffusion', 'dt_tg_condensation',
#            'dt_tg_convection', 'qo3', 'flux_oceanq', 'rh', 'vor', 'div',
#            'tdt_rad']

# three_hourly = ['condensation_rain', 'convection_rain', 'flux_lhe',
#                 'flux_t', 'height', 'sphum', 'temp', 'ucomp', 'vcomp',
#                 'vert_int_tdt_rad', 'ps']

# rad_atmos = ['tdt_lw', 'tdt_sw', 'tdt_rad', 'swdn_toa']

# # New albedo -- last 1860 days of each run; haven't addressed 3 hourly output
# # yet.
# control = Run(
#     name='control',
#     description=(
#         'Control simulation of idealized moist run with realistic'
#         'radiative transfer.'
#     ),
#     data_in_direc=('/archive/Spencer.Clark/imr_skc/'
#                    'control/gfdl.ncrc3-default-repro/1/'
#                    'history'),
#     default_date_range=('0003-01-01', '0006-12-31'),
#     data_in_dir_struc='one_dir',
#     data_in_files={'monthly': {v: ['00010101.atmos_month.nc',
#                                    '00020101.atmos_month.nc',
#                                    '00030101.atmos_month.nc',
#                                    '00040101.atmos_month.nc',
#                                    '00050101.atmos_month.nc',
#                                    '00060101.atmos_month.nc']
#                                for v in v_atmos},
#                    'rad_month': {v: ['00010101.atmos_rad_month.nc',
#                                      '00020101.atmos_rad_month.nc',
#                                      '00030101.atmos_rad_month.nc',
#                                      '00040101.atmos_rad_month.nc',
#                                      '00050101.atmos_rad_month.nc',
#                                      '00060101.atmos_rad_month.nc']
#                                  for v in rad_atmos},
#                    '3-hourly': {v: ['000{}0101.atmos_8xday.{}.nc'.format(y, v)
#                                     for y in range(6, 7)]
#                                 for v in three_hourly}}  # SKC: for now just do one year.
# )

# conv_off = Run(
#     name='conv_off',
#     description=(
#         'Control simulation of idealized moist run with realistic'
#         'radiative transfer, but no moist convection.'
#     ),
#     data_in_direc=('/archive/Spencer.Clark/imr_skc/'
#                    'conv_off/gfdl.ncrc3-default-repro/'
#                    'history'),
#     default_date_range=('0003-01-01', '0006-12-31'),
#     data_in_dir_struc='one_dir',
#     data_in_files={'monthly': {v: ['00010101.atmos_month.nc',
#                                    '00020101.atmos_month.nc',
#                                    '00030101.atmos_month.nc',
#                                    '00040101.atmos_month.nc',
#                                    '00050101.atmos_month.nc',
#                                    '00060101.atmos_month.nc']
#                                for v in v_atmos},
#                    'rad_month': {v: ['00010101.atmos_rad_month.nc',
#                                      '00020101.atmos_rad_month.nc',
#                                      '00030101.atmos_rad_month.nc',
#                                      '00040101.atmos_rad_month.nc',
#                                      '00050101.atmos_rad_month.nc',
#                                      '00060101.atmos_rad_month.nc']
#                                  for v in rad_atmos},
#                    '3-hourly': {v: '{}.8xday.nc'.format(v) for v in []}}
# )

# fixed_h2o_conv_off = Run(
#     name='fixed_h2o_conv_off',
#     description=(
#         'Control simulation of idealized moist run with fixed'
#         'radiative transfer, and no moist convection.'
#     ),
#     data_in_direc=('/archive/Spencer.Clark/imr_skc/'
#                    'fixed_h2o_conv_off/gfdl.ncrc3-default-repro/5/'
#                    'history'),
#     default_date_range=('0003-01-01', '0006-12-31'),
#     data_in_dir_struc='one_dir',
#     data_in_files={'monthly': {v: ['00010101.atmos_month.nc',
#                                    '00020101.atmos_month.nc',
#                                    '00030101.atmos_month.nc',
#                                    '00040101.atmos_month.nc',
#                                    '00050101.atmos_month.nc',
#                                    '00060101.atmos_month.nc']
#                                for v in v_atmos},
#                    'rad_month': {v: ['00010101.atmos_rad_month.nc',
#                                      '00020101.atmos_rad_month.nc',
#                                      '00030101.atmos_rad_month.nc',
#                                      '00040101.atmos_rad_month.nc',
#                                      '00050101.atmos_rad_month.nc',
#                                      '00060101.atmos_rad_month.nc']
#                                  for v in rad_atmos},
#                    '3-hourly': {v: '{}.8xday.nc'.format(v) for v in []}}
# )

# double_CO2 = Run(
#     name='2xCO2',
#     description=(
#         'Simulation with fully coupled water vapor, dynamics, and'
#         ' radiation.  CO2 at twice current levels.'
#     ),
#     data_in_direc=('/archive/Spencer.Clark/imr_skc/'
#                    '2xCO2/gfdl.ncrc3-default-repro/'
#                    'history'),
#     default_date_range=('0003-01-01', '0006-12-31'),
#     data_in_dir_struc='one_dir',
#     data_in_files={'monthly': {v: ['00010101.atmos_month.nc',
#                                    '00020101.atmos_month.nc',
#                                    '00030101.atmos_month.nc',
#                                    '00040101.atmos_month.nc',
#                                    '00050101.atmos_month.nc',
#                                    '00060101.atmos_month.nc']
#                                for v in v_atmos},
#                    'rad_month': {v: ['00010101.atmos_rad_month.nc',
#                                      '00020101.atmos_rad_month.nc',
#                                      '00030101.atmos_rad_month.nc',
#                                      '00040101.atmos_rad_month.nc',
#                                      '00050101.atmos_rad_month.nc',
#                                      '00060101.atmos_rad_month.nc']
#                                  for v in rad_atmos},
#                    '3-hourly': {v: '{}.8xday.nc'.format(v) for v in []}}
# )

# fixed_h2o = Run(
#     name='fixed_h2o',
#     description=(
#         'Simulation with fully coupled water vapor and dynamics.'
#         ' Radiation code sees constant climatological water vapor pattern.'
#     ),
#     data_in_direc=('/archive/Spencer.Clark/imr_skc/'
#                    'fixed_h2o/gfdl.ncrc3-default-repro/'
#                    'history'),
#     default_date_range=('0003-01-01', '0006-12-31'),
#     data_in_dir_struc='one_dir',
#     data_in_files={'monthly': {v: ['00010101.atmos_month.nc',
#                                    '00020101.atmos_month.nc',
#                                    '00030101.atmos_month.nc',
#                                    '00040101.atmos_month.nc',
#                                    '00050101.atmos_month.nc',
#                                    '00060101.atmos_month.nc']
#                                for v in v_atmos},
#                    'rad_month': {v: ['00010101.atmos_rad_month.nc',
#                                      '00020101.atmos_rad_month.nc',
#                                      '00030101.atmos_rad_month.nc',
#                                      '00040101.atmos_rad_month.nc',
#                                      '00050101.atmos_rad_month.nc',
#                                      '00060101.atmos_rad_month.nc']
#                                  for v in rad_atmos},
#                    '3-hourly': {v: '{}.8xday.nc'.format(v) for v in []}}
# )

# fixed_h2o_2xCO2 = Run(
#     name='fixed_h2o_2xCO2',
#     description=(
#         'Simulation with fully coupled water vapor and dynamics.'
#         ' Radiation code sees constant climatological water vapor pattern'
#         ' from 1xCO2 control experiment.  Atmosphere contains double'
#         ' modern-day CO2.'
#     ),
#     data_in_direc=('/archive/Spencer.Clark/imr_skc/'
#                    'fixed_h2o_2xCO2/gfdl.ncrc3-default-repro/'
#                    'history'),
#     default_date_range=('0003-01-01', '0006-12-31'),
#     data_in_dir_struc='one_dir',
#     data_in_files={'monthly': {v: ['00010101.atmos_month.nc',
#                                    '00020101.atmos_month.nc',
#                                    '00030101.atmos_month.nc',
#                                    '00040101.atmos_month.nc',
#                                    '00050101.atmos_month.nc',
#                                    '00060101.atmos_month.nc']
#                                for v in v_atmos},
#                    'rad_month': {v: ['00010101.atmos_rad_month.nc',
#                                      '00020101.atmos_rad_month.nc',
#                                      '00030101.atmos_rad_month.nc',
#                                      '00040101.atmos_rad_month.nc',
#                                      '00050101.atmos_rad_month.nc',
#                                      '00060101.atmos_rad_month.nc']
#                                  for v in rad_atmos},
#                    '3-hourly': {v: '{}.8xday.nc'.format(v) for v in []}}
# )

# asym_e5 = Run(
#     name='asym_e5',
#     description=(
#         'Fully coupled water vapor, dynamics, and radiation.'
#         ' 10 W m-2 asymmetry in solar forcing imposed in extratropics.'
#     ),
#     data_in_direc=('/archive/Spencer.Clark/imr_skc/'
#                    'asym_e5/gfdl.ncrc3-default-repro/'
#                    'history'),
#     default_date_range=('0003-01-01', '0006-12-31'),
#     data_in_dir_struc='one_dir',
#     data_in_files={'monthly': {v: ['00010101.atmos_month.nc',
#                                    '00020101.atmos_month.nc',
#                                    '00030101.atmos_month.nc',
#                                    '00040101.atmos_month.nc',
#                                    '00050101.atmos_month.nc',
#                                    '00060101.atmos_month.nc']
#                                for v in v_atmos},
#                    'rad_month': {v: ['00010101.atmos_rad_month.nc',
#                                      '00020101.atmos_rad_month.nc',
#                                      '00030101.atmos_rad_month.nc',
#                                      '00040101.atmos_rad_month.nc',
#                                      '00050101.atmos_rad_month.nc',
#                                      '00060101.atmos_rad_month.nc']
#                                  for v in rad_atmos},
#                    '3-hourly': {v: '{}.8xday.nc'.format(v) for v in []}}
# )

# asym_t5 = Run(
#     name='asym_t5',
#     description=(
#         'Fully coupled water vapor, dynamics, and radiation.'
#         ' 10 W m-2 asymmetry in solar forcing imposed in tropics.'
#     ),
#     data_in_direc=('/archive/Spencer.Clark/imr_skc/'
#                    'asym_t5/gfdl.ncrc3-default-repro/'
#                    'history'),
#     default_date_range=('0003-01-01', '0006-12-31'),
#     data_in_dir_struc='one_dir',
#     data_in_files={'monthly': {v: ['00010101.atmos_month.nc',
#                                    '00020101.atmos_month.nc',
#                                    '00030101.atmos_month.nc',
#                                    '00040101.atmos_month.nc',
#                                    '00050101.atmos_month.nc',
#                                    '00060101.atmos_month.nc']
#                                for v in v_atmos},
#                    'rad_month': {v: ['00010101.atmos_rad_month.nc',
#                                      '00020101.atmos_rad_month.nc',
#                                      '00030101.atmos_rad_month.nc',
#                                      '00040101.atmos_rad_month.nc',
#                                      '00050101.atmos_rad_month.nc',
#                                      '00060101.atmos_rad_month.nc']
#                                  for v in rad_atmos},
#                    '3-hourly': {v: '{}.8xday.nc'.format(v) for v in []}}
# )

# asym_e15 = Run(
#     name='asym_e15',
#     description=(
#         'Fully coupled water vapor, dynamics, and radiation.'
#         ' 30 W m-2 asymmetry in solar forcing imposed in extratropics.'
#     ),
#     data_in_direc=('/archive/Spencer.Clark/imr_skc/'
#                    'asym_e15/gfdl.ncrc3-default-repro/2/'
#                    'history'),
#     default_date_range=('0003-01-01', '0006-12-31'),
#     data_in_dir_struc='one_dir',
#     data_in_files={'monthly': {v: ['00010101.atmos_month.nc',
#                                    '00020101.atmos_month.nc',
#                                    '00030101.atmos_month.nc',
#                                    '00040101.atmos_month.nc',
#                                    '00050101.atmos_month.nc',
#                                    '00060101.atmos_month.nc']
#                                for v in v_atmos},
#                    'rad_month': {v: ['00010101.atmos_rad_month.nc',
#                                      '00020101.atmos_rad_month.nc',
#                                      '00030101.atmos_rad_month.nc',
#                                      '00040101.atmos_rad_month.nc',
#                                      '00050101.atmos_rad_month.nc',
#                                      '00060101.atmos_rad_month.nc']
#                                  for v in rad_atmos},
#                    '3-hourly': {v: '{}.8xday.nc'.format(v) for v in []}}
# )

# asym_t15 = Run(
#     name='asym_t15',
#     description=(
#         'Fully coupled water vapor, dynamics, and radiation.'
#         ' 30 W m-2 asymmetry in solar forcing imposed in tropics.'
#     ),
#     data_in_direc=('/archive/Spencer.Clark/imr_skc/'
#                    'asym_t15/gfdl.ncrc3-default-repro/2/'
#                    'history'),
#     default_date_range=('0003-01-01', '0006-12-31'),
#     data_in_dir_struc='one_dir',
#     data_in_files={'monthly': {v: ['00010101.atmos_month.nc',
#                                    '00020101.atmos_month.nc',
#                                    '00030101.atmos_month.nc',
#                                    '00040101.atmos_month.nc',
#                                    '00050101.atmos_month.nc',
#                                    '00060101.atmos_month.nc']
#                                for v in v_atmos},
#                    'rad_month': {v: ['00010101.atmos_rad_month.nc',
#                                      '00020101.atmos_rad_month.nc',
#                                      '00030101.atmos_rad_month.nc',
#                                      '00040101.atmos_rad_month.nc',
#                                      '00050101.atmos_rad_month.nc',
#                                      '00060101.atmos_rad_month.nc']
#                                  for v in rad_atmos},
#                    '3-hourly': {v: '{}.8xday.nc'.format(v) for v in []}}
# )

# asym_e18 = Run(
#     name='asym_e18',
#     description=(
#         'Fully coupled water vapor, dynamics, and radiation.'
#         ' 36 W m-2 asymmetry in solar forcing imposed in extratropics.'
#     ),
#     data_in_direc=('/archive/Spencer.Clark/imr_skc/'
#                    'asym_e18/gfdl.ncrc3-default-repro/'
#                    'history'),
#     default_date_range=('0003-01-01', '0006-12-31'),
#     data_in_dir_struc='one_dir',
#     data_in_files={'monthly': {v: ['00010101.atmos_month.nc',
#                                    '00020101.atmos_month.nc',
#                                    '00030101.atmos_month.nc',
#                                    '00040101.atmos_month.nc',
#                                    '00050101.atmos_month.nc',
#                                    '00060101.atmos_month.nc']
#                                for v in v_atmos},
#                    'rad_month': {v: ['00010101.atmos_rad_month.nc',
#                                      '00020101.atmos_rad_month.nc',
#                                      '00030101.atmos_rad_month.nc',
#                                      '00040101.atmos_rad_month.nc',
#                                      '00050101.atmos_rad_month.nc',
#                                      '00060101.atmos_rad_month.nc']
#                                  for v in rad_atmos},
#                    '3-hourly': {v: '{}.8xday.nc'.format(v) for v in []}}
# )

# asym_t18 = Run(
#     name='asym_t18',
#     description=(
#         'Fully coupled water vapor, dynamics, and radiation.'
#         ' 36 W m-2 asymmetry in solar forcing imposed in tropics.'
#     ),
#     data_in_direc=('/archive/Spencer.Clark/imr_skc/'
#                    'asym_t18/gfdl.ncrc3-default-repro/'
#                    'history'),
#     default_date_range=('0003-01-01', '0006-12-31'),
#     data_in_dir_struc='one_dir',
#     data_in_files={'monthly': {v: ['00010101.atmos_month.nc',
#                                    '00020101.atmos_month.nc',
#                                    '00030101.atmos_month.nc',
#                                    '00040101.atmos_month.nc',
#                                    '00050101.atmos_month.nc',
#                                    '00060101.atmos_month.nc']
#                                for v in v_atmos},
#                    'rad_month': {v: ['00010101.atmos_rad_month.nc',
#                                      '00020101.atmos_rad_month.nc',
#                                      '00030101.atmos_rad_month.nc',
#                                      '00040101.atmos_rad_month.nc',
#                                      '00050101.atmos_rad_month.nc',
#                                      '00060101.atmos_rad_month.nc']
#                                  for v in rad_atmos},
#                    '3-hourly': {v: '{}.8xday.nc'.format(v) for v in []}}
# )

# asym_t20 = Run(
#     name='asym_t20',
#     description=(
#         'Fully coupled water vapor, dynamics, and radiation.'
#         ' 40 W m-2 asymmetry in solar forcing imposed in tropics.'
#     ),
#     data_in_direc=('/archive/Spencer.Clark/imr_skc/'
#                    'asym_t20/gfdl.ncrc3-default-repro/'
#                    'history'),
#     default_date_range=('0003-01-01', '0006-12-31'),
#     data_in_dir_struc='one_dir',
#     data_in_files={'monthly': {v: ['00010101.atmos_month.nc',
#                                    '00020101.atmos_month.nc',
#                                    '00030101.atmos_month.nc',
#                                    '00040101.atmos_month.nc',
#                                    '00050101.atmos_month.nc',
#                                    '00060101.atmos_month.nc']
#                                for v in v_atmos},
#                    'rad_month': {v: ['00010101.atmos_rad_month.nc',
#                                      '00020101.atmos_rad_month.nc',
#                                      '00030101.atmos_rad_month.nc',
#                                      '00040101.atmos_rad_month.nc',
#                                      '00050101.atmos_rad_month.nc',
#                                      '00060101.atmos_rad_month.nc']
#                                  for v in rad_atmos},
#                    '3-hourly': {v: '{}.8xday.nc'.format(v) for v in []}}
# )

# asym_e5_conv_off = Run(
#     name='asym_e5_conv_off',
#     description=(
#         'Fully coupled water vapor, dynamics, and radiation.'
#         ' 10 W m-2 asymmetry in solar forcing imposed in extratropics.'
#         ' Moist convection is turned off in the model.'
#     ),
#     data_in_direc=('/archive/Spencer.Clark/imr_skc/'
#                    'asym_e5_conv_off/gfdl.ncrc3-default-repro/'
#                    'history'),
#     default_date_range=('0003-01-01', '0006-12-31'),
#     data_in_dir_struc='one_dir',
#     data_in_files={'monthly': {v: ['00010101.atmos_month.nc',
#                                    '00020101.atmos_month.nc',
#                                    '00030101.atmos_month.nc',
#                                    '00040101.atmos_month.nc',
#                                    '00050101.atmos_month.nc',
#                                    '00060101.atmos_month.nc']
#                                for v in v_atmos},
#                    'rad_month': {v: ['00010101.atmos_rad_month.nc',
#                                      '00020101.atmos_rad_month.nc',
#                                      '00030101.atmos_rad_month.nc',
#                                      '00040101.atmos_rad_month.nc',
#                                      '00050101.atmos_rad_month.nc',
#                                      '00060101.atmos_rad_month.nc']
#                                  for v in rad_atmos},
#                    '3-hourly': {v: '{}.8xday.nc'.format(v) for v in []}}
# )

# asym_t5_conv_off = Run(
#     name='asym_t5_conv_off',
#     description=(
#         'Fully coupled water vapor, dynamics, and radiation.'
#         ' 10 W m-2 asymmetry in solar forcing imposed in tropics.'
#         ' Moist convection is turned off in the model.'
#     ),
#     data_in_direc=('/archive/Spencer.Clark/imr_skc/'
#                    'asym_t5_conv_off/gfdl.ncrc3-default-repro/'
#                    'history'),
#     default_date_range=('0003-01-01', '0006-12-31'),
#     data_in_dir_struc='one_dir',
#     data_in_files={'monthly': {v: ['00010101.atmos_month.nc',
#                                    '00020101.atmos_month.nc',
#                                    '00030101.atmos_month.nc',
#                                    '00040101.atmos_month.nc',
#                                    '00050101.atmos_month.nc',
#                                    '00060101.atmos_month.nc']
#                                for v in v_atmos},
#                    'rad_month': {v: ['00010101.atmos_rad_month.nc',
#                                      '00020101.atmos_rad_month.nc',
#                                      '00030101.atmos_rad_month.nc',
#                                      '00040101.atmos_rad_month.nc',
#                                      '00050101.atmos_rad_month.nc',
#                                      '00060101.atmos_rad_month.nc']
#                                  for v in rad_atmos},
#                    '3-hourly': {v: '{}.8xday.nc'.format(v) for v in []}}
# )

# asym_e15_conv_off = Run(
#     name='asym_e15_conv_off',
#     description=(
#         'Fully coupled water vapor, dynamics, and radiation.'
#         ' 30 W m-2 asymmetry in solar forcing imposed in extratropics.'
#         ' Moist convection is turned off in the model.'
#     ),
#     data_in_direc=('/archive/Spencer.Clark/imr_skc/'
#                    'asym_e15_conv_off/gfdl.ncrc3-default-repro/'
#                    'history'),
#     default_date_range=('0003-01-01', '0006-12-31'),
#     data_in_dir_struc='one_dir',
#     data_in_files={'monthly': {v: ['00010101.atmos_month.nc',
#                                    '00020101.atmos_month.nc',
#                                    '00030101.atmos_month.nc',
#                                    '00040101.atmos_month.nc',
#                                    '00050101.atmos_month.nc',
#                                    '00060101.atmos_month.nc']
#                                for v in v_atmos},
#                    'rad_month': {v: ['00010101.atmos_rad_month.nc',
#                                      '00020101.atmos_rad_month.nc',
#                                      '00030101.atmos_rad_month.nc',
#                                      '00040101.atmos_rad_month.nc',
#                                      '00050101.atmos_rad_month.nc',
#                                      '00060101.atmos_rad_month.nc']
#                                  for v in rad_atmos},
#                    '3-hourly': {v: '{}.8xday.nc'.format(v) for v in []}}
# )

# asym_t15_conv_off = Run(
#     name='asym_t15_conv_off',
#     description=(
#         'Fully coupled water vapor, dynamics, and radiation.'
#         ' 30 W m-2 asymmetry in solar forcing imposed in tropics.'
#         ' Moist convection is turned off in the model.'
#     ),
#     data_in_direc=('/archive/Spencer.Clark/imr_skc/'
#                    'asym_t15_conv_off/gfdl.ncrc3-default-repro/1/'
#                    'history'),
#     default_date_range=('0003-01-01', '0006-12-31'),
#     data_in_dir_struc='one_dir',
#     data_in_files={'monthly': {v: ['00010101.atmos_month.nc',
#                                    '00020101.atmos_month.nc',
#                                    '00030101.atmos_month.nc',
#                                    '00040101.atmos_month.nc',
#                                    '00050101.atmos_month.nc',
#                                    '00060101.atmos_month.nc']
#                                for v in v_atmos},
#                    'rad_month': {v: ['00010101.atmos_rad_month.nc',
#                                      '00020101.atmos_rad_month.nc',
#                                      '00030101.atmos_rad_month.nc',
#                                      '00040101.atmos_rad_month.nc',
#                                      '00050101.atmos_rad_month.nc',
#                                      '00060101.atmos_rad_month.nc']
#                                  for v in rad_atmos},
#                    '3-hourly': {v: '{}.8xday.nc'.format(v) for v in []}}
# )

# asym_e18_conv_off = Run(
#     name='asym_e18_conv_off',
#     description=(
#         'Fully coupled water vapor, dynamics, and radiation.'
#         ' 36 W m-2 asymmetry in solar forcing imposed in extratropics.'
#         ' Moist convection is turned off in the model.'
#     ),
#     data_in_direc=('/archive/Spencer.Clark/imr_skc/'
#                    'asym_e18_conv_off/gfdl.ncrc3-default-repro/'
#                    'history'),
#     default_date_range=('0003-01-01', '0006-12-31'),
#     data_in_dir_struc='one_dir',
#     data_in_files={'monthly': {v: ['00010101.atmos_month.nc',
#                                    '00020101.atmos_month.nc',
#                                    '00030101.atmos_month.nc',
#                                    '00040101.atmos_month.nc',
#                                    '00050101.atmos_month.nc',
#                                    '00060101.atmos_month.nc']
#                                for v in v_atmos},
#                    'rad_month': {v: ['00010101.atmos_rad_month.nc',
#                                      '00020101.atmos_rad_month.nc',
#                                      '00030101.atmos_rad_month.nc',
#                                      '00040101.atmos_rad_month.nc',
#                                      '00050101.atmos_rad_month.nc',
#                                      '00060101.atmos_rad_month.nc']
#                                  for v in rad_atmos},
#                    '3-hourly': {v: '{}.8xday.nc'.format(v) for v in []}}
# )

# asym_t18_conv_off = Run(
#     name='asym_t18_conv_off',
#     description=(
#         'Fully coupled water vapor, dynamics, and radiation.'
#         ' 36 W m-2 asymmetry in solar forcing imposed in tropics.'
#         ' Moist convection is turned off in the model.'
#     ),
#     data_in_direc=('/archive/Spencer.Clark/imr_skc/'
#                    'asym_t18_conv_off/gfdl.ncrc3-default-repro/'
#                    'history'),
#     default_date_range=('0003-01-01', '0006-12-31'),
#     data_in_dir_struc='one_dir',
#     data_in_files={'monthly': {v: ['00010101.atmos_month.nc',
#                                    '00020101.atmos_month.nc',
#                                    '00030101.atmos_month.nc',
#                                    '00040101.atmos_month.nc',
#                                    '00050101.atmos_month.nc',
#                                    '00060101.atmos_month.nc']
#                                for v in v_atmos},
#                    'rad_month': {v: ['00010101.atmos_rad_month.nc',
#                                      '00020101.atmos_rad_month.nc',
#                                      '00030101.atmos_rad_month.nc',
#                                      '00040101.atmos_rad_month.nc',
#                                      '00050101.atmos_rad_month.nc',
#                                      '00060101.atmos_rad_month.nc']
#                                  for v in rad_atmos},
#                    '3-hourly': {v: '{}.8xday.nc'.format(v) for v in []}}
# )

# asym_e5_conv_off_fixed_h2o = Run(
#     name='asym_e5_conv_off_fixed_h2o',
#     description=(
#         'Fully coupled water vapor, dynamics.  Fixed radiatively active water.'
#         ' 10 W m-2 asymmetry in solar forcing imposed in extratropics.'
#         ' Moist convection is turned off in the model.'
#     ),
#     data_in_direc=('/archive/Spencer.Clark/imr_skc/'
#                    'asym_e5_conv_off_fixed_h2o/gfdl.ncrc3-default-repro/3/'
#                    'history'),
#     default_date_range=('0003-01-01', '0006-12-31'),
#     data_in_dir_struc='one_dir',
#     data_in_files={'monthly': {v: ['00010101.atmos_month.nc',
#                                    '00020101.atmos_month.nc',
#                                    '00030101.atmos_month.nc',
#                                    '00040101.atmos_month.nc',
#                                    '00050101.atmos_month.nc',
#                                    '00060101.atmos_month.nc']
#                                for v in v_atmos},
#                    'rad_month': {v: ['00010101.atmos_rad_month.nc',
#                                      '00020101.atmos_rad_month.nc',
#                                      '00030101.atmos_rad_month.nc',
#                                      '00040101.atmos_rad_month.nc',
#                                      '00050101.atmos_rad_month.nc',
#                                      '00060101.atmos_rad_month.nc']
#                                  for v in rad_atmos},
#                    '3-hourly': {v: '{}.8xday.nc'.format(v) for v in []}}
# )

# asym_t5_conv_off_fixed_h2o = Run(
#     name='asym_t5_conv_off_fixed_h2o',
#     description=(
#         'Fully coupled water vapor, dynamics.  Fixed radiatively active water.'
#         ' 10 W m-2 asymmetry in solar forcing imposed in tropics.'
#         ' Moist convection is turned off in the model.'
#     ),
#     data_in_direc=('/archive/Spencer.Clark/imr_skc/'
#                    'asym_t5_conv_off_fixed_h2o/gfdl.ncrc3-default-repro/2/'
#                    'history'),
#     default_date_range=('0003-01-01', '0006-12-31'),
#     data_in_dir_struc='one_dir',
#     data_in_files={'monthly': {v: ['00010101.atmos_month.nc',
#                                    '00020101.atmos_month.nc',
#                                    '00030101.atmos_month.nc',
#                                    '00040101.atmos_month.nc',
#                                    '00050101.atmos_month.nc',
#                                    '00060101.atmos_month.nc']
#                                for v in v_atmos},
#                    'rad_month': {v: ['00010101.atmos_rad_month.nc',
#                                      '00020101.atmos_rad_month.nc',
#                                      '00030101.atmos_rad_month.nc',
#                                      '00040101.atmos_rad_month.nc',
#                                      '00050101.atmos_rad_month.nc',
#                                      '00060101.atmos_rad_month.nc']
#                                  for v in rad_atmos},
#                    '3-hourly': {v: '{}.8xday.nc'.format(v) for v in []}}
# )

# asym_e15_conv_off_fixed_h2o = Run(
#     name='asym_e15_conv_off_fixed_h2o',
#     description=(
#         'Fully coupled water vapor, dynamics.  Fixed radiatvely active water.'
#         ' 30 W m-2 asymmetry in solar forcing imposed in extratropics.'
#         ' Moist convection is turned off in the model.'
#     ),
#     data_in_direc=('/archive/Spencer.Clark/imr_skc/'
#                    'asym_e15_conv_off_fixed_h2o/gfdl.ncrc3-default-repro/3/'
#                    'history'),
#     default_date_range=('0003-01-01', '0006-12-31'),
#     data_in_dir_struc='one_dir',
#     data_in_files={'monthly': {v: ['00010101.atmos_month.nc',
#                                    '00020101.atmos_month.nc',
#                                    '00030101.atmos_month.nc',
#                                    '00040101.atmos_month.nc',
#                                    '00050101.atmos_month.nc',
#                                    '00060101.atmos_month.nc']
#                                for v in v_atmos},
#                    'rad_month': {v: ['00010101.atmos_rad_month.nc',
#                                      '00020101.atmos_rad_month.nc',
#                                      '00030101.atmos_rad_month.nc',
#                                      '00040101.atmos_rad_month.nc',
#                                      '00050101.atmos_rad_month.nc',
#                                      '00060101.atmos_rad_month.nc']
#                                  for v in rad_atmos},
#                    '3-hourly': {v: '{}.8xday.nc'.format(v) for v in []}}
# )

# asym_t15_conv_off_fixed_h2o = Run(
#     name='asym_t15_conv_off_fixed_h2o',
#     description=(
#         'Fully coupled water vapor, dynamics.  Fixed radiatively active water.'
#         ' 30 W m-2 asymmetry in solar forcing imposed in tropics.'
#         ' Moist convection is turned off in the model.'
#     ),
#     data_in_direc=('/archive/Spencer.Clark/imr_skc/'
#                    'asym_t15_conv_off_fixed_h2o/gfdl.ncrc3-default-repro/2/'
#                    'history'),
#     default_date_range=('0003-01-01', '0006-12-31'),
#     data_in_dir_struc='one_dir',
#     data_in_files={'monthly': {v: ['00010101.atmos_month.nc',
#                                    '00020101.atmos_month.nc',
#                                    '00030101.atmos_month.nc',
#                                    '00040101.atmos_month.nc',
#                                    '00050101.atmos_month.nc',
#                                    '00060101.atmos_month.nc']
#                                for v in v_atmos},
#                    'rad_month': {v: ['00010101.atmos_rad_month.nc',
#                                      '00020101.atmos_rad_month.nc',
#                                      '00030101.atmos_rad_month.nc',
#                                      '00040101.atmos_rad_month.nc',
#                                      '00050101.atmos_rad_month.nc',
#                                      '00060101.atmos_rad_month.nc']
#                                  for v in rad_atmos},
#                    '3-hourly': {v: '{}.8xday.nc'.format(v) for v in []}}
# )

# asym_e18_conv_off_fixed_h2o = Run(
#     name='asym_e18_conv_off_fixed_h2o',
#     description=(
#         'Fully coupled water vapor, dynamics.  Fixed radiatively active water.'
#         ' 36 W m-2 asymmetry in solar forcing imposed in extratropics.'
#         ' Moist convection is turned off in the model.'
#     ),
#     data_in_direc=('/archive/Spencer.Clark/imr_skc/'
#                    'asym_e18_conv_off_fixed_h2o/gfdl.ncrc3-default-repro/3/'
#                    'history'),
#     default_date_range=('0003-01-01', '0006-12-31'),
#     data_in_dir_struc='one_dir',
#     data_in_files={'monthly': {v: ['00010101.atmos_month.nc',
#                                    '00020101.atmos_month.nc',
#                                    '00030101.atmos_month.nc',
#                                    '00040101.atmos_month.nc',
#                                    '00050101.atmos_month.nc',
#                                    '00060101.atmos_month.nc']
#                                for v in v_atmos},
#                    'rad_month': {v: ['00010101.atmos_rad_month.nc',
#                                      '00020101.atmos_rad_month.nc',
#                                      '00030101.atmos_rad_month.nc',
#                                      '00040101.atmos_rad_month.nc',
#                                      '00050101.atmos_rad_month.nc',
#                                      '00060101.atmos_rad_month.nc']
#                                  for v in rad_atmos},
#                    '3-hourly': {v: '{}.8xday.nc'.format(v) for v in []}}
# )

# asym_t18_conv_off_fixed_h2o = Run(
#     name='asym_t18_conv_off_fixed_h2o',
#     description=(
#         'Fully coupled water vapor, dynamics.  Fixed radiatively active water.'
#         ' 36 W m-2 asymmetry in solar forcing imposed in tropics.'
#         ' Moist convection is turned off in the model.'
#     ),
#     data_in_direc=('/archive/Spencer.Clark/imr_skc/'
#                    'asym_t18_conv_off_fixed_h2o/gfdl.ncrc3-default-repro/2/'
#                    'history'),
#     default_date_range=('0003-01-01', '0006-12-31'),
#     data_in_dir_struc='one_dir',
#     data_in_files={'monthly': {v: ['00010101.atmos_month.nc',
#                                    '00020101.atmos_month.nc',
#                                    '00030101.atmos_month.nc',
#                                    '00040101.atmos_month.nc',
#                                    '00050101.atmos_month.nc',
#                                    '00060101.atmos_month.nc']
#                                for v in v_atmos},
#                    'rad_month': {v: ['00010101.atmos_rad_month.nc',
#                                      '00020101.atmos_rad_month.nc',
#                                      '00030101.atmos_rad_month.nc',
#                                      '00040101.atmos_rad_month.nc',
#                                      '00050101.atmos_rad_month.nc',
#                                      '00060101.atmos_rad_month.nc']
#                                  for v in rad_atmos},
#                    '3-hourly': {v: '{}.8xday.nc'.format(v) for v in []}}
# )

# asym_e15_fixed_h2o = Run(
#     name='asym_e15_fixed_h2o',
#     description=(
#         'Radiatvely passive water vapor.'
#         ' 30 W m-2 asymmetry in solar forcing imposed in extratropics.'
#     ),
#     data_in_direc=('/archive/Spencer.Clark/imr_skc/'
#                    'asym_e15_fixed_h2o/gfdl.ncrc3-default-repro/2/'
#                    'history'),
#     default_date_range=('0003-01-01', '0006-12-31'),
#     data_in_dir_struc='one_dir',
#     data_in_files={'monthly': {v: ['00010101.atmos_month.nc',
#                                    '00020101.atmos_month.nc',
#                                    '00030101.atmos_month.nc',
#                                    '00040101.atmos_month.nc',
#                                    '00050101.atmos_month.nc',
#                                    '00060101.atmos_month.nc']
#                                for v in v_atmos},
#                    'rad_month': {v: ['00010101.atmos_rad_month.nc',
#                                      '00020101.atmos_rad_month.nc',
#                                      '00030101.atmos_rad_month.nc',
#                                      '00040101.atmos_rad_month.nc',
#                                      '00050101.atmos_rad_month.nc',
#                                      '00060101.atmos_rad_month.nc']
#                                  for v in rad_atmos},
#                    '3-hourly': {v: '{}.8xday.nc'.format(v) for v in []}}
# )

# asym_t15_fixed_h2o = Run(
#     name='asym_t15_fixed_h2o',
#     description=(
#         'Radiatively passive water vapor.'
#         ' 30 W m-2 asymmetry in solar forcing imposed in tropics.'
#     ),
#     data_in_direc=('/archive/Spencer.Clark/imr_skc/'
#                    'asym_t15_fixed_h2o/gfdl.ncrc3-default-repro/2/'
#                    'history'),
#     default_date_range=('0003-01-01', '0006-12-31'),
#     data_in_dir_struc='one_dir',
#     data_in_files={'monthly': {v: ['00010101.atmos_month.nc',
#                                    '00020101.atmos_month.nc',
#                                    '00030101.atmos_month.nc',
#                                    '00040101.atmos_month.nc',
#                                    '00050101.atmos_month.nc',
#                                    '00060101.atmos_month.nc']
#                                for v in v_atmos},
#                    'rad_month': {v: ['00010101.atmos_rad_month.nc',
#                                      '00020101.atmos_rad_month.nc',
#                                      '00030101.atmos_rad_month.nc',
#                                      '00040101.atmos_rad_month.nc',
#                                      '00050101.atmos_rad_month.nc',
#                                      '00060101.atmos_rad_month.nc']
#                                  for v in rad_atmos},
#                    '3-hourly': {v: '{}.8xday.nc'.format(v) for v in []}}
# )

# asym_e18_fixed_h2o = Run(
#     name='asym_e18_fixed_h2o',
#     description=(
#         'Radiatvely passive water vapor.'
#         ' 36 W m-2 asymmetry in solar forcing imposed in extratropics.'
#     ),
#     data_in_direc=('/archive/Spencer.Clark/imr_skc/'
#                    'asym_e18_fixed_h2o/gfdl.ncrc3-default-repro/'
#                    'ncrc3.default-repro/history'),
#     default_date_range=('0003-01-01', '0006-12-31'),
#     data_in_dir_struc='one_dir',
#     data_in_files={'monthly': {v: ['00010101.atmos_month.nc',
#                                    '00020101.atmos_month.nc',
#                                    '00030101.atmos_month.nc',
#                                    '00040101.atmos_month.nc',
#                                    '00050101.atmos_month.nc',
#                                    '00060101.atmos_month.nc']
#                                for v in v_atmos},
#                    'rad_month': {v: ['00010101.atmos_rad_month.nc',
#                                      '00020101.atmos_rad_month.nc',
#                                      '00030101.atmos_rad_month.nc',
#                                      '00040101.atmos_rad_month.nc',
#                                      '00050101.atmos_rad_month.nc',
#                                      '00060101.atmos_rad_month.nc']
#                                  for v in rad_atmos},
#                    '3-hourly': {v: '{}.8xday.nc'.format(v) for v in []}}
# )

# asym_t18_fixed_h2o = Run(
#     name='asym_t18_fixed_h2o',
#     description=(
#         'Radiatively passive water vapor.'
#         ' 36 W m-2 asymmetry in solar forcing imposed in tropics.'
#     ),
#     data_in_direc=('/archive/Spencer.Clark/imr_skc/'
#                    'asym_t18_fixed_h2o/gfdl.ncrc3-default-repro/'
#                    'ncrc3.default-repro/history'),
#     default_date_range=('0003-01-01', '0006-12-31'),
#     data_in_dir_struc='one_dir',
#     data_in_files={'monthly': {v: ['00010101.atmos_month.nc',
#                                    '00020101.atmos_month.nc',
#                                    '00030101.atmos_month.nc',
#                                    '00040101.atmos_month.nc',
#                                    '00050101.atmos_month.nc',
#                                    '00060101.atmos_month.nc']
#                                for v in v_atmos},
#                    'rad_month': {v: ['00010101.atmos_rad_month.nc',
#                                      '00020101.atmos_rad_month.nc',
#                                      '00030101.atmos_rad_month.nc',
#                                      '00040101.atmos_rad_month.nc',
#                                      '00050101.atmos_rad_month.nc',
#                                      '00060101.atmos_rad_month.nc']
#                                  for v in rad_atmos},
#                    '3-hourly': {v: '{}.8xday.nc'.format(v) for v in []}}
# )

# asym_e5_fixed_h2o = Run(
#     name='asym_e5_fixed_h2o',
#     description=(
#         'Radiatvely passive water vapor.'
#         ' 10 W m-2 asymmetry in solar forcing imposed in extratropics.'
#     ),
#     data_in_direc=('/archive/Spencer.Clark/imr_skc/'
#                    'asym_e5_fixed_h2o/gfdl.ncrc3-default-repro/'
#                    'ncrc3.default-repro/history'),
#     default_date_range=('0003-01-01', '0006-12-31'),
#     data_in_dir_struc='one_dir',
#     data_in_files={'monthly': {v: ['00010101.atmos_month.nc',
#                                    '00020101.atmos_month.nc',
#                                    '00030101.atmos_month.nc',
#                                    '00040101.atmos_month.nc',
#                                    '00050101.atmos_month.nc',
#                                    '00060101.atmos_month.nc']
#                                for v in v_atmos},
#                    'rad_month': {v: ['00010101.atmos_rad_month.nc',
#                                      '00020101.atmos_rad_month.nc',
#                                      '00030101.atmos_rad_month.nc',
#                                      '00040101.atmos_rad_month.nc',
#                                      '00050101.atmos_rad_month.nc',
#                                      '00060101.atmos_rad_month.nc']
#                                  for v in rad_atmos},
#                    '3-hourly': {v: '{}.8xday.nc'.format(v) for v in []}}
# )

# asym_t5_fixed_h2o = Run(
#     name='asym_t5_fixed_h2o',
#     description=(
#         'Radiatively passive water vapor.'
#         ' 10 W m-2 asymmetry in solar forcing imposed in tropics.'
#     ),
#     data_in_direc=('/archive/Spencer.Clark/imr_skc/'
#                    'asym_t5_fixed_h2o/gfdl.ncrc3-default-repro/'
#                    'ncrc3.default-repro/history'),
#     default_date_range=('0003-01-01', '0006-12-31'),
#     data_in_dir_struc='one_dir',
#     data_in_files={'monthly': {v: ['00010101.atmos_month.nc',
#                                    '00020101.atmos_month.nc',
#                                    '00030101.atmos_month.nc',
#                                    '00040101.atmos_month.nc',
#                                    '00050101.atmos_month.nc',
#                                    '00060101.atmos_month.nc']
#                                for v in v_atmos},
#                    'rad_month': {v: ['00010101.atmos_rad_month.nc',
#                                      '00020101.atmos_rad_month.nc',
#                                      '00030101.atmos_rad_month.nc',
#                                      '00040101.atmos_rad_month.nc',
#                                      '00050101.atmos_rad_month.nc',
#                                      '00060101.atmos_rad_month.nc']
#                                  for v in rad_atmos},
#                    '3-hourly': {v: '{}.8xday.nc'.format(v) for v in []}}
# )

# asym_e15_net_zero_solar = Run(
#     name='asym_e15_net_zero_solar',
#     description=(
#         'Net zero solar heating.'
#         ' 30 W m-2 asymmetry in solar forcing imposed in extratropics.'
#     ),
#     data_in_direc=('/archive/Spencer.Clark/imr_skc_net_zero_solar/'
#                    'asym_e15/gfdl.ncrc3-default-repro/'
#                    'history'),
#     default_date_range=('0003-01-01', '0006-12-31'),
#     data_in_dir_struc='one_dir',
#     data_in_files={'monthly': {v: ['00010101.atmos_month.nc',
#                                    '00020101.atmos_month.nc',
#                                    '00030101.atmos_month.nc',
#                                    '00040101.atmos_month.nc',
#                                    '00050101.atmos_month.nc',
#                                    '00060101.atmos_month.nc']
#                                for v in v_atmos},
#                    'rad_month': {v: ['00010101.atmos_rad_month.nc',
#                                      '00020101.atmos_rad_month.nc',
#                                      '00030101.atmos_rad_month.nc',
#                                      '00040101.atmos_rad_month.nc',
#                                      '00050101.atmos_rad_month.nc',
#                                      '00060101.atmos_rad_month.nc']
#                                  for v in rad_atmos},
#                    '3-hourly': {v: '{}.8xday.nc'.format(v) for v in []}}
# )

# asym_t15_net_zero_solar = Run(
#     name='asym_t15_net_zero_solar',
#     description=(
#         'Net zero solar heating.'
#         ' 30 W m-2 asymmetry in solar forcing imposed in tropics.'
#     ),
#     data_in_direc=('/archive/Spencer.Clark/imr_skc_net_zero_solar/'
#                    'asym_t15/gfdl.ncrc3-default-repro/'
#                    'history'),
#     default_date_range=('0003-01-01', '0006-12-31'),
#     data_in_dir_struc='one_dir',
#     data_in_files={'monthly': {v: ['00010101.atmos_month.nc',
#                                    '00020101.atmos_month.nc',
#                                    '00030101.atmos_month.nc',
#                                    '00040101.atmos_month.nc',
#                                    '00050101.atmos_month.nc',
#                                    '00060101.atmos_month.nc']
#                                for v in v_atmos},
#                    'rad_month': {v: ['00010101.atmos_rad_month.nc',
#                                      '00020101.atmos_rad_month.nc',
#                                      '00030101.atmos_rad_month.nc',
#                                      '00040101.atmos_rad_month.nc',
#                                      '00050101.atmos_rad_month.nc',
#                                      '00060101.atmos_rad_month.nc']
#                                  for v in rad_atmos},
#                    '3-hourly': {v: '{}.8xday.nc'.format(v) for v in []}}
# )

# eq_5 = Run(
#     name='eq_5',
#     description=(
#         'Fully coupled water vapor, dynamics, and radiation.'
#         ' 5 W m-2 global area average forcing imposed at the equator'
#     ),
#     data_in_direc=('/archive/Spencer.Clark/imr_skc_eq_forcing/'
#                    'eq_5/gfdl.ncrc3-default-repro/'
#                    'history'),
#     default_date_range=('0003-01-01', '0006-12-31'),
#     data_in_dir_struc='one_dir',
#     data_in_files={'monthly': {v: ['00010101.atmos_month.nc',
#                                    '00020101.atmos_month.nc',
#                                    '00030101.atmos_month.nc',
#                                    '00040101.atmos_month.nc',
#                                    '00050101.atmos_month.nc',
#                                    '00060101.atmos_month.nc']
#                                for v in v_atmos},
#                    'rad_month': {v: ['00010101.atmos_rad_month.nc',
#                                      '00020101.atmos_rad_month.nc',
#                                      '00030101.atmos_rad_month.nc',
#                                      '00040101.atmos_rad_month.nc',
#                                      '00050101.atmos_rad_month.nc',
#                                      '00060101.atmos_rad_month.nc']
#                                  for v in rad_atmos},
#                    '3-hourly': {v: '{}.8xday.nc'.format(v) for v in []}}
# )

# eq_6 = Run(
#     name='eq_6',
#     description=(
#         'Fully coupled water vapor, dynamics, and radiation.'
#         ' 6 W m-2 global area average forcing imposed at the equator'
#     ),
#     data_in_direc=('/archive/Spencer.Clark/imr_skc_eq_forcing/'
#                    'eq_6/gfdl.ncrc3-default-repro/'
#                    'history'),
#     default_date_range=('0003-01-01', '0006-12-31'),
#     data_in_dir_struc='one_dir',
#     data_in_files={'monthly': {v: ['00010101.atmos_month.nc',
#                                    '00020101.atmos_month.nc',
#                                    '00030101.atmos_month.nc',
#                                    '00040101.atmos_month.nc',
#                                    '00050101.atmos_month.nc',
#                                    '00060101.atmos_month.nc']
#                                for v in v_atmos},
#                    'rad_month': {v: ['00010101.atmos_rad_month.nc',
#                                      '00020101.atmos_rad_month.nc',
#                                      '00030101.atmos_rad_month.nc',
#                                      '00040101.atmos_rad_month.nc',
#                                      '00050101.atmos_rad_month.nc',
#                                      '00060101.atmos_rad_month.nc']
#                                  for v in rad_atmos},
#                    '3-hourly': {v: '{}.8xday.nc'.format(v) for v in []}}
# )

# eq_7 = Run(
#     name='eq_7',
#     description=(
#         'Fully coupled water vapor, dynamics, and radiation.'
#         ' 7 W m-2 global area average forcing imposed at the equator'
#     ),
#     data_in_direc=('/archive/Spencer.Clark/imr_skc_eq_forcing/'
#                    'eq_7/gfdl.ncrc3-default-repro/'
#                    'history'),
#     default_date_range=('0003-01-01', '0006-12-31'),
#     data_in_dir_struc='one_dir',
#     data_in_files={'monthly': {v: ['00010101.atmos_month.nc',
#                                    '00020101.atmos_month.nc',
#                                    '00030101.atmos_month.nc',
#                                    '00040101.atmos_month.nc',
#                                    '00050101.atmos_month.nc',
#                                    '00060101.atmos_month.nc']
#                                for v in v_atmos},
#                    'rad_month': {v: ['00010101.atmos_rad_month.nc',
#                                      '00020101.atmos_rad_month.nc',
#                                      '00030101.atmos_rad_month.nc',
#                                      '00040101.atmos_rad_month.nc',
#                                      '00050101.atmos_rad_month.nc',
#                                      '00060101.atmos_rad_month.nc']
#                                  for v in rad_atmos},
#                    '3-hourly': {v: '{}.8xday.nc'.format(v) for v in []}}
# )

# eq_8 = Run(
#     name='eq_8',
#     description=(
#         'Fully coupled water vapor, dynamics, and radiation.'
#         ' 8 W m-2 global area average forcing imposed at the equator'
#     ),
#     data_in_direc=('/archive/Spencer.Clark/imr_skc_eq_forcing/'
#                    'eq_8/gfdl.ncrc3-default-repro/'
#                    'history'),
#     default_date_range=('0003-01-01', '0006-12-31'),
#     data_in_dir_struc='one_dir',
#     data_in_files={'monthly': {v: ['00010101.atmos_month.nc',
#                                    '00020101.atmos_month.nc',
#                                    '00030101.atmos_month.nc',
#                                    '00040101.atmos_month.nc',
#                                    '00050101.atmos_month.nc',
#                                    '00060101.atmos_month.nc']
#                                for v in v_atmos},
#                    'rad_month': {v: ['00010101.atmos_rad_month.nc',
#                                      '00020101.atmos_rad_month.nc',
#                                      '00030101.atmos_rad_month.nc',
#                                      '00040101.atmos_rad_month.nc',
#                                      '00050101.atmos_rad_month.nc',
#                                      '00060101.atmos_rad_month.nc']
#                                  for v in rad_atmos},
#                    '3-hourly': {v: '{}.8xday.nc'.format(v) for v in []}}
# )

# eq_15 = Run(
#     name='eq_15',
#     description=(
#         'Fully coupled water vapor, dynamics, and radiation.'
#         ' 15 W m-2 global area average forcing imposed at the equator'
#     ),
#     data_in_direc=('/archive/Spencer.Clark/imr_skc_eq_forcing/'
#                    'eq_15/gfdl.ncrc3-default-repro/'
#                    'history'),
#     default_date_range=('0003-01-01', '0006-12-31'),
#     data_in_dir_struc='one_dir',
#     data_in_files={'monthly': {v: ['00010101.atmos_month.nc',
#                                    '00020101.atmos_month.nc',
#                                    '00030101.atmos_month.nc',
#                                    '00040101.atmos_month.nc',
#                                    '00050101.atmos_month.nc',
#                                    '00060101.atmos_month.nc']
#                                for v in v_atmos},
#                    'rad_month': {v: ['00010101.atmos_rad_month.nc',
#                                      '00020101.atmos_rad_month.nc',
#                                      '00030101.atmos_rad_month.nc',
#                                      '00040101.atmos_rad_month.nc',
#                                      '00050101.atmos_rad_month.nc',
#                                      '00060101.atmos_rad_month.nc']
#                                  for v in rad_atmos},
#                    '3-hourly': {v: '{}.8xday.nc'.format(v) for v in []}}
# )

# eq_25 = Run(
#     name='eq_25',
#     description=(
#         'Fully coupled water vapor, dynamics, and radiation.'
#         ' 25 W m-2 global area average forcing imposed at the equator'
#     ),
#     data_in_direc=('/archive/Spencer.Clark/imr_skc_eq_forcing/'
#                    'eq_25/gfdl.ncrc3-default-repro/'
#                    'history'),
#     default_date_range=('0003-01-01', '0006-12-31'),
#     data_in_dir_struc='one_dir',
#     data_in_files={'monthly': {v: ['00010101.atmos_month.nc',
#                                    '00020101.atmos_month.nc',
#                                    '00030101.atmos_month.nc',
#                                    '00040101.atmos_month.nc',
#                                    '00050101.atmos_month.nc',
#                                    '00060101.atmos_month.nc']
#                                for v in v_atmos},
#                    'rad_month': {v: ['00010101.atmos_rad_month.nc',
#                                      '00020101.atmos_rad_month.nc',
#                                      '00030101.atmos_rad_month.nc',
#                                      '00040101.atmos_rad_month.nc',
#                                      '00050101.atmos_rad_month.nc',
#                                      '00060101.atmos_rad_month.nc']
#                                  for v in rad_atmos},
#                    '3-hourly': {v: '{}.8xday.nc'.format(v) for v in []}}
# )

# eq_35 = Run(
#     name='eq_35',
#     description=(
#         'Fully coupled water vapor, dynamics, and radiation.'
#         ' 35 W m-2 global area average forcing imposed at the equator'
#     ),
#     data_in_direc=('/archive/Spencer.Clark/imr_skc_eq_forcing/'
#                    'eq_35/gfdl.ncrc3-default-repro/'
#                    'history'),
#     default_date_range=('0003-01-01', '0006-12-31'),
#     data_in_dir_struc='one_dir',
#     data_in_files={'monthly': {v: ['00010101.atmos_month.nc',
#                                    '00020101.atmos_month.nc',
#                                    '00030101.atmos_month.nc',
#                                    '00040101.atmos_month.nc',
#                                    '00050101.atmos_month.nc',
#                                    '00060101.atmos_month.nc']
#                                for v in v_atmos},
#                    'rad_month': {v: ['00010101.atmos_rad_month.nc',
#                                      '00020101.atmos_rad_month.nc',
#                                      '00030101.atmos_rad_month.nc',
#                                      '00040101.atmos_rad_month.nc',
#                                      '00050101.atmos_rad_month.nc',
#                                      '00060101.atmos_rad_month.nc']
#                                  for v in rad_atmos},
#                    '3-hourly': {v: '{}.8xday.nc'.format(v) for v in []}}
# )

# land_test = Run(
#     name='land_test',
#     description=(
#         'Testing the idealized moist full radiation model with crude land'
#     ),
#     data_in_direc=('/archive/Spencer.Clark/imr_skc_crude_land/'
#                    'control/gfdl.ncrc3-default-repro/1/'
#                    'history'),
#     default_date_range=('0003-01-01', '0006-12-31'),
#     data_in_dir_struc='one_dir',
#     data_in_files={'monthly': {v: ['00010101.atmos_month.nc',
#                                    '00020101.atmos_month.nc',
#                                    '00030101.atmos_month.nc',
#                                    '00040101.atmos_month.nc',
#                                    '00050101.atmos_month.nc',
#                                    '00060101.atmos_month.nc']
#                                for v in v_atmos},
#                    'rad_month': {v: ['00010101.atmos_rad_month.nc',
#                                      '00020101.atmos_rad_month.nc',
#                                      '00030101.atmos_rad_month.nc',
#                                      '00040101.atmos_rad_month.nc',
#                                      '00050101.atmos_rad_month.nc',
#                                      '00060101.atmos_rad_month.nc']
#                                  for v in rad_atmos},
#                    '3-hourly': {v: '{}.8xday.nc'.format(v) for v in []}}
# )

# earth_land = Run(
#     name='earth_land',
#     description=(
#         'Testing the idealized moist full radiation model with earth like'
#         'crude land'),
#     data_in_direc=('/archive/Spencer.Clark/imr_skc_crude_land/earth_land/'
#                    'gfdl.ncrc3-default-repro/history'
#                    ),
#     default_date_range=land_test.default_date_range,
#     data_in_dir_struc='one_dir',
#     data_in_files=land_test.data_in_files
# )

# earth_land_seasons = Run(
#     name='earth_land_seasons',
#     description=(
#         'Testing the idealized moist full radiation model with earth like'
#         'crude land.  Seasonal cycle added; 20 m mixed layer depth.'),
#     data_in_direc=('/archive/Spencer.Clark/imr_skc_crude_land/earth_land_seasons/'
#                    'gfdl.ncrc3-default-repro/history'
#                    ),
#     default_date_range=land_test.default_date_range,
#     data_in_dir_struc='one_dir',
#     data_in_files={'monthly': {v: ['%04d0101.atmos_month.nc' % y
#                                    for y in range(1, 21)]
#                                for v in v_atmos},
#                    'rad_month': {v: ['%04d0101.atmos_rad_month.nc' % y
#                                      for y in range(1, 21)]
#                                  for v in rad_atmos},
#                    '3-hourly': {v: '{}.8xday.nc'.format(v) for v in []}}
# )

# rect_seasons = Run(
#     name='rect_seasons',
#     description=(
#         'Testing the idealized moist full radiation model with rectangular'
#         'crude land.  Seasonal cycle added; 20 m mixed layer depth.'),
#     data_in_direc=('/archive/Spencer.Clark/imr_skc_crude_land/rect_seasons/'
#                    'gfdl.ncrc3-default-repro/4/history'
#                    ),
#     default_date_range=land_test.default_date_range,
#     data_in_dir_struc='one_dir',
#     data_in_files=land_test.data_in_files
# )

# earth_land_seasons_mld = Run(
#     name='earth_land_seasons_mld',
#     description=(
#         'Testing the idealized moist full radiation model with earth like'
#         'crude land.  Seasonal cycle added; 20 m mixed layer depth over'
#         ' ocean; 0.2 m depth over land'),
#     data_in_direc=('/archive/Spencer.Clark/imr_skc_crude_land_mld/'
#                    'earth_land_seasons/'
#                    'gfdl.ncrc3-default-repro/history'
#                    ),
#     default_date_range=land_test.default_date_range,
#     data_in_dir_struc='one_dir',
#     data_in_files=earth_land_seasons.data_in_files
# )

# umld_fr_earth_land = Run(
#     name='umld_fr_earth_land',
#     description=(
#         'Testing the idealized moist full radiation model with earth like'
#         'crude land.  Seasonal cycle added; 20 m mixed layer depth everywhere'
#     ),
#     data_in_direc=('/archive/Spencer.Clark/imr_skc_develop/'
#                    'umld_fr_earth_land/'
#                    'gfdl.ncrc3-default-repro/history'
#                    ),
#     default_date_range=land_test.default_date_range,
#     data_in_dir_struc='one_dir',
#     data_in_files=earth_land_seasons.data_in_files
# )

# umld_gr_earth_land = Run(
#     name='umld_gr_earth_land',
#     description=(
#         'Testing the idealized moist gray radiation model with earth like'
#         'crude land.  Seasonal cycle added; 20 m mixed layer depth everywhere'
#     ),
#     data_in_direc=('/archive/Spencer.Clark/imr_skc_develop/'
#                    'umld_gr_earth_land/'
#                    'gfdl.ncrc3-default-repro/history'
#                    ),
#     default_date_range=land_test.default_date_range,
#     data_in_dir_struc='one_dir',
#     data_in_files=earth_land_seasons.data_in_files
# )

# vmld_fr_earth_land = Run(
#     name='vmld_fr_earth_land',
#     description=(
#         'Testing the idealized moist full radiation model with earth like'
#         'crude land.  Seasonal cycle added; 20 m mixed layer depth everywhere;'
#         '0.2 m mixed layer depth over land'
#     ),
#     data_in_direc=('/archive/Spencer.Clark/imr_skc_develop/'
#                    'vmld_fr_earth_land/'
#                    'gfdl.ncrc3-default-repro/history'
#                    ),
#     default_date_range=land_test.default_date_range,
#     data_in_dir_struc='one_dir',
#     data_in_files=earth_land_seasons.data_in_files
# )

# vmld_gr_earth_land = Run(
#     name='vmld_gr_earth_land',
#     description=(
#         'Testing the idealized moist gray radiation model with earth like'
#         'crude land.  Seasonal cycle added; 20 m mixed layer depth everywhere;'
#         '0.2 m mixed layer depth over land'
#     ),
#     data_in_direc=('/archive/Spencer.Clark/imr_skc_develop/'
#                    'vmld_gr_earth_land/'
#                    'gfdl.ncrc3-default-repro/history'
#                    ),
#     default_date_range=land_test.default_date_range,
#     data_in_dir_struc='one_dir',
#     data_in_files=earth_land_seasons.data_in_files
# )

# umld_fr_earth_land_conv_off = Run(
#     name='umld_fr_earth_land_conv_off',
#     description=(
#         'Testing the idealized moist full radiation model with earth like'
#         'crude land.  Seasonal cycle added; 20 m mixed layer depth everywhere;'
#         'moist convection turned off.'
#     ),
#     data_in_direc=('/archive/Spencer.Clark/imr_skc_develop/'
#                    'umld_fr_earth_land_conv_off/'
#                    'gfdl.ncrc3-default-repro/history'
#                    ),
#     default_date_range=land_test.default_date_range,
#     data_in_dir_struc='one_dir',
#     data_in_files=earth_land_seasons.data_in_files
# )

# umld_gr_earth_land_conv_off = Run(
#     name='umld_gr_earth_land_conv_off',
#     description=(
#         'Testing the idealized moist gray radiation model with earth like'
#         'crude land.  Seasonal cycle added; 20 m mixed layer depth everywhere;'
#         'moist convection turned off.'
#     ),
#     data_in_direc=('/archive/Spencer.Clark/imr_skc_develop/'
#                    'umld_gr_earth_land_conv_off/'
#                    'gfdl.ncrc3-default-repro/history'
#                    ),
#     default_date_range=land_test.default_date_range,
#     data_in_dir_struc='one_dir',
#     data_in_files=earth_land_seasons.data_in_files
# )

# vmld_fr_earth_land_conv_off = Run(
#     name='vmld_fr_earth_land_conv_off',
#     description=(
#         'Testing the idealized moist full radiation model with earth like'
#         'crude land.  Seasonal cycle added; 20 m mixed layer depth everywhere;'
#         '0.2 m mixed layer depth over land; moist convection turned off.'
#     ),
#     data_in_direc=('/archive/Spencer.Clark/imr_skc_develop/'
#                    'vmld_fr_earth_land_conv_off/'
#                    'gfdl.ncrc3-default-repro/history'
#                    ),
#     default_date_range=land_test.default_date_range,
#     data_in_dir_struc='one_dir',
#     data_in_files=earth_land_seasons.data_in_files
# )

# vmld_gr_earth_land_conv_off = Run(
#     name='vmld_gr_earth_land_conv_off',
#     description=(
#         'Testing the idealized moist gray radiation model with earth like'
#         'crude land.  Seasonal cycle added; 20 m mixed layer depth everywhere;'
#         '0.2 m mixed layer depth over land; moist convection turned off.'
#     ),
#     data_in_direc=('/archive/Spencer.Clark/imr_skc_develop/'
#                    'vmld_gr_earth_land_conv_off/'
#                    'gfdl.ncrc3-default-repro/history'
#                    ),
#     default_date_range=land_test.default_date_range,
#     data_in_dir_struc='one_dir',
#     data_in_files=earth_land_seasons.data_in_files
# )

# asym_t15_fixed_h2o_tropics = Run(
#     name='asym_t15_fixed_h2o_tropics',
#     description=(
#         'Radiatively passive water vapor.'
#         ' 30 W m-2 asymmetry in solar forcing imposed in tropics.'
#         ' Fixed water in 20S to 20N'
#     ),
#     data_in_direc=('/archive/Spencer.Clark/imr_skc_develop/'
#                    'asym_t15_fixed_h2o_tropics/gfdl.ncrc3-default-repro/'
#                    'history'),
#     default_date_range=('0003-01-01', '0006-12-31'),
#     data_in_dir_struc='one_dir',
#     data_in_files={'monthly': {v: ['00010101.atmos_month.nc',
#                                    '00020101.atmos_month.nc',
#                                    '00030101.atmos_month.nc',
#                                    '00040101.atmos_month.nc',
#                                    '00050101.atmos_month.nc',
#                                    '00060101.atmos_month.nc']
#                                for v in v_atmos},
#                    'rad_month': {v: ['00010101.atmos_rad_month.nc',
#                                      '00020101.atmos_rad_month.nc',
#                                      '00030101.atmos_rad_month.nc',
#                                      '00040101.atmos_rad_month.nc',
#                                      '00050101.atmos_rad_month.nc',
#                                      '00060101.atmos_rad_month.nc']
#                                  for v in rad_atmos},
#                    '3-hourly': {v: '{}.8xday.nc'.format(v) for v in []}}
# )

# asym_e15_fixed_h2o_tropics = Run(
#     name='asym_e15_fixed_h2o_tropics',
#     description=(
#         'Radiatively passive water vapor.'
#         ' 30 W m-2 asymmetry in solar forcing imposed in extratropics.'
#         ' Fixed water in 20S to 20N'
#     ),
#     data_in_direc=('/archive/Spencer.Clark/imr_skc_develop/'
#                    'asym_e15_fixed_h2o_tropics/gfdl.ncrc3-default-repro/'
#                    'history'),
#     default_date_range=('0003-01-01', '0006-12-31'),
#     data_in_dir_struc='one_dir',
#     data_in_files={'monthly': {v: ['00010101.atmos_month.nc',
#                                    '00020101.atmos_month.nc',
#                                    '00030101.atmos_month.nc',
#                                    '00040101.atmos_month.nc',
#                                    '00050101.atmos_month.nc',
#                                    '00060101.atmos_month.nc']
#                                for v in v_atmos},
#                    'rad_month': {v: ['00010101.atmos_rad_month.nc',
#                                      '00020101.atmos_rad_month.nc',
#                                      '00030101.atmos_rad_month.nc',
#                                      '00040101.atmos_rad_month.nc',
#                                      '00050101.atmos_rad_month.nc',
#                                      '00060101.atmos_rad_month.nc']
#                                  for v in rad_atmos},
#                    '3-hourly': {v: '{}.8xday.nc'.format(v) for v in []}}
# )

# asym_t15_fixed_h2o_extratropics = Run(
#     name='asym_t15_fixed_h2o_extratropics',
#     description=(
#         'Radiatively passive water vapor.'
#         ' 30 W m-2 asymmetry in solar forcing imposed in tropics.'
#         ' Fixed water outside 20S to 20N'
#     ),
#     data_in_direc=('/archive/Spencer.Clark/imr_skc_develop/'
#                    'asym_t15_fixed_h2o_extratropics/gfdl.ncrc3-default-repro/'
#                    'history'),
#     default_date_range=('0003-01-01', '0006-12-31'),
#     data_in_dir_struc='one_dir',
#     data_in_files={'monthly': {v: ['00010101.atmos_month.nc',
#                                    '00020101.atmos_month.nc',
#                                    '00030101.atmos_month.nc',
#                                    '00040101.atmos_month.nc',
#                                    '00050101.atmos_month.nc',
#                                    '00060101.atmos_month.nc']
#                                for v in v_atmos},
#                    'rad_month': {v: ['00010101.atmos_rad_month.nc',
#                                      '00020101.atmos_rad_month.nc',
#                                      '00030101.atmos_rad_month.nc',
#                                      '00040101.atmos_rad_month.nc',
#                                      '00050101.atmos_rad_month.nc',
#                                      '00060101.atmos_rad_month.nc']
#                                  for v in rad_atmos},
#                    '3-hourly': {v: '{}.8xday.nc'.format(v) for v in []}}
# )

# asym_e15_fixed_h2o_extratropics = Run(
#     name='asym_e15_fixed_h2o_extratropics',
#     description=(
#         'Radiatively passive water vapor.'
#         ' 30 W m-2 asymmetry in solar forcing imposed in extratropics.'
#         ' Fixed water outside 20S to 20N'
#     ),
#     data_in_direc=('/archive/Spencer.Clark/imr_skc_develop/'
#                    'asym_e15_fixed_h2o_extratropics/gfdl.ncrc3-default-repro/'
#                    'history'),
#     default_date_range=('0003-01-01', '0006-12-31'),
#     data_in_dir_struc='one_dir',
#     data_in_files={'monthly': {v: ['00010101.atmos_month.nc',
#                                    '00020101.atmos_month.nc',
#                                    '00030101.atmos_month.nc',
#                                    '00040101.atmos_month.nc',
#                                    '00050101.atmos_month.nc',
#                                    '00060101.atmos_month.nc']
#                                for v in v_atmos},
#                    'rad_month': {v: ['00010101.atmos_rad_month.nc',
#                                      '00020101.atmos_rad_month.nc',
#                                      '00030101.atmos_rad_month.nc',
#                                      '00040101.atmos_rad_month.nc',
#                                      '00050101.atmos_rad_month.nc',
#                                      '00060101.atmos_rad_month.nc']
#                                  for v in rad_atmos},
#                    '3-hourly': {v: '{}.8xday.nc'.format(v) for v in []}}
# )

# zero_o3 = Run(
#     name='zero_o3',
#     description=(
#         'Control simulation of idealized moist run with realistic'
#         'radiative transfer with zero ozone.'
#     ),
#     data_in_direc=('/archive/Spencer.Clark/imr_skc_develop/'
#                    'zero_o3/gfdl.ncrc3-default-repro/'
#                    'history'),
#     default_date_range=('0003-01-01', '0006-12-31'),
#     data_in_dir_struc='one_dir',
#     data_in_files={'monthly': {v: ['00010101.atmos_month.nc',
#                                    '00020101.atmos_month.nc',
#                                    '00030101.atmos_month.nc',
#                                    '00040101.atmos_month.nc',
#                                    '00050101.atmos_month.nc',
#                                    '00060101.atmos_month.nc']
#                                for v in v_atmos},
#                    'rad_month': {v: ['00010101.atmos_rad_month.nc',
#                                      '00020101.atmos_rad_month.nc',
#                                      '00030101.atmos_rad_month.nc',
#                                      '00040101.atmos_rad_month.nc',
#                                      '00050101.atmos_rad_month.nc',
#                                      '00060101.atmos_rad_month.nc']
#                                  for v in rad_atmos},
#                    '3-hourly': {v: ['000{}0101.atmos_8xday.{}.nc'.format(y, v)
#                                     for y in range(6, 7)]
#                                 for v in three_hourly}}  # SKC: for now just do one year.
# )

# anti_t15 = Run(
#     name='anti_t15',
#     description=(
#         'Antisymmetric gaussian solar forcing. Asymmetry equivalent to'
#         ' asym_*15 cases.'
#     ),
#     data_in_direc=('/archive/Spencer.Clark/imr_skc_develop/'
#                    'anti_t15/gfdl.ncrc3-default-repro/'
#                    'history'),
#     default_date_range=('0003-01-01', '0006-12-31'),
#     data_in_dir_struc='one_dir',
#     data_in_files={'monthly': {v: ['00010101.atmos_month.nc',
#                                    '00020101.atmos_month.nc',
#                                    '00030101.atmos_month.nc',
#                                    '00040101.atmos_month.nc',
#                                    '00050101.atmos_month.nc',
#                                    '00060101.atmos_month.nc']
#                                for v in v_atmos},
#                    'rad_month': {v: ['00010101.atmos_rad_month.nc',
#                                      '00020101.atmos_rad_month.nc',
#                                      '00030101.atmos_rad_month.nc',
#                                      '00040101.atmos_rad_month.nc',
#                                      '00050101.atmos_rad_month.nc',
#                                      '00060101.atmos_rad_month.nc']
#                                  for v in rad_atmos},
#                    '3-hourly': {v: ['000{}0101.atmos_8xday.{}.nc'.format(y, v)
#                                     for y in range(6, 7)]
#                                 for v in three_hourly}}  # SKC: for now just do one year.
# )

# anti_e15 = Run(
#     name='anti_e15',
#     description=(
#         'Antisymmetric gaussian solar forcing. Asymmetry equivalent to'
#         ' asym_*15 cases.'
#     ),
#     data_in_direc=('/archive/Spencer.Clark/imr_skc_develop/'
#                    'anti_e15/gfdl.ncrc3-default-repro/'
#                    'history'),
#     default_date_range=('0003-01-01', '0006-12-31'),
#     data_in_dir_struc='one_dir',
#     data_in_files={'monthly': {v: ['00010101.atmos_month.nc',
#                                    '00020101.atmos_month.nc',
#                                    '00030101.atmos_month.nc',
#                                    '00040101.atmos_month.nc',
#                                    '00050101.atmos_month.nc',
#                                    '00060101.atmos_month.nc']
#                                for v in v_atmos},
#                    'rad_month': {v: ['00010101.atmos_rad_month.nc',
#                                      '00020101.atmos_rad_month.nc',
#                                      '00030101.atmos_rad_month.nc',
#                                      '00040101.atmos_rad_month.nc',
#                                      '00050101.atmos_rad_month.nc',
#                                      '00060101.atmos_rad_month.nc']
#                                  for v in rad_atmos},
#                    '3-hourly': {v: ['000{}0101.atmos_8xday.{}.nc'.format(y, v)
#                                     for y in range(6, 7)]
#                                 for v in three_hourly}}  # SKC: for now just do one year.
# )

# anti_t15_fixed_h2o = Run(
#     name='anti_t15_fixed_h2o',
#     description=(
#         'Antisymmetric gaussian solar forcing. Asymmetry equivalent to'
#         ' asym_*15 cases.'
#     ),
#     data_in_direc=('/archive/Spencer.Clark/imr_skc_develop/'
#                    'anti_t15_fixed_h2o/gfdl.ncrc3-default-repro/'
#                    'history'),
#     default_date_range=('0003-01-01', '0006-12-31'),
#     data_in_dir_struc='one_dir',
#     data_in_files={'monthly': {v: ['00010101.atmos_month.nc',
#                                    '00020101.atmos_month.nc',
#                                    '00030101.atmos_month.nc',
#                                    '00040101.atmos_month.nc',
#                                    '00050101.atmos_month.nc',
#                                    '00060101.atmos_month.nc']
#                                for v in v_atmos},
#                    'rad_month': {v: ['00010101.atmos_rad_month.nc',
#                                      '00020101.atmos_rad_month.nc',
#                                      '00030101.atmos_rad_month.nc',
#                                      '00040101.atmos_rad_month.nc',
#                                      '00050101.atmos_rad_month.nc',
#                                      '00060101.atmos_rad_month.nc']
#                                  for v in rad_atmos},
#                    '3-hourly': {v: ['000{}0101.atmos_8xday.{}.nc'.format(y, v)
#                                     for y in range(6, 7)]
#                                 for v in three_hourly}}  # SKC: for now just do one year.
# )

# anti_e15_fixed_h2o = Run(
#     name='anti_e15_fixed_h2o',
#     description=(
#         'Antisymmetric gaussian solar forcing. Asymmetry equivalent to'
#         ' asym_*15 cases.'
#     ),
#     data_in_direc=('/archive/Spencer.Clark/imr_skc_develop/'
#                    'anti_e15_fixed_h2o/gfdl.ncrc3-default-repro/'
#                    'history'),
#     default_date_range=('0003-01-01', '0006-12-31'),
#     data_in_dir_struc='one_dir',
#     data_in_files={'monthly': {v: ['00010101.atmos_month.nc',
#                                    '00020101.atmos_month.nc',
#                                    '00030101.atmos_month.nc',
#                                    '00040101.atmos_month.nc',
#                                    '00050101.atmos_month.nc',
#                                    '00060101.atmos_month.nc']
#                                for v in v_atmos},
#                    'rad_month': {v: ['00010101.atmos_rad_month.nc',
#                                      '00020101.atmos_rad_month.nc',
#                                      '00030101.atmos_rad_month.nc',
#                                      '00040101.atmos_rad_month.nc',
#                                      '00050101.atmos_rad_month.nc',
#                                      '00060101.atmos_rad_month.nc']
#                                  for v in rad_atmos},
#                    '3-hourly': {v: ['000{}0101.atmos_8xday.{}.nc'.format(y, v)
#                                     for y in range(6, 7)]
#                                 for v in three_hourly}}  # SKC: for now just do one year.
# )

# anti_t15_fixed_h2o_tropics = Run(
#     name='anti_t15_fixed_h2o_tropics',
#     description=(
#         'Antisymmetric gaussian solar forcing. Asymmetry equivalent to'
#         ' asym_*15 cases.'
#     ),
#     data_in_direc=('/archive/Spencer.Clark/imr_skc_develop/'
#                    'anti_t15_fixed_h2o_tropics/gfdl.ncrc3-default-repro/'
#                    'history'),
#     default_date_range=('0003-01-01', '0006-12-31'),
#     data_in_dir_struc='one_dir',
#     data_in_files={'monthly': {v: ['00010101.atmos_month.nc',
#                                    '00020101.atmos_month.nc',
#                                    '00030101.atmos_month.nc',
#                                    '00040101.atmos_month.nc',
#                                    '00050101.atmos_month.nc',
#                                    '00060101.atmos_month.nc']
#                                for v in v_atmos},
#                    'rad_month': {v: ['00010101.atmos_rad_month.nc',
#                                      '00020101.atmos_rad_month.nc',
#                                      '00030101.atmos_rad_month.nc',
#                                      '00040101.atmos_rad_month.nc',
#                                      '00050101.atmos_rad_month.nc',
#                                      '00060101.atmos_rad_month.nc']
#                                  for v in rad_atmos},
#                    '3-hourly': {v: ['000{}0101.atmos_8xday.{}.nc'.format(y, v)
#                                     for y in range(6, 7)]
#                                 for v in three_hourly}}  # SKC: for now just do one year.
# )

# anti_e15_fixed_h2o_tropics = Run(
#     name='anti_e15_fixed_h2o_tropics',
#     description=(
#         'Antisymmetric gaussian solar forcing. Asymmetry equivalent to'
#         ' asym_*15 cases.'
#     ),
#     data_in_direc=('/archive/Spencer.Clark/imr_skc_develop/'
#                    'anti_e15_fixed_h2o_tropics/gfdl.ncrc3-default-repro/'
#                    'history'),
#     default_date_range=('0003-01-01', '0006-12-31'),
#     data_in_dir_struc='one_dir',
#     data_in_files={'monthly': {v: ['00010101.atmos_month.nc',
#                                    '00020101.atmos_month.nc',
#                                    '00030101.atmos_month.nc',
#                                    '00040101.atmos_month.nc',
#                                    '00050101.atmos_month.nc',
#                                    '00060101.atmos_month.nc']
#                                for v in v_atmos},
#                    'rad_month': {v: ['00010101.atmos_rad_month.nc',
#                                      '00020101.atmos_rad_month.nc',
#                                      '00030101.atmos_rad_month.nc',
#                                      '00040101.atmos_rad_month.nc',
#                                      '00050101.atmos_rad_month.nc',
#                                      '00060101.atmos_rad_month.nc']
#                                  for v in rad_atmos},
#                    '3-hourly': {v: ['000{}0101.atmos_8xday.{}.nc'.format(y, v)
#                                     for y in range(6, 7)]
#                                 for v in three_hourly}}  # SKC: for now just do one year.
# )

# anti_t15_fixed_h2o_extratropics = Run(
#     name='anti_t15_fixed_h2o_extratropics',
#     description=(
#         'Antisymmetric gaussian solar forcing. Asymmetry equivalent to'
#         ' asym_*15 cases.'
#     ),
#     data_in_direc=('/archive/Spencer.Clark/imr_skc_develop/'
#                    'anti_t15_fixed_h2o_extratropics/gfdl.ncrc3-default-repro/'
#                    'history'),
#     default_date_range=('0003-01-01', '0006-12-31'),
#     data_in_dir_struc='one_dir',
#     data_in_files={'monthly': {v: ['00010101.atmos_month.nc',
#                                    '00020101.atmos_month.nc',
#                                    '00030101.atmos_month.nc',
#                                    '00040101.atmos_month.nc',
#                                    '00050101.atmos_month.nc',
#                                    '00060101.atmos_month.nc']
#                                for v in v_atmos},
#                    'rad_month': {v: ['00010101.atmos_rad_month.nc',
#                                      '00020101.atmos_rad_month.nc',
#                                      '00030101.atmos_rad_month.nc',
#                                      '00040101.atmos_rad_month.nc',
#                                      '00050101.atmos_rad_month.nc',
#                                      '00060101.atmos_rad_month.nc']
#                                  for v in rad_atmos},
#                    '3-hourly': {v: ['000{}0101.atmos_8xday.{}.nc'.format(y, v)
#                                     for y in range(6, 7)]
#                                 for v in three_hourly}}  # SKC: for now just do one year.
# )

# anti_e15_fixed_h2o_extratropics = Run(
#     name='anti_e15_fixed_h2o_extratropics',
#     description=(
#         'Antisymmetric gaussian solar forcing. Asymmetry equivalent to'
#         ' asym_*15 cases.'
#     ),
#     data_in_direc=('/archive/Spencer.Clark/imr_skc_develop/'
#                    'anti_e15_fixed_h2o_extratropics/gfdl.ncrc3-default-repro/'
#                    'history'),
#     default_date_range=('0003-01-01', '0006-12-31'),
#     data_in_dir_struc='one_dir',
#     data_in_files={'monthly': {v: ['00010101.atmos_month.nc',
#                                    '00020101.atmos_month.nc',
#                                    '00030101.atmos_month.nc',
#                                    '00040101.atmos_month.nc',
#                                    '00050101.atmos_month.nc',
#                                    '00060101.atmos_month.nc']
#                                for v in v_atmos},
#                    'rad_month': {v: ['00010101.atmos_rad_month.nc',
#                                      '00020101.atmos_rad_month.nc',
#                                      '00030101.atmos_rad_month.nc',
#                                      '00040101.atmos_rad_month.nc',
#                                      '00050101.atmos_rad_month.nc',
#                                      '00060101.atmos_rad_month.nc']
#                                  for v in rad_atmos},
#                    '3-hourly': {v: ['000{}0101.atmos_8xday.{}.nc'.format(y, v)
#                                     for y in range(6, 7)]
#                                 for v in three_hourly}}  # SKC: for now just do one year.
# )

# control_gray = Run(
#     name='control_gray',
#     description=(
#         'Case with symmetric solar insolation and a gray atmosphere.'
#     ),
#     data_in_direc=('/archive/Spencer.Clark/imr_skc_develop/'
#                    'control_gray/gfdl.ncrc3-default-repro/'
#                    'history'),
#     default_date_range=('0003-01-01', '0006-12-31'),
#     data_in_dir_struc='one_dir',
#     data_in_files={'monthly': {v: ['00010101.atmos_month.nc',
#                                    '00020101.atmos_month.nc',
#                                    '00030101.atmos_month.nc',
#                                    '00040101.atmos_month.nc',
#                                    '00050101.atmos_month.nc',
#                                    '00060101.atmos_month.nc']
#                                for v in v_atmos}
#                    }
# )

# control_gray_solar = Run(
#     name='control_gray_solar',
#     description=(
#         'Case with symmetric solar insolation and a gray atmosphere.'
#         ' Includes a parameterization of absorption of shortwave radiation.'
#         ' The absorption parameter is set to 0.2 and the solar exponent is 4.0'
#     ),
#     data_in_direc=('/archive/Spencer.Clark/imr_skc_develop/'
#                    'control_gray_solar/gfdl.ncrc3-default-repro/2/'
#                    'history'),
#     default_date_range=('0003-01-01', '0006-12-31'),
#     data_in_dir_struc='one_dir',
#     data_in_files={'monthly': {v: ['00010101.atmos_month.nc',
#                                    '00020101.atmos_month.nc',
#                                    '00030101.atmos_month.nc',
#                                    '00040101.atmos_month.nc',
#                                    '00050101.atmos_month.nc',
#                                    '00060101.atmos_month.nc']
#                                for v in v_atmos}
#                    }
# )
