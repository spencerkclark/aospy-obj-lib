from aospy.var import Var
from aospy_user import units, calcs
from .water_native import precip, evap


p_minus_e = Var(
    name='p_minus_e',
    variables=(precip, evap),
    units=units.kg_m2_s1,
    domain='atmos',
    description='Precipitation minus evaporation',
    def_time=True,
    def_vert=False,
    def_lat=True,
    def_lon=True,
    func=calcs.universal.water.p_minus_e,
)
