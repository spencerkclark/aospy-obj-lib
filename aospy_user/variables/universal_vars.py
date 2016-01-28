"""Variables specific to the gray atmosphere idealized moist model."""
from aospy.var import Var
from aospy_user import calcs, units
from aospy_user.variables import (temp, sphum, height_full, swdn_sfc,
                                  olr, lwdn_sfc, lwup_sfc)

flux_t = Var(
    name='flux_t',
    units=units.W_m2,
    domain='atmos',
    description='Sensible heat flux in idealized moist model',
    def_time=True,
    def_vert=False,
    def_lat=True,
    def_lon=True,
    in_nc_grid=False
)
flux_lhe = Var(
    name='flux_lhe',
    units=units.W_m2,
    domain='atmos',
    description='Latent heat flux in idealized moist model',
    def_time=True,
    def_vert=False,
    def_lat=True,
    def_lon=False,
    in_nc_grid=False
)
dse_im = Var(
    name='dse_im',
    domain='atmos',
    description=('Dry Static Energy'),
    variables=(temp, height_full),
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
Q_sfc_im = Var(
    name='Q_sfc_im',
    domain='atmos',
    description=('Heat flux at the surface in idealized model.'),
    variables=(swdn_sfc, lwdn_sfc, lwup_sfc, flux_t, flux_lhe),
    def_time=True,
    def_vert=False,
    def_lat=True,
    def_lon=True,
    func=calcs.idealized_moist.energy.Q_sfc,
    units=units.W_m2
)
Q_toa_im = Var(
    name='Q_toa_im',
    domain='atmos',
    description=('Heat flux at the TOA in idealized model.'),
    variables=(swdn_sfc, olr),
    def_time=True,
    def_vert=False,
    def_lat=True,
    def_lon=True,
    func=calcs.idealized_moist.energy.Q_toa,
    units=units.W_m2
)
Q_diff_im = Var(
    name='Q_diff_im',
    domain='atmos',
    description=('Net column heating'),
    variables=(swdn_sfc, olr, lwdn_sfc, lwup_sfc, flux_t, flux_lhe),
    def_time=True,
    def_vert=False,
    def_lat=True,
    def_lon=True,
    func=calcs.idealized_moist.energy.Q_diff,
    units=units.W_m2
)
Q_diff_sw_im = Var(
    name='Q_diff_sw_im',
    domain='atmos',
    description=('Net shortwave heating of atmosphere.'),
    variables=(swdn_sfc),
    def_time=True,
    def_vert=False,
    def_lat=True,
    def_lon=True,
    func=calcs.idealized_moist.energy.Q_diff_sw,
    units=units.W_m2
)
Q_diff_lw_im = Var(
    name='Q_diff_lw_im',
    domain='atmos',
    description=('Net longwave radiation heating of atmosphere.'),
    variables=(olr, lwdn_sfc, lwup_sfc),
    def_time=True,
    def_vert=False,
    def_lat=True,
    def_lon=True,
    func=calcs.idealized_moist.energy.Q_diff_lw,
    units=units.W_m2
)
