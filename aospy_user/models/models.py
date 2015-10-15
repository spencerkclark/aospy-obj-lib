from aospy.model import Model
import aospy_user.runs.cases as runs
import aospy_user.runs.idealized as idealized

am2 = Model(
    name='am2',
    nc_grid_paths=(
        ('/archive/Yi.Ming/sm2.1_fixed/SM2.1U_Control-1860_lm2_aie_rerun6.YIM/pp/atmos/atmos.static.nc'),
         ('/archive/Yi.Ming/sm2.1_fixed/SM2.1U_Control-1860_lm2_aie_rerun6.YIM/pp/atmos_level/atmos_level.static.nc'),
         ('/archive/Yi.Ming/sm2.1_fixed/SM2.1U_Control-1860_lm2_aie_rerun6.YIM/pp/atmos_level/ts/monthly/5yr/atmos_level.011601-012012.vcomp.nc'),
         ('/archive/Yi.Ming/sm2.1_fixed/SM2.1U_Control-1860_lm2_aie_rerun6.YIM/pp/atmos/ts/monthly/100yr/atmos.000101-010012.temp.nc')
         ),
    nc_dur=1,
    nc_start_yr=1,
    nc_end_yr=100,
    default_yr_range=(21,100),
    runs=[runs.am2_control, runs.am2_tropics, runs.am2_extratropics, runs.am2_tropics_and_extratropics,
          runs.am2_reyoi_extratropics_full, runs.am2_reyoi_extratropics_sp, runs.am2_reyoi_extratropics_u, runs.am2_reyoi_control,
          runs.am2_HadISST_control,runs.am2_reyoi_tropics_sp_SI, runs.am2_reyoi_extratropics_sp_SI,runs.am2_reyoi_tropics_full, runs.am2_reyoi_tropics_u],
    default_runs=[runs.am2_control, runs.am2_tropics, runs.am2_extratropics, runs.am2_tropics_and_extratropics,
                  runs.am2_reyoi_extratropics_full, runs.am2_reyoi_extratropics_sp, runs.am2_reyoi_extratropics_u, runs.am2_reyoi_control,
                  runs.am2_HadISST_control, runs.am2_reyoi_extratropics_sp_SI, runs.am2_reyoi_tropics_sp_SI, runs.am2_reyoi_tropics_full, runs.am2_reyoi_tropics_u],
    read_mode='xray'
)

dargan = Model(
    name='dargan',
    nc_grid_paths=(
        ('/archive/skc/idealized_moist_T85/control_T85/gfdl.ncrc2-default-prod/1x0m720d_32pe/history/00000.1x20days.nc'),
        ),
    runs=[idealized.control_T85, idealized.extratropics_15_T85, idealized.extratropics_037_T85,
          idealized.tropics_10_T85, idealized.tropics_025_T85],
    default_runs=[idealized.control_T85, idealized.extratropics_15_T85, idealized.extratropics_037_T85,
                  idealized.tropics_10_T85, idealized.tropics_025_T85],
    read_mode='xray'
)
