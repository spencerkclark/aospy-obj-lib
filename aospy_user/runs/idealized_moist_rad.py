import os
from datetime import datetime

from aospy import Run
from aospy.data_loader import DictDataLoader


def data_dir(run, fre_stem='imr_skc', iteration='', tag=''):
    ROOT = os.path.join('/archive/Spencer.Clark/', fre_stem)
    return os.path.join(ROOT, run, 'gfdl.ncrc3-default-repro/',
                        tag, iteration, 'history')


def file_map(run, fre_stem='imr_skc', iteration='', tag=''):
    return {'monthly': os.path.join(
            data_dir(run, fre_stem, iteration, tag), '00*0101.atmos_month.nc'),
            'rad_monthly': os.path.join(
            data_dir(run, fre_stem, iteration, tag),
            '00*0101.atmos_rad_month.nc'),
            '3hr': os.path.join(
            data_dir(run, fre_stem, iteration, tag), '00*0101.atmos_8xday.nc')}


control = Run(
    name='control',
    description=(
        'Control simulation of idealized moist run with realistic'
        'radiative transfer and parameterized moist convection.'
    ),
    default_start_date=datetime(3, 1, 1),
    default_end_date=datetime(6, 12, 31),
    data_loader=DictDataLoader(file_map('control', iteration='1'))
)

conv_off = Run(
    name='conv_off',
    description=(
        'Control simulation of idealized moist run with realistic'
        'radiative transfer, without parameterized moist convection.'
    ),
    default_start_date=datetime(3, 1, 1),
    default_end_date=datetime(6, 12, 31),
    data_loader=DictDataLoader(file_map('conv_off'))
)

fixed_h2o_conv_off = Run(
    name='fixed_h2o_conv_off',
    description=(
        'Control simulation of idealized moist run with fixed'
        'water radiative transfer, and no moist convection.'
    ),
    default_start_date=datetime(3, 1, 1),
    default_end_date=datetime(6, 12, 31),
    data_loader=DictDataLoader(file_map('fixed_h2o_conv_off', iteration='5'))
)

double_CO2 = Run(
    name='2xCO2',
    description=(
        'Simulation with fully coupled water vapor, dynamics, and'
        ' radiation.  CO2 at twice current levels.'
    ),
    default_start_date=datetime(3, 1, 1),
    default_end_date=datetime(6, 12, 31),
    data_loader=DictDataLoader(file_map('2xCO2'))
)

fixed_h2o = Run(
    name='fixed_h2o',
    description=(
        'Simulation with fully coupled water vapor and dynamics.'
        ' Radiation code sees constant climatological water vapor pattern.'
    ),
    default_start_date=datetime(3, 1, 1),
    default_end_date=datetime(6, 12, 31),
    data_loader=DictDataLoader(file_map('fixed_h2o'))
)

fixed_h2o_2xCO2 = Run(
    name='fixed_h2o_2xCO2',
    description=(
        'Simulation with fully coupled water vapor and dynamics.'
        ' Radiation code sees constant climatological water vapor pattern'
        ' from 1xCO2 control experiment.  Atmosphere contains double'
        ' modern-day CO2.'
    ),
    default_start_date=datetime(3, 1, 1),
    default_end_date=datetime(6, 12, 31),
    data_loader=DictDataLoader(file_map('fixed_h2o_2xCO2'))
)

asym_e5 = Run(
    name='asym_e5',
    description=(
        'Fully coupled water vapor, dynamics, and radiation.'
        ' 10 W m-2 asymmetry in solar forcing imposed in extratropics.'
    ),
    default_start_date=datetime(3, 1, 1),
    default_end_date=datetime(6, 12, 31),
    data_loader=DictDataLoader(file_map('asym_e5'))
)

asym_t5 = Run(
    name='asym_t5',
    description=(
        'Fully coupled water vapor, dynamics, and radiation.'
        ' 10 W m-2 asymmetry in solar forcing imposed in tropics.'
    ),
    default_start_date=datetime(3, 1, 1),
    default_end_date=datetime(6, 12, 31),
    data_loader=DictDataLoader(file_map('asym_t5'))
)

