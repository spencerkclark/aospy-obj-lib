from aospy.model import Model
import aospy_user.runs.cases as runs

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
    runs=[runs.am2_control],
    default_runs=[runs.am2_control],
    read_mode='xray'
)

dargan = Model(
    name='dargan',
    nc_grid_paths=(
        ('/work/skc/idealized_moist_T85/control_T85/00000.1x20days.nc'),
        ),
    nc_dur=720,
    nc_start_yr=1,
    nc_end_yr=720,
    default_yr_range=(360,720),
    runs=[runs.dargan_control],
    default_runs=[runs.dargan_control],
    read_mode='xray'
)
