from aospy.proj import Proj
from aospy_user import regions, models, variables

am2_2009_yim = Proj(
    'am2_2009_yim',
    vars=variables.master_vars_list,
    direc_out='/archive/skc/am2_2009_sandbox/',
    nc_dir_struc='gfdl',
    models=(
        models.am2,
        ),
    regions=(regions.globe,)
)

dargan_test = Proj(
    'dargan_test',
    vars=variables.master_vars_list,
    direc_out='/archive/skc/d_test/',
    nc_dir_struc='one_dir',
    models=(
        models.dargan,
        ),
    regions=(regions.globe,)
)
