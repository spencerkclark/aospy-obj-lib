from aospy.var import Var
from aospy_user import calcs, units
from ..universal.dynamics_native import height_full
from ..universal.thermo_native import temp, sphum


tdt_rad = Var(
    name='tdt_rad',
    alt_names=('allradp', 'dt_tg_rad'),
    domain='atmos',
    description=('Heating rate due to radiation'),
    def_time=True,
    def_vert=True,
    def_lat=True,
    def_lon=True,
    units=units.K_s1
)

tdt_solar = Var(
    name='tdt_solar',
    alt_names=('tdt_sw',),
    domain='atmos',
    description=('Heating rate due to solar radiation'),
    def_time=True,
    def_vert=True,
    def_lat=True,
    def_lon=True,
    units=units.K_s1
)

dse = Var(
    name='dse',
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

mse = Var(
    name='mse',
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

mse_stat = Var(
    name='mse_stat',
    domain='atmos',
    description=('Moist Static Energy'),
    variables=(temp, height_full, sphum),
    def_time=True,
    def_vert=True,
    def_lat=True,
    def_lon=True,
    func=calcs.idealized_moist.thermo.mse_stat,
    units=units.J_kg1
)
