from aospy import Var
from aospy_user import calcs, units
from aospy_user.variables import vert_int_tdt_rad_imr, flux_t, flux_lhe


# Computed variables
aht_imr = Var(
    name='aht_imr',
    domain='atmos',
    description=('atmospheric heat transport'),
    variables=(vert_int_tdt_rad_imr, flux_lhe, flux_t),
    def_time=True,
    def_vert=False,
    def_lat=True,
    def_lon=False,
    func=calcs.idealized_moist_rad.energy.aht,
    units=units.W
)
