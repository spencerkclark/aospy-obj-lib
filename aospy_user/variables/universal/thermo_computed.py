from aospy.var import Var
from aospy_user import calcs, units
from .pressure import dp, p
from .thermo_native import temp, sphum


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
    func=calcs.universal.thermo.dse,
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
    func=calcs.universal.thermo.mse,
    units=units.J_kg1
)

mse_b = Var(
    name='mse_b',
    domain='atmos',
    description=('Average moist static energy 20 to 40 hPa from sfc.'),
    variables=(temp, sphum, dp, p),
    def_time=True,
    def_vert=False,
    def_lat=True,
    def_lon=True,
    units=units.J_kg1,
    func=calcs.universal.thermo.mse_b
)

mse_lower_trop = Var(
    name='mse_lower_trop',
    domain='atmos',
    description=('Average moist static energy 20 to 500 hPa from sfc.'),
    variables=(temp, sphum, dp, p),
    def_time=True,
    def_vert=False,
    def_lat=True,
    def_lon=True,
    units=units.J_kg1,
    func=calcs.universal.thermo.mse_lower_trop
)

vert_av_temp = Var(
    name='vert_av_temp',
    domain='atmos',
    description=('Vertical, mass-weighted integral of temperature.'),
    variables=(temp, dp),
    def_time=True,
    def_vert=False,
    def_lat=True,
    def_lon=True,
    units=units.K,
    func=calcs.universal.thermo.vert_av_temp
)

potential_temp = Var(
    name='potential_temp',
    domain='atmos',
    description=('Potential temperature'),
    variables=(temp, p),
    def_time=True,
    def_vert=True,
    def_lat=True,
    def_lon=True,
    units=units.K,
    func=calcs.universal.thermo.potential_temp
)

equiv_potential_temp = Var(
    name='equiv_potential_temp',
    domain='atmos',
    description=('Equivalent potential temperature'),
    variables=(temp, p, sphum),
    def_time=True,
    def_vert=True,
    def_lat=True,
    def_lon=True,
    units=units.K,
    func=calcs.universal.thermo.equiv_potential_temp
)
