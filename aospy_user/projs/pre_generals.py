from aospy.proj import Proj
from aospy_user import regions
import aospy_user.models.models_aospy_beta as models

# itcz = Proj(
#     'itcz',
#     models=(
#         models.am2,
#         models.am2_reyoi,
#         models.dargan_T42,
#         models.dargan,
#         models.idealized_moist_rad
#         ),
#     regions=(regions.globe,
#              regions.nh),
#     direc_out='/work/Spencer.Clark',
#     tar_direc_out='/archive/Spencer.Clark'
# )

# dargan_test = Proj(
#     'dargan_test',
#     direc_out='/archive/skc/d_test/',
# #    nc_dir_struc='one_dir',
#     models=(
#         models.dargan,
#         models.dargan_T42,
#         ),
#     regions=(regions.globe,)
# )

test = Proj(
    'test',
    models=(
        models.am2,
        models.idealized_moist_rad,
        ),
    regions=(regions.globe,
             regions.nh),
    direc_out='/work/Spencer.Clark/aospy-beta',
    tar_direc_out='/archive/Spencer.Clark/aospy-beta'
)
