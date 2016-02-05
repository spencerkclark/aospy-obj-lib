from aospy.var import Var
from aospy_user import calcs, units
from aospy_user.variables import flux_lhe, flux_t

netrad_toa_imr = Var(
    name='netrad_toa',
    domain='atmos',
    description=('Net radiation at top of atmosphere'),
    def_time=True,
    def_vert=False,
    def_lon=True,
    def_lat=True,
    units=units.W_m2
)

vert_int_tdt_rad_imr = Var(
    name='vert_int_tdt_rad',
    domain='atmos',
    description=('Vertically integrated heating rate'
                 ' due to all radiation'),
    def_time=True,
    def_vert=True,
    def_lat=True,
    def_lon=True,
    units=units.W_m2
)

vert_int_tdtsw_rad_imr = Var(
    name='vert_int_tdtsw_rad',
    domain='atmos',
    description=('Vertically integrated heating rate '
                 'due to shortwave radiation'),
    def_time=True,
    def_vert=True,
    def_lat=True,
    def_lon=True,
    units=units.W_m2
)

vert_int_tdtlw_rad_imr = Var(
    name='vert_int_tdtlw_rad',
    domain='atmos',
    description=('Vertically integrated heating rate '
                 'due to longwave radiation'),
    def_time=True,
    def_vert=True,
    def_lat=True,
    def_lon=True,
    units=units.W_m2
)

Q_sfc_imr = Var(
    name='Q_sfc_imr',
    domain='atmos',
    description=('Heat flux at the surface in idealized model.'),
    variables=(netrad_toa_imr, vert_int_tdt_rad_imr, flux_lhe, flux_t),
    def_time=True,
    def_vert=False,
    def_lat=True,
    def_lon=True,
    func=calcs.idealized_moist_rad.energy.Q_sfc,
    units=units.W_m2
)

Q_diff_imr = Var(
    name='Q_diff_imr',
    domain='atmos',
    description=('Net column heating'),
    variables=(vert_int_tdt_rad_imr, flux_lhe, flux_t),
    def_time=True,
    def_vert=False,
    def_lat=True,
    def_lon=True,
    func=calcs.idealized_moist_rad.energy.Q_diff,
    units=units.W_m2
)
