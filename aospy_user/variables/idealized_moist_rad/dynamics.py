from aospy import Var
from aospy_user import calcs, units
from ..idealized_moist.water import condensation_rain, convection_rain
from ..idealized_moist.energy import flux_t, flux_lhe
from .energy import vert_int_tdt_rad, netrad_toa


# Computed variables
aht = Var(
    name='aht',
    domain='atmos',
    description=('atmospheric heat transport'),
    variables=(vert_int_tdt_rad, flux_lhe, flux_t),
    def_time=True,
    def_vert=False,
    def_lat=True,
    def_lon=False,
    func=calcs.idealized_moist_rad.energy.aht,
    units=units.W
)

simple_aht = Var(
    name='simple_aht',
    domain='atmos',
    description=('atmospheric heat transport'),
    variables=(netrad_toa,),
    def_time=True,
    def_vert=False,
    def_lat=True,
    def_lon=False,
    func=calcs.idealized_moist_rad.energy.aht_simple,
    units=units.W
)

alet = Var(
    name='alet',
    domain='atmos',
    description=('atmospheric latent energy transport'),
    variables=(condensation_rain, convection_rain, flux_lhe),
    def_time=True,
    def_vert=False,
    def_lat=True,
    def_lon=False,
    func=calcs.idealized_moist_rad.energy.alet,
    units=units.W
)

alet_cond = Var(
    name='alet_cond',
    domain='atmos',
    description=('atmospheric latent energy transport'
                 '-- only condensation_rain'),
    variables=(condensation_rain, 0.0, flux_lhe),
    def_time=True,
    def_vert=False,
    def_lat=True,
    def_lon=False,
    func=calcs.idealized_moist_rad.energy.alet,
    units=units.W
)