asym_e15 = Run(
    name='asym_e15',
    description=(
        'Fully coupled water vapor, dynamics, and radiation.'
        ' 30 W m-2 asymmetry in solar forcing imposed in extratropics.'
    ),
    default_start_date=datetime(3, 1, 1),
    default_end_date=datetime(6, 12, 31),
    data_loader=DictDataLoader(file_map('asym_e15', iteration='2'))
)

asym_t15 = Run(
    name='asym_t15',
    description=(
        'Fully coupled water vapor, dynamics, and radiation.'
        ' 30 W m-2 asymmetry in solar forcing imposed in tropics.'
    ),
    default_start_date=datetime(3, 1, 1),
    default_end_date=datetime(6, 12, 31),
    data_loader=DictDataLoader(file_map('asym_t15', iteration='2'))
)

asym_e18 = Run(
    name='asym_e18',
    description=(
        'Fully coupled water vapor, dynamics, and radiation.'
        ' 36 W m-2 asymmetry in solar forcing imposed in extratropics.'
    ),
    default_start_date=datetime(3, 1, 1),
    default_end_date=datetime(6, 12, 31),
    data_loader=DictDataLoader(file_map('asym_e18'))
)

asym_t18 = Run(
    name='asym_t18',
    description=(
        'Fully coupled water vapor, dynamics, and radiation.'
        ' 36 W m-2 asymmetry in solar forcing imposed in tropics.'
    ),
    default_start_date=datetime(3, 1, 1),
    default_end_date=datetime(6, 12, 31),
    data_loader=DictDataLoader(file_map('asym_t18'))
)

asym_t20 = Run(
    name='asym_t20',
    description=(
        'Fully coupled water vapor, dynamics, and radiation.'
        ' 40 W m-2 asymmetry in solar forcing imposed in tropics.'
    ),
    default_start_date=datetime(3, 1, 1),
    default_end_date=datetime(6, 12, 31),
    data_loader=DictDataLoader(file_map('asym_t20'))
)

asym_e5_conv_off = Run(
    name='asym_e5_conv_off',
    description=(
        'Fully coupled water vapor, dynamics, and radiation.'
        ' 10 W m-2 asymmetry in solar forcing imposed in extratropics.'
        ' Moist convection is turned off in the model.'
    ),
    default_start_date=datetime(3, 1, 1),
    default_end_date=datetime(6, 12, 31),
    data_loader=DictDataLoader(file_map('asym_e5_conv_off'))
)

asym_t5_conv_off = Run(
    name='asym_t5_conv_off',
    description=(
        'Fully coupled water vapor, dynamics, and radiation.'
        ' 10 W m-2 asymmetry in solar forcing imposed in tropics.'
        ' Moist convection is turned off in the model.'
    ),
    default_start_date=datetime(3, 1, 1),
    default_end_date=datetime(6, 12, 31),
    data_loader=DictDataLoader(file_map('asym_t5_conv_off'))
)

asym_e15_conv_off = Run(
    name='asym_e15_conv_off',
    description=(
        'Fully coupled water vapor, dynamics, and radiation.'
        ' 30 W m-2 asymmetry in solar forcing imposed in extratropics.'
        ' Moist convection is turned off in the model.'
    ),
    default_start_date=datetime(3, 1, 1),
    default_end_date=datetime(6, 12, 31),
    data_loader=DictDataLoader(file_map('asym_e15_conv_off'))
)

asym_t15_conv_off = Run(
    name='asym_t15_conv_off',
    description=(
        'Fully coupled water vapor, dynamics, and radiation.'
        ' 30 W m-2 asymmetry in solar forcing imposed in tropics.'
        ' Moist convection is turned off in the model.'
    ),
    default_start_date=datetime(3, 1, 1),
    default_end_date=datetime(6, 12, 31),
    data_loader=DictDataLoader(file_map('asym_t15_conv_off', iteration='1'))
)

