"""Collection of aospy.Var objects for use in my research."""
from universal.dynamics_native import (
    height_half, height_full, ucomp, vcomp, u_ref, v_ref,
    omega, vort, divg, pv, esf
)

from universal.dynamics_computed import (
    msf, gz, aht, gms, vcomp_mb, alet,
    msf_at_500_hPa, mmc_mse_flux, msf_500_zeros, dmv_dx, dmv_dy, vcomp_stat
)

from universal.energy_native import (
    olr, olr_clr, lwdn_sfc, lwdn_sfc_clr, lwup_sfc, lwup_sfc_clr,
    swdn_sfc, swdn_sfc_clr, swup_sfc, swup_sfc_clr, swdn_toa, swdn_toa_clr,
    swup_toa, swup_toa_clr, alb_sfc, shflx
)

from universal.energy_computed import (
    Q_diff, Q_diff_sw, Q_diff_lw
)

from universal.pressure import (
    p, ps, bk, pk, dp, dp_sigma, pfull
)

from universal.thermo_native import (
    sphum, rh, rh_ref, temp, t_surf, tdt_conv,
    qdt_vdif, tdt_ls, tdt_lw, tdt_sw, tdt_lw_clr,
    tdt_sw_clr, tdt_vdif, ice_wat, liq_wat, mc, mc_full,
    mc_half, sst
)

from universal.thermo_computed import (
    dse, mse, mse_b, mse_lower_trop, vert_av_temp
)

from universal.water_native import (
    precip, prec_conv, prec_ls, evap, snow_conv, snow_ls,
    soil_liq, soil_moisture, high_cld_amt, low_cld_amt,
    mid_cld_amt, tot_cld_amt, cld_amt, wvp
)

from universal.water_computed import (
    p_minus_e
)

from idealized_moist.dynamics import (
    umse_vint, vmse_vint, omega_mse_vint, umse, vmse,
    omega_mse, aht_im, dmv_dx_im, dmv_dy_im, dmv_dx_v_im,
    dmv_dy_v_im
)

from idealized_moist.energy import (
    flux_t, flux_lhe, flux_ocean, Q_sfc_im, Q_toa_im,
    Q_diff_im, Q_diff_sw_im, Q_diff_lw_im
)

from idealized_moist.thermo import (
    tdt_rad, tdt_solar, dse_im, mse_im, mse_stat_im
)

from idealized_moist.water import (
    condensation_rain, convection_rain, precip_im, p_minus_e_im,
    cond_minus_e_im
)

from idealized_moist_rad.energy import (
    netrad_toa_imr, vert_int_tdt_rad_imr, vert_int_tdtlw_rad_imr,
    vert_int_tdtsw_rad_imr, Q_diff_imr, Q_sfc_imr, swnet_toa_imr,
    olr_imr,
    # energy_column_divg_adj_eddy, energy_horiz_advec_eta_upwind_adj_time_mean,
    # energy_column_vert_advec_as_resid_eta_time_mean,
    # energy_column_tendency_each_timestep, energy_column_divg_adj_time_mean,
    # energy_column_divg_adj, energy_column_divg
)

from idealized_moist_rad.dynamics import (
    aht_imr, alet_imr, alet_cond_imr, simple_aht_imr
)
