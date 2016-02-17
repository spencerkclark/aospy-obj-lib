from aospy.model import Model
import aospy_user.runs.cases as runs
import aospy_user.runs.idealized as idealized
import aospy_user.runs.idealized_moist_rad as imr

am2 = Model(
    name='am2',
    grid_file_paths=(
        ('/archive/Yi.Ming/sm2.1_fixed/SM2.1U_Control-1860_lm2_aie_rerun6.YIM/'
         'pp/atmos/atmos.static.nc'),
        ('/archive/Yi.Ming/sm2.1_fixed/SM2.1U_Control-1860_lm2_aie_rerun6.YIM/'
         'pp/atmos_level/atmos_level.static.nc'),
        ('/archive/Yi.Ming/sm2.1_fixed/SM2.1U_Control-1860_lm2_aie_rerun6.YIM/'
         'pp/atmos_level/ts/monthly/5yr/atmos_level.011601-012012.vcomp.nc'),
        ('/archive/Yi.Ming/sm2.1_fixed/SM2.1U_Control-1860_lm2_aie_rerun6.YIM/'
         'pp/atmos/ts/monthly/100yr/atmos.000101-010012.temp.nc')
    ),
    runs=[runs.am2_control, runs.am2_tropics, runs.am2_extratropics,
          runs.am2_tropics_and_extratropics],
    default_runs=[runs.am2_control, runs.am2_tropics, runs.am2_extratropics,
                  runs.am2_tropics_and_extratropics]
)

am2_reyoi = Model(
    name='am2_reyoi',
    grid_file_paths=(
        ('/archive/yim/siena_201203/m45_am2p14_1990/gfdl.ncrc2-intel-prod/'
         'pp/atmos/atmos.static.nc',
         '/archive/yim/siena_201203/m45_am2p14_1990/gfdl.ncrc2-intel-prod/'
         'pp/atmos_level/atmos_level.static.nc',
         '/archive/yim/siena_201203/m45_am2p14_1990/gfdl.ncrc2-intel-prod/'
         'pp/atmos/ts/annual/16yr/atmos.1983-1998.temp.nc',
         '/archive/yim/siena_201203/m45_am2p14_1990/gfdl.ncrc2-intel-prod/'
         'pp/atmos_level/ts/monthly/16yr/atmos_level.198301-199812.temp.nc')
    ),
    runs=[runs.am2_HadISST_control, runs.am2_reyoi_extratropics_full,
          runs.am2_reyoi_extratropics_sp, runs.am2_reyoi_extratropics_u,
          runs.am2_reyoi_extratropics_sp_SI,
          runs.am2_reyoi_tropics_sp_SI, runs.am2_reyoi_tropics_full,
          runs.am2_reyoi_tropics_u],
    default_runs=[runs.am2_HadISST_control, runs.am2_reyoi_extratropics_full,
                  runs.am2_reyoi_extratropics_sp,
                  runs.am2_reyoi_extratropics_u,
                  runs.am2_reyoi_extratropics_sp_SI,
                  runs.am2_reyoi_tropics_sp_SI, runs.am2_reyoi_tropics_full,
                  runs.am2_reyoi_tropics_u]
)

dargan = Model(
    name='dargan',
    grid_file_paths=(
        ('/archive/skc/idealized_moist_T85/control_T85/'
         'gfdl.ncrc2-default-prod/'
         '1x0m720d_32pe/history/00000.1x20days.nc',
         '/home/skc/inputdata/aquaplanet.land_mask.nc'),
    ),
    runs=[idealized.control_T85, idealized.extratropics_15_T85,
          idealized.extratropics_037_T85,
          idealized.tropics_10_T85, idealized.tropics_025_T85],
    default_runs=[idealized.control_T85, idealized.extratropics_15_T85,
                  idealized.extratropics_037_T85,
                  idealized.tropics_10_T85, idealized.tropics_025_T85],
)

dargan_T42 = Model(
    name='dargan_T42',
    grid_file_paths=(
        ('/archive/skc/idealized_moist_alb_T42/control_alb_T42/'
         'gfdl.ncrc2-default-prod/1x0m720d_32pe/history/00000.1x20days.nc',
         '/home/skc/inputdata/aquaplanet.land_mask.nc'),
    ),
    runs=[idealized.control_alb_T42, idealized.control_gaussian_T42,
          idealized.tropics_gaussian_5_T42,
          idealized.extratropics_gaussian_5_T42,
          idealized.tropics_gaussian_15_T42,
          idealized.extratropics_gaussian_15_T42,
          idealized.tropics_gaussian_25_T42,
          idealized.extratropics_gaussian_25_T42],
    default_runs=[idealized.control_alb_T42],
)

idealized_moist_rad = Model(
    name='idealized_moist_rad',
    grid_file_paths=(
        ('/home/skc/archive/testing_2015_12_22/idealized_moist_rad/'
         'gfdl.ncrc2-default-repro/1x0m360d_32pe/history/'
         '00010101.atmos_1x20day.nc',
         '/home/skc/inputdata/aquaplanet.land_mask.nc'),
    ),
    runs=[idealized.imr_control, idealized.imr_fixed_h2o,
          idealized.imr_control_yi, idealized.imr_rad_passive_h2o,
          idealized.imr_fixed_h2o_symm, idealized.imr_2xCO2,
          idealized.imr_fixed_h2o_2xCO2, imr.control, imr.conv_off,
          imr.double_CO2, imr.fixed_h2o, imr.fixed_h2o_2xCO2, imr.asym_e5,
          imr.asym_t5, imr.asym_e15, imr.asym_t15, imr.asym_t20],
    default_runs=[idealized.imr_control, idealized.imr_fixed_h2o,
                  idealized.imr_control_yi, idealized.imr_rad_passive_h2o,
                  idealized.imr_fixed_h2o_symm, idealized.imr_2xCO2,
                  idealized.imr_fixed_h2o_2xCO2, imr.control, imr.conv_off,
                  imr.double_CO2, imr.fixed_h2o, imr.fixed_h2o_2xCO2,
                  imr.asym_e5, imr.asym_t5, imr.asym_e15, imr.asym_t15,
                  imr.asym_t20],
)