asym_e18_conv_off = Run(
    name='asym_e18_conv_off',
    description=(
        'Fully coupled water vapor, dynamics, and radiation.'
        ' 36 W m-2 asymmetry in solar forcing imposed in extratropics.'
        ' Moist convection is turned off in the model.'
    ),
    default_start_date=datetime(3, 1, 1),
    default_end_date=datetime(6, 12, 31),
    data_loader=DictDataLoader(file_map('asym_e18_conv_off'))
)

asym_t18_conv_off = Run(
    name='asym_t18_conv_off',
    description=(
        'Fully coupled water vapor, dynamics, and radiation.'
        ' 36 W m-2 asymmetry in solar forcing imposed in tropics.'
        ' Moist convection is turned off in the model.'
    ),
    default_start_date=datetime(3, 1, 1),
    default_end_date=datetime(6, 12, 31),
    data_loader=DictDataLoader(file_map('asym_t18_conv_off'))
)

asym_e5_conv_off_fixed_h2o = Run(
    name='asym_e5_conv_off_fixed_h2o',
    description=(
        'Fully coupled water vapor, dynamics.  Fixed radiatively active water.'
        ' 10 W m-2 asymmetry in solar forcing imposed in extratropics.'
        ' Moist convection is turned off in the model.'
    ),
    default_start_date=datetime(3, 1, 1),
    default_end_date=datetime(6, 12, 31),
    data_loader=DictDataLoader(file_map('asym_e5_conv_off_fixed_h2o',
                               iteration='3'))
)

asym_t5_conv_off_fixed_h2o = Run(
    name='asym_t5_conv_off_fixed_h2o',
    description=(
        'Fully coupled water vapor, dynamics.  Fixed radiatively active water.'
        ' 10 W m-2 asymmetry in solar forcing imposed in tropics.'
        ' Moist convection is turned off in the model.'
    ),
    default_start_date=datetime(3, 1, 1),
    default_end_date=datetime(6, 12, 31),
    data_loader=DictDataLoader(file_map('asym_t5_conv_off_fixed_h2o',
                               iteration='2'))
)

asym_e15_conv_off_fixed_h2o = Run(
    name='asym_e15_conv_off_fixed_h2o',
    description=(
        'Fully coupled water vapor, dynamics.  Fixed radiatvely active water.'
        ' 30 W m-2 asymmetry in solar forcing imposed in extratropics.'
        ' Moist convection is turned off in the model.'
    ),
    default_start_date=datetime(3, 1, 1),
    default_end_date=datetime(6, 12, 31),
    data_loader=DictDataLoader(file_map('asym_e15_conv_off_fixed_h2o',
                               iteration='3'))
)

asym_t15_conv_off_fixed_h2o = Run(
    name='asym_t15_conv_off_fixed_h2o',
    description=(
        'Fully coupled water vapor, dynamics.  Fixed radiatively active water.'
        ' 30 W m-2 asymmetry in solar forcing imposed in tropics.'
        ' Moist convection is turned off in the model.'
    ),
    default_start_date=datetime(3, 1, 1),
    default_end_date=datetime(6, 12, 31),
    data_loader=DictDataLoader(file_map('asym_t15_conv_off_fixed_h2o',
                               iteration='2'))
)

asym_e18_conv_off_fixed_h2o = Run(
    name='asym_e18_conv_off_fixed_h2o',
    description=(
        'Fully coupled water vapor, dynamics.  Fixed radiatively active water.'
        ' 36 W m-2 asymmetry in solar forcing imposed in extratropics.'
        ' Moist convection is turned off in the model.'
    ),
    default_start_date=datetime(3, 1, 1),
    default_end_date=datetime(6, 12, 31),
    data_loader=DictDataLoader(file_map('asym_e18_conv_off_fixed_h2o',
                               iteration='3'))
)

asym_t18_conv_off_fixed_h2o = Run(
    name='asym_t18_conv_off_fixed_h2o',
    description=(
        'Fully coupled water vapor, dynamics.  Fixed radiatively active water.'
        ' 36 W m-2 asymmetry in solar forcing imposed in tropics.'
        ' Moist convection is turned off in the model.'
    ),
    default_start_date=datetime(3, 1, 1),
    default_end_date=datetime(6, 12, 31),
    data_loader=DictDataLoader(file_map('asym_t18_conv_off_fixed_h2o',
                               iteration='2'))
)

