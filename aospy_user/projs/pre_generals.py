from aospy.proj import Proj
from aospy_user import regions
import aospy_user.models.models as models

itcz = Proj(
    'itcz',
    direc_out='/archive/skc/itcz/',
    models=(
        models.am2,
        models.am2_reyoi,
        models.dargan_T42,
        models.dargan,
        models.idealized_moist_rad
        ),
    regions=(regions.globe,
             regions.nh)
)

dargan_test = Proj(
    'dargan_test',
    direc_out='/archive/skc/d_test/',
#    nc_dir_struc='one_dir',
    models=(
        models.dargan,
        models.dargan_T42,
        ),
    regions=(regions.globe,)
)
