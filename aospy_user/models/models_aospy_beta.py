from aospy.model import Model

import aospy_user.runs.cases as runs
import aospy_user.runs.imr_aospy_beta as imr

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
    runs=[runs.am2_control],
    default_runs=[runs.am2_control]
)

idealized_moist_rad = Model(
    name='idealized_moist_rad',
    grid_file_paths=(
        ('/home/skc/archive/testing_2015_12_22/idealized_moist_rad/'
         'gfdl.ncrc2-default-repro/1x0m360d_32pe/history/'
         '00010101.atmos_1x20day.nc',
         '/home/skc/scratch_nbs/04-18-2016/imr.landmask.nc'),
    ),
    runs=[imr.control],
    default_runs=[imr.control],
)
