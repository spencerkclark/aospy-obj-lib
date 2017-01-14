# from aospy import Run
# # import numpy as np
# # import pandas as pd
# from datetime import datetime, timedelta

# # S. Clark 10-30-2015: Contrary to what idealized model runs suggest,
# # we start at year 1 NOT 0.
# # Also note that it throws things into a 365 day no-leap calendar.
# # So if you want the last 360 days you need to be smarter about things.

# varia = ['olr', 'temp', 'sphum', 'ps', 'vcomp', 'swdn_sfc', 'olr', 'lwdn_sfc',
#          'lwup_sfc', 'flux_t', 'flux_lhe',
#          'convection_rain', 'condensation_rain',
#          'ucomp', 'omega', 'umse', 'vmse', 'omega_mse', 'mse', 'umse_vint',
#          'vmse_vint', 'omega_mse_vint', 'swdn_toa', 't_surf', 'tdt_rad',
#          'height']

# # If we run more than four years we'll have to think about leap years,
# # but for now this is OK.
# model_start = datetime(1, 1, 1)
# length = timedelta(days=720)
# end = model_start + length
# analysis_length = timedelta(days=360)
# a_start = str(end - analysis_length)
# a_end = str(end)

# control_T85 = Run(
#     name='control_T85',
#     description=(
#         'A test case for using aospy + an idealized simulation.'
#     ),
#     data_in_direc='/archive/skc/idealized_moist_T85/control_T85/'
#                   'gfdl.ncrc2-default-prod/1x0m720d_32pe/history',
#     default_date_range=(a_start, a_end),
#     data_in_dir_struc='one_dir',
#     data_in_files={'20-day': {v: '00000.1x20days.nc' for v in varia},
#                    'daily': {v: '00000.1xday.nc' for v in varia},
#                    '6-hourly': {v: '00000.4xday.nc' for v in varia}},
#     idealized=False
# )

# extratropics_15_T85 = Run(
#     name='extratropics_0.15_T85',
#     description=(
#         'Solar absorption decreased by 15% from 30N to 90N'
#     ),
#     data_in_direc='/archive/skc/idealized_moist_alb_T85/extratropics_0.15_T85/'
#                   'gfdl.ncrc2-default-prod/1x0m720d_32pe/history',
#     default_date_range=(a_start, a_end),
#     data_in_dir_struc='one_dir',
#     data_in_files={'20-day': {v: '00000.1x20days.nc' for v in varia},
#                    'daily': {v: '00000.1xday.nc' for v in varia},
#                    '6-hourly': {v: '00000.4xday.nc' for v in varia}},
#     idealized=False
# )

# extratropics_037_T85 = Run(
#     name='extratropics_0.037_T85',
#     description=(
#         'Solar absorption decreased by 3.7% from 30N to 90N'
#     ),
#     data_in_direc='/archive/skc/idealized_moist_alb_T85/extratropics_0.037_T85'
#                   '/gfdl.ncrc2-default-prod/1x0m720d_32pe/history',
#     default_date_range=(a_start, a_end),
#     data_in_dir_struc='one_dir',
#     data_in_files={'20-day': {v: '00000.1x20days.nc' for v in varia},
#                    'daily': {v: '00000.1xday.nc' for v in varia},
#                    '6-hourly': {v: '00000.4xday.nc' for v in varia}},
#     idealized=False
# )

# tropics_10_T85 = Run(
#     name='tropics_0.1_T85',
#     description=(
#         'Solar absorption decreased by 10% from EQ to 30N'
#     ),
#     data_in_direc='/archive/skc/idealized_moist_alb_T85/tropics_0.1_T85/'
#                   'gfdl.ncrc2-default-prod/1x0m720d_32pe/history',
#     default_date_range=(a_start, a_end),
#     data_in_dir_struc='one_dir',
#     data_in_files={'20-day': {v: '00000.1x20days.nc' for v in varia},
#                    'daily': {v: '00000.1xday.nc' for v in varia},
#                    '6-hourly': {v: '00000.4xday.nc' for v in varia}},
#     idealized=False
# )