asym_e15_fixed_h2o = Run(
    name='asym_e15_fixed_h2o',
    description=(
        'Radiatvely passive water vapor.'
        ' 30 W m-2 asymmetry in solar forcing imposed in extratropics.'
    ),
    default_start_date=datetime(3, 1, 1),
    default_end_date=datetime(6, 12, 31),
    data_loader=DictDataLoader(file_map('asym_e15_fixed_h2o', iteration='2'))
)

asym_t15_fixed_h2o = Run(
    name='asym_t15_fixed_h2o',
    description=(
        'Radiatively passive water vapor.'
        ' 30 W m-2 asymmetry in solar forcing imposed in tropics.'
    ),
    default_start_date=datetime(3, 1, 1),
    default_end_date=datetime(6, 12, 31),
    data_loader=DictDataLoader(file_map('asym_t15_fixed_h2o', iteration='2'))
)

asym_e18_fixed_h2o = Run(
    name='asym_e18_fixed_h2o',
    description=(
        'Radiatvely passive water vapor.'
        ' 36 W m-2 asymmetry in solar forcing imposed in extratropics.'
    ),
    default_start_date=datetime(3, 1, 1),
    default_end_date=datetime(6, 12, 31),
    data_loader=DictDataLoader(file_map('asym_e18_fixed_h2o',
                                        tag='ncrc3.default-repro'))
)

asym_t18_fixed_h2o = Run(
    name='asym_t18_fixed_h2o',
    description=(
        'Radiatively passive water vapor.'
        ' 36 W m-2 asymmetry in solar forcing imposed in tropics.'
    ),
    default_start_date=datetime(3, 1, 1),
    default_end_date=datetime(6, 12, 31),
    data_loader=DictDataLoader(file_map('asym_t18_fixed_h2o',
                                        tag='ncrc3.default-repro'))
)

asym_e5_fixed_h2o = Run(
    name='asym_e5_fixed_h2o',
    description=(
        'Radiatvely passive water vapor.'
        ' 10 W m-2 asymmetry in solar forcing imposed in extratropics.'
    ),
    default_start_date=datetime(3, 1, 1),
    default_end_date=datetime(6, 12, 31),
    data_loader=DictDataLoader(file_map('asym_e5_fixed_h2o',
                                        tag='ncrc3.default-repro'))
)

asym_t5_fixed_h2o = Run(
    name='asym_t5_fixed_h2o',
    description=(
        'Radiatively passive water vapor.'
        ' 10 W m-2 asymmetry in solar forcing imposed in tropics.'
    ),
    default_start_date=datetime(3, 1, 1),
    default_end_date=datetime(6, 12, 31),
    data_loader=DictDataLoader(file_map('asym_t5_fixed_h2o',
                                        tag='ncrc3.default-repro'))
)

asym_e15_net_zero_solar = Run(
    name='asym_e15_net_zero_solar',
    description=(
        'Net zero solar heating.'
        ' 30 W m-2 asymmetry in solar forcing imposed in extratropics.'
    ),
    default_start_date=datetime(3, 1, 1),
    default_end_date=datetime(6, 12, 31),
    data_loader=DictDataLoader(file_map('asym_e15_net_zero_solar',
                               fre_stem='imr_skc_net_zero_solar'))
)

asym_t15_net_zero_solar = Run(
    name='asym_t15_net_zero_solar',
    description=(
        'Net zero solar heating.'
        ' 30 W m-2 asymmetry in solar forcing imposed in tropics.'
    ),
    default_start_date=datetime(3, 1, 1),
    default_end_date=datetime(6, 12, 31),
    data_loader=DictDataLoader(file_map('asym_t15_net_zero_solar',
                               fre_stem='imr_skc_net_zero_solar'))
)

