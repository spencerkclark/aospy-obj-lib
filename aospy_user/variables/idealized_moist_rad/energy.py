from aospy.var import Var
from aospy.constants import r_e
from aospy_user import calcs, units
from aospy_user.variables import (flux_lhe, flux_t, swdn_sfc,
                                  temp, height_full, sphum,
                                  ucomp, vcomp, condensation_rain,
                                  convection_rain, ps, dp, pk, bk)

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

swnet_toa_imr = Var(
    name='swnet_toa',
    domain='atmos',
    description=('Net shortwave heating'),
    variables=(swdn_sfc, vert_int_tdtsw_rad_imr),
    def_time=True,
    def_vert=False,
    def_lat=True,
    def_lon=True,
    func=calcs.idealized_moist_rad.energy.swnet_toa,
    units=units.W_m2
)

olr_imr = Var(
    name='olr',
    domain='atmos',
    description=('Outgoing longwave radiation'),
    variables=(swdn_sfc, vert_int_tdtsw_rad_imr, netrad_toa_imr),
    def_time=True,
    def_vert=False,
    def_lat=True,
    def_lon=True,
    func=calcs.idealized_moist_rad.energy.olr,
    units=units.W_m2
)

# SAH MSE budget variables
energy_column_divg_adj_eddy = Var(
    name='energy_column_divg_adj_eddy',
    domain='atmos',
    description='',
    variables=(temp, height_full, sphum, ucomp, vcomp, vert_int_tdt_rad_imr,
               flux_t, flux_lhe,
               condensation_rain, convection_rain, ps, dp, r_e.value),
    def_time=True,
    def_vert=False,
    def_lat=True,
    def_lon=True,
    func=calcs.sah_mse_budget.energy.energy_column_divg_adj_eddy,
    units=units.W_m2,
    colormap='RdBu'
)

energy_horiz_advec_eta_upwind_adj_time_mean = Var(
    name='energy_horiz_advec_eta_upwind_adj_time_mean',
    domain='atmos',
    variables=(temp, height_full, sphum, ucomp, vcomp, vert_int_tdt_rad_imr,
               flux_t, flux_lhe,
               condensation_rain, convection_rain, ps, dp, r_e.value, bk, pk),
    def_time=True,
    def_vert=True,
    def_lat=True,
    def_lon=True,
    func=calcs.sah_mse_budget.energy.energy_horiz_advec_eta_upwind_adj_time_mean,
    units=units.J_kg1_s1,
    colormap='RdBu'
)

energy_column_vert_advec_as_resid_eta_time_mean = Var(
    name='energy_column_vert_advec_as_resid_eta_time_mean',
    domain='atmos',
    description='',
    variables=(temp, height_full, sphum, ucomp, vcomp, vert_int_tdt_rad_imr,
               flux_t, flux_lhe,
               condensation_rain, convection_rain, ps, dp, r_e.value, bk, pk),
    def_time=True,
    def_vert=False,
    def_lat=True,
    def_lon=True,
    func=calcs.sah_mse_budget.energy.energy_column_vert_advec_as_resid_eta_time_mean,
    units=units.W_m2,
    colormap='RdBu'
)

energy_column_tendency_each_timestep = Var(
    name='energy_column_tendency_each_timestep',
    domain='atmos',
    description='Monthly time-tendency of column integrated energy.',
    variables=(temp, height_full, sphum, ucomp, vcomp, dp),
    def_time=True,
    def_vert=False,
    def_lat=True,
    def_lon=True,
    func=calcs.sah_mse_budget.energy.energy_column_tendency_each_timestep,
    units=units.W_m2,
    colormap='RdBu_r'
)

# TESTING
energy_column_divg_adj_time_mean = Var(
    name='energy_column_divg_adj_time_mean',
    domain='atmos',
    description='',
    variables=(temp, height_full, sphum, ucomp, vcomp, vert_int_tdt_rad_imr,
               flux_t, flux_lhe,
               condensation_rain, convection_rain, ps, dp, r_e.value),
    def_time=True,
    def_vert=False,
    def_lat=True,
    def_lon=True,
    func=calcs.sah_mse_budget.energy.energy_column_divg_adj_time_mean,
    units=units.W_m2,
    colormap='RdBu'
)

energy_column_divg_adj = Var(
    name='energy_column_divg_adj',
    domain='atmos',
    description='',
    variables=(temp, height_full, sphum, ucomp, vcomp, vert_int_tdt_rad_imr,
               flux_t, flux_lhe,
               condensation_rain, convection_rain, ps, dp, r_e.value),
    def_time=True,
    def_vert=False,
    def_lat=True,
    def_lon=True,
    func=calcs.sah_mse_budget.energy.energy_column_divg_adj,
    units=units.W_m2,
    colormap='RdBu'
)

energy_column_divg = Var(
    name='energy_column_divg',
    domain='atmos',
    description='',
    variables=(temp, height_full, sphum, ucomp, vcomp, dp, r_e.value),
    def_time=True,
    def_vert=False,
    def_lat=True,
    def_lon=True,
    func=calcs.sah_mse_budget.energy.energy_column_divg,
    units=units.W_m2,
    colormap='RdBu'
)
