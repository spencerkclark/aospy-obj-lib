from aospy.proj import Proj
from aospy_user import regions
import aospy_user.models.models as models

itcz = Proj(
    'itcz',
    models=(
        models.idealized_moist_rad,
    ),
    regions=(regions.globe,
             regions.nh),
    direc_out='/work/Spencer.Clark/aospy-v0.1',
    tar_direc_out='/archive/Spencer.Clark/aospy-v0.1'
)

# test = Proj(
#     'test',
#     models=(
#         models.am2,
#         models.idealized_moist_rad,
#         ),
#     regions=(regions.globe,
#              regions.nh),
#     direc_out='/work/Spencer.Clark/aospy-beta',
#     tar_direc_out='/archive/Spencer.Clark/aospy-beta'
# )