# tropics_025_T85 = Run(
#     name='tropics_0.025_T85',
#     description=(
#         'Solar absorption decreased by 2.5% from EQ to 30N'
#     ),
#     data_in_direc='/archive/skc/idealized_moist_alb_T85/tropics_0.025_T85/'
#                   'gfdl.ncrc2-default-prod/1x0m720d_32pe/history',
#     default_date_range=(a_start, a_end),
#     data_in_dir_struc='one_dir',
#     data_in_files={'20-day': {v: '00000.1x20days.nc' for v in varia},
#                    'daily': {v: '00000.1xday.nc' for v in varia},
#                    '6-hourly': {v: '00000.4xday.nc' for v in varia}},
#     idealized=False
# )

# control_alb_T42 = Run(
#     name='control_alb_T42',
#     description=(
#         'Control case at T42 spectral resolution'
#     ),
#     data_in_direc='/archive/skc/idealized_moist_alb_T42/control_alb_T42/'
#                   'gfdl.ncrc2-default-prod/1x0m720d_32pe/history',
#     default_date_range=(a_start, a_end),
#     data_in_dir_struc='one_dir',
#     data_in_files={'20-day': {v: '00000.1x20days.nc' for v in varia},
#                    'daily': {v: '00000.1xday.nc' for v in varia},
#                    '3-hourly': {v: '{}.8xday.nc'.format(v) for v in varia}},
#     idealized=False
# )

# control_gaussian_T42 = Run(
#     name='control_gaussian_T42',
#     description=(
#         'Control case at T42 spectral resolution'
#     ),
#     data_in_direc='/archive/skc/idealized_moist_alb_T42/control_gaussian_T42/'
#                   'gfdl.ncrc2-default-prod/1x0m720d_32pe1/history',
#     default_date_range=(a_start, a_end),
#     data_in_dir_struc='one_dir',
#     data_in_files={'20-day': {v: '00000.1x20days.nc' for v in varia},
#                    '3-hourly': {v: '{}.8xday.nc'.format(v) for v in varia}},
#     idealized=False
# )

# tropics_gaussian_5_T42 = Run(
#     name='tropics_gaussian_5.0_T42',
#     description=(
#         'Tropical case with Gaussian forcing at T42 spectral resolution'
#         ' Forcing is asymmetric, with global average magnitude of -5.0 W m^-2'
#     ),
#     data_in_direc='/archive/skc/idealized_moist_alb_T42/'
#                   'tropics_gaussian_5.0_T42/'
#                   'gfdl.ncrc2-default-prod/1x0m720d_32pe/history',
#     default_date_range=(a_start, a_end),
#     data_in_dir_struc='one_dir',
#     data_in_files={'20-day': {v: '00000.1x20days.nc' for v in varia},
#                    '3-hourly': {v: '{}.8xday.nc'.format(v) for v in varia}},
#     idealized=False
# )

# extratropics_gaussian_5_T42 = Run(
#     name='extratropics_gaussian_5.0_T42',
#     description=(
#         'Extratropical case with Gaussian forcing at T42 spectral resolution'
#         ' Forcing is asymmetric, with global average magnitude of -5.0 W m^-2'
#     ),
#     data_in_direc='/archive/skc/idealized_moist_alb_T42/'
#                   'extratropics_gaussian_5.0_T42/'
#                   'gfdl.ncrc2-default-prod/1x0m720d_32pe/history',
#     default_date_range=(a_start, a_end),
#     data_in_dir_struc='one_dir',
#     data_in_files={'20-day': {v: '00000.1x20days.nc' for v in varia},
#                    '3-hourly': {v: '{}.8xday.nc'.format(v) for v in varia}},
#     idealized=False
# )

