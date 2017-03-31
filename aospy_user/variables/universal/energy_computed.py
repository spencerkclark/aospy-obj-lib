from aospy.var import Var
from aospy_user import calcs, units
from .energy_native import (swdn_toa, olr, swup_toa, swdn_sfc, lwdn_sfc,
                            swup_sfc, lwup_sfc, shflx)
from .water_native import evap


# Computed variables
Q_diff = Var(
    name='Q_diff',
    domain='atmos',
    description=('Net column heating'),
    variables=(swdn_toa, olr, swup_toa, swdn_sfc, lwdn_sfc, swup_sfc,
               lwup_sfc, shflx, evap),
    def_time=True,
    def_vert=False,
    def_lat=True,
    def_lon=True,
    func=calcs.universal.energy.Q_diff,
    units=units.W_m2
)

Q_diff_sw = Var(
    name='Q_diff_sw',
    domain='atmos',
    description=('Net shortwave radiation.'),
    variables=(swdn_toa, swup_toa, swdn_sfc, swup_sfc),
    def_time=True,
    def_vert=False,
    def_lat=True,
    def_lon=True,
    func=calcs.universal.energy.Q_diff_sw,
    units=units.W_m2
)

Q_diff_lw = Var(
    name='Q_diff_lw',
    domain='atmos',
    description=('Net longwave radiation.'),
    variables=(olr, lwdn_sfc, lwup_sfc),
    def_time=True,
    def_vert=False,
    def_lat=True,
    def_lon=True,
    func=calcs.universal.energy.Q_diff_lw,
    units=units.W_m2
)
