from aospy.var import Var
from aospy_user import calcs, units
from aospy_user.variables.universal.pressure import dp, p
from aospy_user.variables.universal.thermo_native import (temp,
                                                          sphum)


# Computed variables
dse = Var(
    name='dse',
    domain='atmos',
    description=('Dry Static Energy'),
    variables=(temp, sphum, dp, p),
    def_time=True,
    def_vert=True,
    def_lat=True,
    def_lon=True,
    func=calcs.dse,
    units=units.J_kg1
)
mse = Var(
    name='mse',
    domain='atmos',
    description=('Moist Static Energy'),
    variables=(temp, sphum, dp, p),
    def_time=True,
    def_vert=True,
    def_lat=True,
    def_lon=True,
    func=calcs.mse,
    units=units.J_kg1
)
hb = Var(
    name='hb',
    domain='atmos',
    description=('Average moist static energy 20 to 40 hPa from sfc.'),
    variables=(temp, sphum, dp, p),
    def_time=True,
    def_vert=False,
    def_lat=True,
    def_lon=True,
    units=units.J_kg1,
    func=calcs.hb
)
h_lower_trop = Var(
    name='h_lower_trop',
    domain='atmos',
    description=('Average moist static energy 20 to 500 hPa from sfc.'),
    variables=(temp, sphum, dp, p),
    def_time=True,
    def_vert=False,
    def_lat=True,
    def_lon=True,
    units=units.J_kg1,
    func=calcs.h_lower_trop
)