eq_5 = Run(
    name='eq_5',
    description=(
        'Fully coupled water vapor, dynamics, and radiation.'
        ' 5 W m-2 global area average forcing imposed at the equator'
    ),
    default_start_date=datetime(3, 1, 1),
    default_end_date=datetime(6, 12, 31),
    data_loader=DictDataLoader(file_map('eq_5',
                               fre_stem='imr_skc_eq_forcing'))
)

eq_6 = Run(
    name='eq_6',
    description=(
        'Fully coupled water vapor, dynamics, and radiation.'
        ' 6 W m-2 global area average forcing imposed at the equator'
    ),
    default_start_date=datetime(3, 1, 1),
    default_end_date=datetime(6, 12, 31),
    data_loader=DictDataLoader(file_map('eq_6',
                               fre_stem='imr_skc_eq_forcing'))
)

eq_7 = Run(
    name='eq_7',
    description=(
        'Fully coupled water vapor, dynamics, and radiation.'
        ' 7 W m-2 global area average forcing imposed at the equator'
    ),
    default_start_date=datetime(3, 1, 1),
    default_end_date=datetime(6, 12, 31),
    data_loader=DictDataLoader(file_map('eq_7',
                               fre_stem='imr_skc_eq_forcing'))
)

eq_8 = Run(
    name='eq_8',
    description=(
        'Fully coupled water vapor, dynamics, and radiation.'
        ' 8 W m-2 global area average forcing imposed at the equator'
    ),
    default_start_date=datetime(3, 1, 1),
    default_end_date=datetime(6, 12, 31),
    data_loader=DictDataLoader(file_map('eq_8',
                               fre_stem='imr_skc_eq_forcing'))
)

eq_15 = Run(
    name='eq_15',
    description=(
        'Fully coupled water vapor, dynamics, and radiation.'
        ' 15 W m-2 global area average forcing imposed at the equator'
    ),
    default_start_date=datetime(3, 1, 1),
    default_end_date=datetime(6, 12, 31),
    data_loader=DictDataLoader(file_map('eq_15',
                               fre_stem='imr_skc_eq_forcing'))
)

eq_25 = Run(
    name='eq_25',
    description=(
        'Fully coupled water vapor, dynamics, and radiation.'
        ' 25 W m-2 global area average forcing imposed at the equator'
    ),
    default_start_date=datetime(3, 1, 1),
    default_end_date=datetime(6, 12, 31),
    data_loader=DictDataLoader(file_map('eq_25',
                               fre_stem='imr_skc_eq_forcing'))
)

eq_35 = Run(
    name='eq_35',
    description=(
        'Fully coupled water vapor, dynamics, and radiation.'
        ' 35 W m-2 global area average forcing imposed at the equator'
    ),
    default_start_date=datetime(3, 1, 1),
    default_end_date=datetime(6, 12, 31),
    data_loader=DictDataLoader(file_map('eq_35',
                               fre_stem='imr_skc_eq_forcing'))
)

land_test = Run(
    name='land_test',
    description=(
        'Testing the idealized moist full radiation model with crude land'
    ),
    default_start_date=datetime(3, 1, 1),
    default_end_date=datetime(6, 12, 31),
    data_loader=DictDataLoader(file_map('land_test',
                               fre_stem='imr_skc_crude_land',
                               iteration='1'))
)

earth_land = Run(
    name='earth_land',
    description=(
        'Testing the idealized moist full radiation model with earth like'
        'crude land'),
    default_start_date=datetime(3, 1, 1),
    default_end_date=datetime(6, 12, 31),
    data_loader=DictDataLoader(file_map('earth_land',
                               fre_stem='imr_skc_crude_land'))
)

earth_land_seasons = Run(
    name='earth_land_seasons',
    description=(
        'Testing the idealized moist full radiation model with earth like'
        'crude land.  Seasonal cycle added; 20 m mixed layer depth.'),
    default_start_date=datetime(3, 1, 1),
    default_end_date=datetime(6, 12, 31),
    data_loader=DictDataLoader(file_map('earth_land_seasons',
                               fre_stem='imr_skc_crude_land'))
)

