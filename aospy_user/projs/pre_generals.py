from aospy.proj import Proj
from aospy_user import regions, variables
import aospy_user.models.models as models

itcz = Proj(
    'itcz',
    vars=variables.master_vars_list,
    direc_out='/archive/skc/itcz/',
    models=(
        models.am2,
        models.am2_reyoi,
        models.dargan_T42,
        models.dargan
        ),
    regions=(regions.globe,)
)

dargan_test = Proj(
    'dargan_test',
    vars=variables.master_vars_list,
    direc_out='/archive/skc/d_test/',
#    nc_dir_struc='one_dir',
    models=(
        models.dargan,
        models.dargan_T42,
        ),
    regions=(regions.globe,)
)