# tropics_gaussian_25_T42 = Run(
#     name='tropics_gaussian_25.0_T42',
#     description=(
#         'Tropical case with Gaussian forcing at T42 spectral resolution'
#         ' Forcing is asymmetric, with global average magnitude of -25.0 W m^-2'
#     ),
#     data_in_direc='/archive/skc/idealized_moist_alb_T42/'
#                   'tropics_gaussian_25.0_T42/'
#                   'gfdl.ncrc2-default-prod/1x0m720d_32pe/history',
#     default_date_range=(a_start, a_end),
#     data_in_dir_struc='one_dir',
#     data_in_files={'20-day': {v: '00000.1x20days.nc' for v in varia},
#                    '3-hourly': {v: '{}.8xday.nc'.format(v) for v in varia}},
#     idealized=False
# )

# extratropics_gaussian_25_T42 = Run(
#     name='extratropics_gaussian_25.0_T42',
#     description=(
#         'Extratropical case with Gaussian forcing at T42 spectral resolution'
#         ' Forcing is asymmetric, with global average magnitude of -25.0 W m^-2'
#     ),
#     data_in_direc='/archive/skc/idealized_moist_alb_T42/'
#                   'extratropics_gaussian_25.0_T42/'
#                   'gfdl.ncrc2-default-prod/1x0m720d_32pe/history',
#     default_date_range=(a_start, a_end),
#     data_in_dir_struc='one_dir',
#     data_in_files={'20-day': {v: '00000.1x20days.nc' for v in varia},
#                    '3-hourly': {v: '{}.8xday.nc'.format(v) for v in varia}},
#     idealized=False
# )

# tropics_gaussian_15_T42 = Run(
#     name='tropics_gaussian_15.0_T42',
#     description=(
#         'Tropical case with Gaussian forcing at T42 spectral resolution'
#         ' Forcing is asymmetric, with global average magnitude of -15.0 W m^-2'
#     ),
#     data_in_direc='/archive/skc/idealized_moist_alb_T42/'
#                   'tropics_gaussian_15.0_T42/'
#                   'gfdl.ncrc2-default-prod/1x0m720d_32pe/history',
#     default_date_range=(a_start, a_end),
#     data_in_dir_struc='one_dir',
#     data_in_files={'20-day': {v: '00000.1x20days.nc' for v in varia},
#                    '3-hourly': {v: '{}.8xday.nc'.format(v) for v in varia}},
#     idealized=False
# )

# extratropics_gaussian_15_T42 = Run(
#     name='extratropics_gaussian_15.0_T42',
#     description=(
#         'Extratropical case with Gaussian forcing at T42 spectral resolution'
#         ' Forcing is asymmetric, with global average magnitude of -15.0 W m^-2'
#     ),
#     data_in_direc='/archive/skc/idealized_moist_alb_T42/'
#                   'extratropics_gaussian_15.0_T42/'
#                   'gfdl.ncrc2-default-prod/1x0m720d_32pe/history',
#     default_date_range=(a_start, a_end),
#     data_in_dir_struc='one_dir',
#     data_in_files={'20-day': {v: '00000.1x20days.nc' for v in varia},
#                    '3-hourly': {v: '{}.8xday.nc'.format(v) for v in varia}},
#     idealized=False
# )

# legendre_1 = Run(
#     name='legendre_1',
#     description=(
#         'Case with gamma set to 0.1'
#     ),
#     data_in_direc='/archive/skc/idealized_moist_legendre/'
#                   'legendre_0.1/'
#                   'gfdl.ncrc2-default-prod/1x0m720d_32pe/history',
#     default_date_range=(a_start, a_end),
#     data_in_dir_struc='one_dir',
#     data_in_files={'20-day': {v: '00000.1x20days.nc' for v in varia},
#                    '3-hourly': {v: '{}.8xday.nc'.format(v) for v in varia}},
#     idealized=False
# )

# legendre_2 = Run(
#     name='legendre_2',
#     description=(
#         'Case with gamma set to 0.2'
#     ),
#     data_in_direc='/archive/skc/idealized_moist_legendre/'
#                   'legendre_0.2/'
#                   'gfdl.ncrc2-default-prod/1x0m720d_32pe/history',
#     default_date_range=(a_start, a_end),
#     data_in_dir_struc='one_dir',
#     data_in_files={'20-day': {v: '00000.1x20days.nc' for v in varia},
#                    '3-hourly': {v: '{}.8xday.nc'.format(v) for v in varia}},
#     idealized=False
# )