rect_seasons = Run(
    name='rect_seasons',
    description=(
        'Testing the idealized moist full radiation model with rectangular'
        'crude land.  Seasonal cycle added; 20 m mixed layer depth.'),
    default_start_date=datetime(3, 1, 1),
    default_end_date=datetime(6, 12, 31),
    data_loader=DictDataLoader(file_map('rect_seasons',
                               fre_stem='imr_skc_crude_land',
                               iteration='4'))
)

asym_t15_fixed_h2o_tropics = Run(
    name='asym_t15_fixed_h2o_tropics',
    description=(
        'Radiatively passive water vapor.'
        ' 30 W m-2 asymmetry in solar forcing imposed in tropics.'
        ' Fixed water in 20S to 20N'
    ),
    default_start_date=datetime(3, 1, 1),
    default_end_date=datetime(6, 12, 31),
    data_loader=DictDataLoader(file_map('asym_t15_fixed_h2o_tropics',
                               fre_stem='imr_skc_develop'))
)

asym_e15_fixed_h2o_tropics = Run(
    name='asym_e15_fixed_h2o_tropics',
    description=(
        'Radiatively passive water vapor.'
        ' 30 W m-2 asymmetry in solar forcing imposed in extratropics.'
        ' Fixed water in 20S to 20N'
    ),
    default_start_date=datetime(3, 1, 1),
    default_end_date=datetime(6, 12, 31),
    data_loader=DictDataLoader(file_map('asym_e15_fixed_h2o_tropics',
                               fre_stem='imr_skc_develop'))
)

asym_t15_fixed_h2o_extratropics = Run(
    name='asym_t15_fixed_h2o_extratropics',
    description=(
        'Radiatively passive water vapor.'
        ' 30 W m-2 asymmetry in solar forcing imposed in tropics.'
        ' Fixed water outside 20S to 20N'
    ),
    default_start_date=datetime(3, 1, 1),
    default_end_date=datetime(6, 12, 31),
    data_loader=DictDataLoader(file_map('asym_t15_fixed_h2o_extratropics',
                               fre_stem='imr_skc_develop'))
)

asym_e15_fixed_h2o_extratropics = Run(
    name='asym_e15_fixed_h2o_extratropics',
    description=(
        'Radiatively passive water vapor.'
        ' 30 W m-2 asymmetry in solar forcing imposed in extratropics.'
        ' Fixed water outside 20S to 20N'
    ),
    default_start_date=datetime(3, 1, 1),
    default_end_date=datetime(6, 12, 31),
    data_loader=DictDataLoader(file_map('asym_e15_fixed_h2o_extratropics',
                               fre_stem='imr_skc_develop'))
)

zero_o3 = Run(
    name='zero_o3',
    description=(
        'Control simulation of idealized moist run with realistic'
        'radiative transfer with zero ozone.'
    ),
    default_start_date=datetime(3, 1, 1),
    default_end_date=datetime(6, 12, 31),
    data_loader=DictDataLoader(file_map('zero_o3', fre_stem='imr_skc_develop'))
)

anti_t15 = Run(
    name='anti_t15',
    description=(
        'Antisymmetric gaussian solar forcing. Asymmetry equivalent to'
        ' asym_*15 cases.'
    ),
    default_start_date=datetime(3, 1, 1),
    default_end_date=datetime(6, 12, 31),
    data_loader=DictDataLoader(file_map('anti_t15',
                               fre_stem='imr_skc_develop'))
)

anti_e15 = Run(
    name='anti_e15',
    description=(
        'Antisymmetric gaussian solar forcing. Asymmetry equivalent to'
        ' asym_*15 cases.'
    ),
    default_start_date=datetime(3, 1, 1),
    default_end_date=datetime(6, 12, 31),
    data_loader=DictDataLoader(file_map('anti_e15',
                               fre_stem='imr_skc_develop'))
)

