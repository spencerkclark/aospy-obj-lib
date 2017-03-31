from aospy.var import Var
from aospy.constants import r_e
from aospy_user import calcs, units
from ..idealized_moist.energy import flux_lhe, flux_t
from ..universal.energy_native import swdn_sfc, lwdn_sfc
from ..universal.thermo_native import sphum, temp
from ..universal.dynamics_native import height_full, ucomp, vcomp
from ..idealized_moist.water import condensation_rain, convection_rain
from ..universal.pressure import ps, dp, pk, bk


netrad_toa = Var(
    name='netrad_toa',
    domain='atmos',
    description=('Net radiation at top of atmosphere'),
    def_time=True,
    def_vert=False,
    def_lon=True,
    def_lat=True,
    units=units.W_m2
)

vert_int_tdt_rad = Var(
    name='vert_int_tdt_rad',
    domain='atmos',
    description=('Vertically integrated heating rate'
                 ' due to all radiation'),
    def_time=True,
    def_vert=False,
    def_lat=True,
    def_lon=True,
    units=units.W_m2
)

vert_int_tdtsw_rad = Var(
    name='vert_int_tdtsw_rad',
    domain='atmos',
    description=('Vertically integrated heating rate '
                 'due to shortwave radiation'),
    def_time=True,
    def_vert=False,
    def_lat=True,
    def_lon=True,
    units=units.W_m2
)

vert_int_tdtlw_rad = Var(
    name='vert_int_tdtlw_rad',
    domain='atmos',
    description=('Vertically integrated heating rate '
                 'due to longwave radiation'),
    def_time=True,
    def_vert=False,
    def_lat=True,
    def_lon=True,
    units=units.W_m2
)

Q_sfc = Var(
    name='Q_sfc',
    domain='atmos',
    description=('Heat flux at the surface in idealized model.'),
    variables=(netrad_toa, vert_int_tdt_rad, flux_lhe, flux_t),
    def_time=True,
    def_vert=False,
    def_lat=True,
    def_lon=True,
    func=calcs.idealized_moist_rad.energy.Q_sfc,
    units=units.W_m2
)

Q_diff = Var(
    name='Q_diff',
    domain='atmos',
    description=('Net column heating'),
    variables=(vert_int_tdt_rad, flux_lhe, flux_t),
    def_time=True,
    def_vert=False,
    def_lat=True,
    def_lon=True,
    func=calcs.idealized_moist_rad.energy.Q_diff,
    units=units.W_m2
)

swnet_toa = Var(
    name='swnet_toa',
    domain='atmos',
    description=('Net shortwave heating'),
    variables=(swdn_sfc, vert_int_tdtsw_rad),
    def_time=True,
    def_vert=False,
    def_lat=True,
    def_lon=True,
    func=calcs.idealized_moist_rad.energy.swnet_toa,
    units=units.W_m2
)

olr = Var(
    name='olr',
    domain='atmos',
    description=('Outgoing longwave radiation'),
    variables=(swdn_sfc, vert_int_tdtsw_rad, netrad_toa),
    def_time=True,
    def_vert=False,
    def_lat=True,
    def_lon=True,
    func=calcs.idealized_moist_rad.energy.olr,
    units=units.W_m2
)

lwup_sfc = Var(
    name='lwup_sfc',
    domain='atmos',
    description=('Upward flux of longwave radiation at the surface.'),
    variables=(swdn_sfc, vert_int_tdtsw_rad, netrad_toa, lwdn_sfc,
               vert_int_tdtlw_rad),
    def_time=True,
    def_vert=False,
    def_lat=True,
    def_lon=True,
    func=calcs.idealized_moist_rad.energy.lwup_sfc,
    units=units.W_m2
)

# Diagnostics from radiation module itself.  Not valid.
# olr_diag_imr = Var(
#     name='olr_diag',
#     alt_names=('olr',),
#     domain='atmos',
#     description=('Outgoing longwave radiation diagnostic '
#                  'I am wary of this diagnostic and would like to test it out'),
#     def_time=True,
#     def_vert=False,
#     def_lat=True,
#     def_lon=True,
#     units=units.W_m2
# )

# lwdn_sfc_imr = Var(
#     name='lwdn_sfc_diag',
#     alt_names=('lwdn_sfc',),
#     domain='atmos',
#     description=('LW down surface diagnostic '
#                  'I am wary of this diagnostic and would like to test it out'),
#     def_time=True,
#     def_vert=False,
#     def_lat=True,
#     def_lon=True,
#     units=units.W_m2
# )