# legendre_3 = Run(
#     name='legendre_3',
#     description=(
#         'Case with gamma set to 0.3'
#     ),
#     data_in_direc='/archive/skc/idealized_moist_legendre/'
#                   'legendre_0.3/'
#                   'gfdl.ncrc2-default-prod/1x0m720d_32pe/history',
#     default_date_range=(a_start, a_end),
#     data_in_dir_struc='one_dir',
#     data_in_files={'20-day': {v: '00000.1x20days.nc' for v in varia},
#                    '3-hourly': {v: '{}.8xday.nc'.format(v) for v in varia}},
#     idealized=False
# )

# model_start = datetime(1, 1, 1)
# length = timedelta(days=1080)
# end = model_start + length
# analysis_length = timedelta(days=500)
# a_start = str(end - analysis_length)
# a_end = str(end)

# v_atmos = ['temp', 'sphum', 'ps', 'vcomp',
#            'flux_t', 'flux_lhe', 'convection_rain',
#            'condensation_rain', 'ucomp', 'omega', 't_surf', 'height', 'vor',
#            'div', 'sw_down_sfc', 'lw_down_sfc', 'netrad_toa',
#            'vert_int_tdt_rad',
#            'vert_int_tdtlw_rad', 'vert_int_tdtsw_rad', 'dt_tg_rad',
#            'dt_tg_diffusion', 'dt_qg_diffusion', 'dt_tg_condensation',
#            'dt_tg_convection', 'qo3']

# rad_atmos = ['tdt_lw', 'tdt_sw', 'allradp']

# imr_control = Run(
#     name='imr_control',
#     description=(
#         'Control simulation of idealized moist run with realistic'
#         'radiative transfer.'
#     ),
#     data_in_direc=('/home/skc/archive/testing_2015_12_22/'
#                    'idealized_moist_rad/gfdl.ncrc2-default-repro/'
#                    '1x0m360d_32pe/history'),
#     default_date_range=(a_start, a_end),
#     data_in_dir_struc='one_dir',
#     data_in_files={'20-day': {v: ['00010101.atmos_1x20day.nc',
#                                   '00011227.atmos_1x20day.nc',
#                                   '00021222.atmos_1x20day.nc',
#                                   '00031217.atmos_1x20day.nc']
#                               for v in v_atmos},
#                    '20-day-rad': {v: ['00010101.atmos_rad_1x20day.nc',
#                                       '00011227.atmos_rad_1x20day.nc',
#                                       '00021222.atmos_rad_1x20day.nc',
#                                       '00031217.atmos_rad_1x20day.nc']
#                                   for v in rad_atmos},
#                    '3-hourly': {v: '{}.8xday.nc'.format(v) for v in varia}}
# )

# imr_fixed_h2o = Run(
#     name='imr_fixed_h2o',
#     description=(
#         'Simulation with idealized moist model with realistic radiative'
#         'transfer, but with fixed radiative effect due to water vapor.'
#     ),
#     data_in_direc=('/home/skc/archive/testing_2015_12_22/'
#                    'idealized_moist_rad_fixed_h2o/gfdl.ncrc2-default-repro/'
#                    '1x0m360d_32pe/history'),
#     default_date_range=(a_start, a_end),
#     data_in_dir_struc='one_dir',
#     data_in_files={'20-day': {v: ['00010101.atmos_1x20day.nc',
#                                   '00011227.atmos_1x20day.nc',
#                                   '00021222.atmos_1x20day.nc',
#                                   '00031217.atmos_1x20day.nc']
#                               for v in v_atmos},
#                    '20-day-rad': {v: ['00010101.atmos_rad_1x20day.nc',
#                                       '00011227.atmos_rad_1x20day.nc',
#                                       '00021222.atmos_rad_1x20day.nc',
#                                       '00031217.atmos_rad_1x20day.nc']
#                                   for v in rad_atmos},
#                    '3-hourly': {v: '{}.8xday.nc'.format(v) for v in varia}}
# )

