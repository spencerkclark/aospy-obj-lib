from aospy import Var
from aospy_user import calcs, units
from aospy_user.variables import (vert_int_tdt_rad_imr, flux_t, flux_lhe,
                                  netrad_toa_imr, condensation_rain,
                                  convection_rain)


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

simple_aht_imr = Var(
    name='simple_aht_imr',
    domain='atmos',
    description=('atmospheric heat transport'),
    variables=(netrad_toa_imr,),
    def_time=True,
    def_vert=False,
    def_lat=True,
    def_lon=False,
    func=calcs.idealized_moist_rad.energy.aht_simple,
    units=units.W
)

alet_imr = Var(
    name='alet_imr',
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

alet_cond_imr = Var(
    name='alet_cond_imr',
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