# lwup_sfc_imr = Var(
#     name='lwup_sfc_diag',
#     alt_names=('lwup_sfc',),
#     domain='atmos',
#     description=('LW up surface diagnostic '
#                  'I am wary of this diagnostic and would like to test it out'),
#     def_time=True,
#     def_vert=False,
#     def_lat=True,
#     def_lon=True,
#     units=units.W_m2
# )

# SAH MSE budget variables
# energy_column_divg_adj_eddy = Var(
#     name='energy_column_divg_adj_eddy',
#     domain='atmos',
#     description='',
#     variables=(temp, height_full, sphum, ucomp, vcomp, vert_int_tdt_rad_imr,
#                flux_t, flux_lhe,
#                condensation_rain, convection_rain, ps, dp, r_e.value),
#     def_time=True,
#     def_vert=False,
#     def_lat=True,
#     def_lon=True,
#     func=calcs.sah_mse_budget.energy.energy_column_divg_adj_eddy,
#     units=units.W_m2,
#     colormap='RdBu'
# )

# energy_horiz_advec_eta_upwind_adj_time_mean = Var(
#     name='energy_horiz_advec_eta_upwind_adj_time_mean',
#     domain='atmos',
#     variables=(temp, height_full, sphum, ucomp, vcomp, vert_int_tdt_rad_imr,
#                flux_t, flux_lhe,
#                condensation_rain, convection_rain, ps, dp, r_e.value, bk, pk),
#     def_time=True,
#     def_vert=True,
#     def_lat=True,
#     def_lon=True,
#     func=calcs.sah_mse_budget.energy.energy_horiz_advec_eta_upwind_adj_time_mean,
#     units=units.J_kg1_s1,
#     colormap='RdBu'
# )

# energy_column_vert_advec_as_resid_eta_time_mean = Var(
#     name='energy_column_vert_advec_as_resid_eta_time_mean',
#     domain='atmos',
#     description='',
#     variables=(temp, height_full, sphum, ucomp, vcomp, vert_int_tdt_rad_imr,
#                flux_t, flux_lhe,
#                condensation_rain, convection_rain, ps, dp, r_e.value, bk, pk),
#     def_time=True,
#     def_vert=False,
#     def_lat=True,
#     def_lon=True,
#     func=calcs.sah_mse_budget.energy.energy_column_vert_advec_as_resid_eta_time_mean,
#     units=units.W_m2,
#     colormap='RdBu'
# )

# energy_column_tendency_each_timestep = Var(
#     name='energy_column_tendency_each_timestep',
#     domain='atmos',
#     description='Monthly time-tendency of column integrated energy.',
#     variables=(temp, height_full, sphum, ucomp, vcomp, dp),
#     def_time=True,
#     def_vert=False,
#     def_lat=True,
#     def_lon=True,
#     func=calcs.sah_mse_budget.energy.energy_column_tendency_each_timestep,
#     units=units.W_m2,
#     colormap='RdBu_r'
# )

# # TESTING
# energy_column_divg_adj_time_mean = Var(
#     name='energy_column_divg_adj_time_mean',
#     domain='atmos',
#     description='',
#     variables=(temp, height_full, sphum, ucomp, vcomp, vert_int_tdt_rad_imr,
#                flux_t, flux_lhe,
#                condensation_rain, convection_rain, ps, dp, r_e.value),
#     def_time=True,
#     def_vert=False,
#     def_lat=True,
#     def_lon=True,
#     func=calcs.sah_mse_budget.energy.energy_column_divg_adj_time_mean,
#     units=units.W_m2,
#     colormap='RdBu'
# )

# energy_column_divg_adj = Var(
#     name='energy_column_divg_adj',
#     domain='atmos',
#     description='',
#     variables=(temp, height_full, sphum, ucomp, vcomp, vert_int_tdt_rad_imr,
#                flux_t, flux_lhe,
#                condensation_rain, convection_rain, ps, dp, r_e.value),
#     def_time=True,
#     def_vert=False,
#     def_lat=True,
#     def_lon=True,
#     func=calcs.sah_mse_budget.energy.energy_column_divg_adj,
#     units=units.W_m2,
#     colormap='RdBu'
# )

# energy_column_divg = Var(
#     name='energy_column_divg',
#     domain='atmos',
#     description='',
#     variables=(temp, height_full, sphum, ucomp, vcomp, dp, r_e.value),
#     def_time=True,
#     def_vert=False,
#     def_lat=True,
#     def_lon=True,
#     func=calcs.sah_mse_budget.energy.energy_column_divg,
#     units=units.W_m2,
#     colormap='RdBu'
# )
