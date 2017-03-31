from aospy.var import Var
from aospy_user import calcs, units
from aospy_user.variables import swdn_sfc, lwdn_sfc, lwup_sfc, olr


flux_t = Var(
    name='flux_t',
    units=units.W_m2,
    domain='atmos',
    description='Sensible heat flux in idealized moist model',
    def_time=True,
    def_vert=False,
    def_lat=True,
    def_lon=True
)
flux_lhe = Var(
    name='flux_lhe',
    units=units.W_m2,
    domain='atmos',
    description='Latent heat flux in idealized moist model',
    def_time=True,
    def_vert=False,
    def_lat=True,
    def_lon=False
)
flux_ocean = Var(
    name='flux_oceanq',
    units=units.W_m2,
    domain='atmos',
    description='Ocean heat flux in idealized moist model',
    def_time=True,
    def_vert=False,
    def_lat=True,
    def_lon=False
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

insolation = Var(
    name='insolation',
    units=units.W_m2,
    domain='atmos',
    description='Raw solar insolation used in model',
    def_time=True,
    def_vert=False,
    def_lat=True,
    def_lon=True
)

net_lw_surf = Var(
    name='net_lw_surf',
    units=units.W_m2,
    domain='atmos',
    description='Net LW radiation at the surface',
    def_time=True,
    def_vert=False,
    def_lat=True,
    def_lon=True
)

lwup_sfc_im = Var(
    name='lwup_sfc',
    domain='atmos',
    description=('Upward flux of longwave radiation at the surface.'),
    variables=(net_lw_surf, lwdn_sfc),
    def_time=True,
    def_vert=False,
    def_lat=True,
    def_lon=True,
    func=calcs.idealized_moist.energy.lwup_sfc,
    units=units.W_m2
)