anti_t15_fixed_h2o = Run(
    name='anti_t15_fixed_h2o',
    description=(
        'Antisymmetric gaussian solar forcing. Asymmetry equivalent to'
        ' asym_*15 cases.'
    ),
    default_start_date=datetime(3, 1, 1),
    default_end_date=datetime(6, 12, 31),
    data_loader=DictDataLoader(file_map('anti_t15_fixed_h2o',
                               fre_stem='imr_skc_develop'))
)

anti_e15_fixed_h2o = Run(
    name='anti_e15_fixed_h2o',
    description=(
        'Antisymmetric gaussian solar forcing. Asymmetry equivalent to'
        ' asym_*15 cases.'
    ),
    default_start_date=datetime(3, 1, 1),
    default_end_date=datetime(6, 12, 31),
    data_loader=DictDataLoader(file_map('anti_e15_fixed_h2o',
                               fre_stem='imr_skc_develop'))
)

anti_t15_fixed_h2o_tropics = Run(
    name='anti_t15_fixed_h2o_tropics',
    description=(
        'Antisymmetric gaussian solar forcing. Asymmetry equivalent to'
        ' asym_*15 cases.'
    ),
    default_start_date=datetime(3, 1, 1),
    default_end_date=datetime(6, 12, 31),
    data_loader=DictDataLoader(file_map('anti_t15_fixed_h2o_tropics',
                               fre_stem='imr_skc_develop'))
)

anti_e15_fixed_h2o_tropics = Run(
    name='anti_e15_fixed_h2o_tropics',
    description=(
        'Antisymmetric gaussian solar forcing. Asymmetry equivalent to'
        ' asym_*15 cases.'
    ),
    default_start_date=datetime(3, 1, 1),
    default_end_date=datetime(6, 12, 31),
    data_loader=DictDataLoader(file_map('anti_e15_fixed_h2o_tropics',
                               fre_stem='imr_skc_develop'))
)

anti_t15_fixed_h2o_extratropics = Run(
    name='anti_t15_fixed_h2o_extratropics',
    description=(
        'Antisymmetric gaussian solar forcing. Asymmetry equivalent to'
        ' asym_*15 cases.'
    ),
    default_start_date=datetime(3, 1, 1),
    default_end_date=datetime(6, 12, 31),
    data_loader=DictDataLoader(file_map('anti_t15_fixed_h2o_extratropics',
                               fre_stem='imr_skc_develop'))
)

anti_e15_fixed_h2o_extratropics = Run(
    name='anti_e15_fixed_h2o_extratropics',
    description=(
        'Antisymmetric gaussian solar forcing. Asymmetry equivalent to'
        ' asym_*15 cases.'
    ),
    default_start_date=datetime(3, 1, 1),
    default_end_date=datetime(6, 12, 31),
    data_loader=DictDataLoader(file_map('anti_e15_fixed_h2o_extratropics',
                               fre_stem='imr_skc_develop'))
)

control_gray = Run(
    name='control_gray',
    description=(
        'Case with symmetric solar insolation and a gray atmosphere.'
    ),
    default_start_date=datetime(3, 1, 1),
    default_end_date=datetime(6, 12, 31),
    data_loader=DictDataLoader(file_map('control_gray',
                               fre_stem='imr_skc_develop',
                               iteration='5'))
)

control_gray_solar = Run(
    name='control_gray_solar',
    description=(
        'Case with symmetric solar insolation and a gray atmosphere.'
        ' Includes a parameterization of absorption of shortwave radiation.'
        ' The absorption parameter is set to 0.2 and the solar exponent is 4.0'
    ),
    default_start_date=datetime(3, 1, 1),
    default_end_date=datetime(6, 12, 31),
    data_loader=DictDataLoader(file_map('control_gray_solar',
                               fre_stem='imr_skc_develop',
                               iteration='7'))
)

control_raw = Run(
    name='control_raw',
    description=(
        'Case with as few code modifications as possible. '
        'This is meant as a test on the swdn_toa diagnostic.'
    ),
    default_start_date=datetime(3, 1, 1),
    default_end_date=datetime(6, 12, 31),
    data_loader=DictDataLoader(file_map('control',
                               fre_stem='imr_skc_working_base',
                               iteration='2'))
)
