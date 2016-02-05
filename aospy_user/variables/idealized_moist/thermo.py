from aospy.var import Var
from aospy_user import calcs, units
from aospy_user.variables import temp, sphum, height_full

tdt_rad = Var(
    name='tdt_rad',
    alt_names=('allradp',),
    domain='atmos',
    description=('Heating rate due to radiation'),
    def_time=True,
    def_vert=True,
    def_lat=True,
    def_lon=True,
    units=units.K_s1
)

dse_im = Var(
    name='dse_im',
    domain='atmos',
    description=('Dry Static Energy'),
    variables=(temp, height_full, sphum),
    def_time=True,
    def_vert=True,
    def_lat=True,
    def_lon=True,
    func=calcs.idealized_moist.thermo.dse,
    units=units.J_kg1
)

mse_im = Var(
    name='mse_im',
    domain='atmos',
    description=('Moist Static Energy'),
    variables=(temp, height_full, sphum),
    def_time=True,
    def_vert=True,
    def_lat=True,
    def_lon=True,
    func=calcs.idealized_moist.thermo.mse,
    units=units.J_kg1
)
