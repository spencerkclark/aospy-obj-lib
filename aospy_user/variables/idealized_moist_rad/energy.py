from aospy.var import Var
from aospy_user import calcs, units

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
# Q_sfc_imr = Var(
#     name='Q_sfc_im',
#     domain='atmos',
#     description=('Heat flux at the surface in idealized model.'),
#     variables=(swdn_sfc, lwdn_sfc, lwup_sfc, flux_t, flux_lhe),
#     def_time=True,
#     def_vert=False,
#     def_lat=True,
#     def_lon=True,
#     func=calcs.idealized_moist.energy.Q_sfc,
#     units=units.W_m2
# )
# Q_toa_imr = Var(
#     name='Q_toa_im',
#     domain='atmos',
#     description=('Heat flux at the TOA in idealized model.'),
#     variables=(swdn_sfc, olr),
#     def_time=True,
#     def_vert=False,
#     def_lat=True,
#     def_lon=True,
#     func=calcs.idealized_moist.energy.Q_toa,
#     units=units.W_m2
# )
# Q_diff_imr = Var(
#     name='Q_diff_im',
#     domain='atmos',
#     description=('Net column heating'),
#     variables=(swdn_sfc, olr, lwdn_sfc, lwup_sfc, flux_t, flux_lhe),
#     def_time=True,
#     def_vert=False,
#     def_lat=True,
#     def_lon=True,
#     func=calcs.idealized_moist.energy.Q_diff,
#     units=units.W_m2
# )
# Q_diff_sw_imr = Var(
#     name='Q_diff_sw_im',
#     domain='atmos',
#     description=('Net shortwave heating of atmosphere.'),
#     variables=(swdn_sfc),
#     def_time=True,
#     def_vert=False,
#     def_lat=True,
#     def_lon=True,
#     func=calcs.idealized_moist.energy.Q_diff_sw,
#     units=units.W_m2
# )
# Q_diff_lw_imr = Var(
#     name='Q_diff_lw_im',
#     domain='atmos',
#     description=('Net longwave radiation heating of atmosphere.'),
#     variables=(olr, lwdn_sfc, lwup_sfc),
#     def_time=True,
#     def_vert=False,
#     def_lat=True,
#     def_lon=True,
#     func=calcs.idealized_moist.energy.Q_diff_lw,
#     units=units.W_m2
# )