# imr_fixed_h2o_symm = Run(
#     name='imr_fixed_h2o_symm',
#     description=(
#         'Simulation with idealized moist model with realistic radiative'
#         'transfer, but with fixed radiative effect due to water vapor.'
#         'Fixed H2O imposed to be symmetric about equator.'
#     ),
#     data_in_direc=('/home/skc/archive/testing_2015_12_22/'
#                    'idealized_moist_rad_fixed_h2o/gfdl.ncrc2-default-repro/'),
#     default_date_range=(a_start, a_end),
#     data_in_dir_struc='one_dir',
#     data_in_files={'20-day': {v: [('1x0m360d_32pe6/history/'
#                                    '00010101.atmos_1x20day.nc'),
#                                   ('1x0m720d_32pe/history/'
#                                    '00011227.atmos_1x20day.nc'),
#                                   ('1x0m360d_32pe8/history/'
#                                    '00031217.atmos_1x20day.nc'),
#                                   ('1x0m720_32pe1/history/'
#                                    '00041212.atmos_1x20day.nc')]
#                               for v in v_atmos},
#                    '20-day-rad': {v: [('1x0m360d_32pe6/history/'
#                                        '00010101.atmos_rad_1x20day.nc'),
#                                       ('1x0m720d_32pe/history/'
#                                        '00011227.atmos_rad_1x20day.nc'),
#                                       ('1x0m360d_32pe8/history/'
#                                        '00031217.atmos_rad_1x20day.nc'),
#                                       ('1x0m720d_32pe1/history/'
#                                        '00041212.atmos_rad_1x20day.nc')]
#                                   for v in rad_atmos},
#                    '3-hourly': {v: '{}.8xday.nc'.format(v) for v in varia}}
# )

# imr_2xCO2 = Run(
#     name='imr_2xCO2',
#     description=(
#         'Simulation with idealized moist model with realistic radiative'
#         'transfer, with 2xCO2 from control case.'
#     ),
#     data_in_direc=('/home/skc/archive/testing_2015_12_22/'
#                    'idealized_moist_rad_2xCO2/gfdl.ncrc2-default-repro/'),
#     default_date_range=(a_start, a_end),
#     data_in_dir_struc='one_dir',
#     data_in_files={'20-day': {v: [('1x0m360d_32pe/history/'
#                                    '00010101.atmos_1x20day.nc'),
#                                   ('1x0m720d_32pe/history/'
#                                    '00011227.atmos_1x20day.nc'),
#                                   ('1x0m360d_32pe/history/'
#                                    '00031217.atmos_1x20day.nc'),
#                                   ('1x0m720d_32pe/history/'
#                                    '00041212.atmos_1x20day.nc')]
#                               for v in v_atmos},
#                    '20-day-rad': {v: [('1x0m360d_32pe/history/'
#                                        '00010101.atmos_rad_1x20day.nc'),
#                                       ('1x0m720d_32pe/history/'
#                                        '00011227.atmos_rad_1x20day.nc'),
#                                       ('1x0m360d_32pe/history/'
#                                        '00031217.atmos_rad_1x20day.nc'),
#                                       ('1x0m720d_32pe/history/'
#                                        '00041212.atmos_rad_1x20day.nc')]
#                                   for v in rad_atmos},
#                    '3-hourly': {v: '{}.8xday.nc'.format(v) for v in varia}}
# )

