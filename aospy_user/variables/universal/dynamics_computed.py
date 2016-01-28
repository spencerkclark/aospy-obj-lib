from aospy.var import Var
from aospy_user import calcs, units
from aospy_user.variables.universal.pressure import dp, p
from aospy_user.variables.universal.thermo_native import temp, sphum
from aospy_user.variables.universal.energy_native import (swdn_toa,
                                                          swup_toa, olr,
                                                          lwup_sfc, lwdn_sfc,
                                                          swup_sfc,
                                                          swdn_sfc, shflx)
from aospy_user.variables.universal.water_native import evap
from aospy_user.variables.universal.dynamics_native import ucomp, vcomp


# Computed variables
msf = Var(
    name='msf',
    domain='atmos',
    description=('Eulerian meridional mass streamfunction'),
    variables=(vcomp, dp),
    def_time=True,
    def_vert=True,
    def_lat=True,
    def_lon=False,
    func=calcs.msf,
    units=units.kg_s1
)
gz = Var(
    name='gz',
    domain='atmos',
    description=('Atmospheric Geopotential'),
    variables=(temp, sphum, dp, p),
    def_time=True,
    def_vert=True,
    def_lat=True,
    def_lon=True,
    func=calcs.gz,
    units=units.J_kg1
)
aht = Var(
    name='aht',
    domain='atmos',
    description=('Meridional total atmospheric heat transport.'),
    variables=(swdn_toa, olr, swup_toa, swdn_sfc, lwdn_sfc, swup_sfc,
               lwup_sfc, shflx, evap),
    def_time=True,
    def_vert=False,
    def_lat=True,
    def_lon=True,
    func=calcs.aht_gcm,
    units=units.W
)
gms = Var(
    name='gms',
    domain='atmos',
    description=('Gross Moist Stability as defined in SH 2015.'),
    variables=(temp, sphum, vcomp, dp, p),
    def_time=True,
    def_vert=False,
    def_lat=True,
    def_lon=False,
    func=calcs.gms,
    units=units.K
)
vcomp_mb = Var(
    name='vcomp_mb',
    domain='atmos',
    description=('vcomp mass balance'),
    variables=(vcomp, dp),
    def_time=True,
    def_vert=True,
    def_lat=True,
    def_lon=False,
    func=calcs.correct_vcomp,
    units=units.m_s1,
)
# Continue supporting below?
msf_at_500_hPa = Var(
    name='msf_500',
    domain='atmos',
    description=('Eulerian meridional mass streamfunction'
                 'evaluated at 500 hPa'),
    variables=(vcomp, dp, p),
    def_time=False,
    def_vert=False,
    def_lat=True,
    def_lon=False,
    func=calcs.msf_at_500_hPa,
    units=units.kg_s1
)
mmc_mse_flux = Var(
    name='msef_mmc',
    domain='atmos',
    description=('Mean meridional circulation component of'
                 'the moist static energy flux.'),
    variables=(temp, sphum, vcomp, dp, p),
    def_time=True,
    def_vert=False,
    def_lat=True,
    def_lon=False,
    func=calcs.mmc_mse_flux,
    units=units.W
)
msf_500_zeros = Var(
    name='msf_500_zeros',
    domain='atmos',
    description=('Zeros of the 500 hPa streamfunction'),
    variables=(vcomp, dp, p),
    def_time=False,
    def_vert=False,
    def_lat=True,
    def_lon=False,
    func=calcs.msf_500_zeros,
    units=units.latlon
)
dmv_dx = Var(
    name='dmv_dx',
    domain='atmos',
    description=('Zonal flux divergence of mse.'),
    variables=(ucomp, temp, sphum, dp, p),
    def_time=True,
    def_vert=True,
    def_lat=True,
    def_lon=True,
    func=calcs.mse_zonal_flux_divg,
    units=units.W
)
dmv_dy = Var(
    name='dmv_dy',
    domain='atmos',
    description=('Meridional flux divergence of mse.'),
    variables=(vcomp, temp, sphum, dp, p),
    def_time=True,
    def_vert=True,
    def_lat=True,
    def_lon=True,
    func=calcs.mse_merid_flux_divg,
    units=units.W
)
