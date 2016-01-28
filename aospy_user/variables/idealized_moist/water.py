from aospy.var import Var
from aospy_user import calcs, units


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
precip_im = Var(
    name='precip_im',
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