# imr_fixed_h2o_2xCO2 = Run(
#     name='imr_fixed_h2o_2xCO2',
#     description=(
#         'Simulation with idealized moist model with realistic radiative'
#         'transfer, with 2xCO2 from control case and fixed H2O'
#         ' radiative effect.'
#     ),
#     data_in_direc=('/home/skc/archive/testing_2015_12_22/'
#                    'idealized_moist_rad_fixed_h2o_2xCO2/'
#                    'gfdl.ncrc2-default-repro/'),
#     default_date_range=(a_start, a_end),
#     data_in_dir_struc='one_dir',
#     data_in_files={'20-day': {v: [('1x0m360d_32pe/history/'
#                                    '00010101.atmos_1x20day.nc'),
#                                   ('1x0m720d_32pe/history/'
#                                    '00011227.atmos_1x20day.nc'),
#                                   ('1x0m360d_32pe/history/'
#                                    '00031217.atmos_1x20day.nc'),
#                                   ('1x0m720d_32pe/history/'
#                                    '00041212.atmos_1x20day.nc')]
#                               for v in v_atmos},
#                    '20-day-rad': {v: [('1x0m360d_32pe/history/'
#                                        '00010101.atmos_rad_1x20day.nc'),
#                                       ('1x0m720d_32pe/history/'
#                                        '00011227.atmos_rad_1x20day.nc'),
#                                       ('1x0m360d_32pe/history/'
#                                        '00031217.atmos_rad_1x20day.nc'),
#                                       ('1x0m720d_32pe/history/'
#                                        '00041212.atmos_rad_1x20day.nc')]
#                                   for v in rad_atmos},
#                    '3-hourly': {v: '{}.8xday.nc'.format(v) for v in varia}}
# )

# imr_rad_passive_h2o = Run(
#     name='imr_rad_passive_h2o',
#     description=(
#         'Simulation with idealized moist model with realistic radiative'
#         'transfer, but with zero radiative effect due to water vapor.'
#     ),
#     data_in_direc=('/home/skc/archive/testing_2015_12_22/'
#                    'idealized_moist_rad_passive_h2o/'
#                    'gfdl.ncrc2-default-repro/'),
#     default_date_range=(a_start, a_end),
#     data_in_dir_struc='one_dir',
#     data_in_files={'20-day': {v: [('1x0m360d_32pe/history/'
#                                    '00010101.atmos_1x20day.nc'),
#                                   ('1x0m360d_32pe/history/'
#                                    '00011227.atmos_1x20day.nc'),
#                                   ('1x0m360d_32pe/history/'
#                                    '00021222.atmos_1x20day.nc'),
#                                   ('1x0m360d_32pe/history/'
#                                    '00031217.atmos_1x20day.nc'),
#                                   ('1xm720d_32pe/history/'
#                                    '00041212.atmos_1x20day.nc')]
#                               for v in v_atmos},
#                    '20-day-rad': {v: [('1x0m360d_32pe/history/'
#                                        '00010101.atmos_rad_1x20day.nc'),
#                                       ('1x0m360d_32pe/history/'
#                                        '00011227.atmos_rad_1x20day.nc'),
#                                       ('1x0m360d_32pe/history/'
#                                        '00021222.atmos_rad_1x20day.nc'),
#                                       ('1x0m360d_32pe/history/'
#                                        '00031217.atmos_rad_1x20day.nc'),
#                                       ('1xm720d_32pe/history/'
#                                        '00041212.atmos_rad_1x20day.nc')]
#                                   for v in rad_atmos},
#                    '3-hourly': {v: '{}.8xday.nc'.format(v) for v in varia}}
# )

# imr_control_yi = Run(
#     name='imr_control_yi',
#     description=(
#         'Control simulation of idealized moist run with realistic'
#         'radiative transfer; Yi ran this one.'
#     ),
#     data_in_direc=('/archive/yim/ulm_201505/idealized_moist_rad/'
#                    'gfdl.ncrc2-default-prod/1x0m500d_32pe/history'),
#     default_date_range=('0001-01-01', '0001-12-27'),
#     data_in_dir_struc='one_dir',
#     data_in_files={'daily': {v: '00010312.atmos_daily.nc' for v in varia},
#                    '3-hourly': {v: '{}.8xday.nc'.format(v) for v in varia}},
#     idealized=False
# )
