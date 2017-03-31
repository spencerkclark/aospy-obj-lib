from aospy.var import Var
from aospy_user import calcs, units
from .energy import flux_lhe


condensation_rain = Var(
    name='condensation_rain',
    domain='atmos',
    description=('condensation rain in idealized moist model'),
    def_time=True,
    def_vert=False,
    def_lat=True,
    def_lon=True,
    units=units.kg_m2_s1
)

convection_rain = Var(
    name='convection_rain',
    domain='atmos',
    description=('convection rain in idealized moist model'),
    def_time=True,
    def_vert=False,
    def_lat=True,
    def_lon=True,
    units=units.kg_m2_s1
)

precip = Var(
    name='precip',
    domain='atmos',
    description=('Total precipitation rate (convective + condensation'),
    variables=(condensation_rain, convection_rain),
    def_time=True,
    def_vert=False,
    def_lat=True,
    def_lon=True,
    func=calcs.idealized_moist.water.precip,
    units=units.kg_m2_s1
)

evap = Var(
    name='evap',
    domain='atmos',
    description=('Total evaporation rate in idealized moist model'),
    variables=(flux_lhe,),
    def_time=True,
    def_vert=False,
    def_lat=True,
    def_lon=True,
    func=calcs.idealized_moist.water.evap,
    units=units.kg_m2_s1
)

p_minus_e = Var(
    name='p_minus_e',
    domain='atmos',
    description=('P-E in idealized moist model'),
    variables=(condensation_rain, convection_rain, flux_lhe,),
    def_time=True,
    def_vert=False,
    def_lat=True,
    def_lon=True,
    func=calcs.idealized_moist.water.p_minus_e,
    units=units.kg_m2_s1
)

cond_minus_e = Var(
    name='cond_minus_e',
    domain='atmos',
    description=('Condensation Rain-E in idealized moist model'),
    variables=(condensation_rain, flux_lhe,),
    def_time=True,
    def_vert=False,
    def_lat=True,
    def_lon=True,
    func=calcs.idealized_moist.water.cond_minus_e,
    units=units.kg_m2_s1
)
