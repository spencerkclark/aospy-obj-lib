#! /usr/bin/env python
"""Main script for automating computations using aospy."""
import aospy_user

conv_off = ['conv_off',
            'asym_e5_conv_off', 'asym_t5_conv_off', 'asym_e15_conv_off',
            'asym_t15_conv_off', 'asym_e18_conv_off', 'asym_t18_conv_off']
conv_off_fixed_h2o = ['asym_e5_conv_off_fixed_h2o',
                      'asym_t5_conv_off_fixed_h2o',
                      'asym_e15_conv_off_fixed_h2o',
                      'asym_t15_conv_off_fixed_h2o',
                      'asym_e18_conv_off_fixed_h2o',
                      'asym_t18_conv_off_fixed_h2o', 'fixed_h2o_conv_off']
asym = ['asym_e5', 'asym_e15', 'asym_e18', 'asym_t5',
        'asym_t15', 'asym_t18', 'asym_t20']
eq = ['eq_5', 'eq_6', 'eq_7', 'eq_8', 'eq_15', 'eq_25', 'eq_35']
fixed_h2o = ['asym_e5_fixed_h2o','asym_t5_fixed_h2o',
             'asym_e15_fixed_h2o', 'asym_t15_fixed_h2o',
             'asym_e18_fixed_h2o', 'asym_t18_fixed_h2o']
#fixed_h2o = ['asym_t15_fixed_h2o', 'asym_e15_fixed_h2o']
control = ['control']
net_zero_solar = ['asym_e15_net_zero_solar', 'asym_t15_net_zero_solar']

land = ['umld_fr_earth_land', 'umld_gr_earth_land',
        'vmld_fr_earth_land', 'vmld_gr_earth_land',
        'umld_fr_earth_land_conv_off', 'umld_gr_earth_land_conv_off',
        'vmld_fr_earth_land_conv_off', 'vmld_gr_earth_land_conv_off']

gray_land = [r for r in land if 'gr' in r]
gray_land_conv = ['umld_gr_earth_land', 'vmld_gr_earth_land']


mp = aospy_user.MainParams()
mp.proj = 'itcz'
#    mp.proj = 'dargan_test'
#mp.model = ['am2']
#mp.model = ['dargan_T42']
mp.model = ['idealized_moist_rad']
#    mp.model = ['am2_reyoi']
#    mp.model = ['dargan']
#mp.run = [('am2_control','am2_tropics', 'am2_extratropics','am2_tropics+extratropics')]
#mp.run = [('imr_control', 'imr_fixed_h2o_symm', 'imr_rad_passive_h2o',
#           'imr_2xCO2', 'imr_fixed_h2o_2xCO2')]
#mp.run = [('imr_fixed_h2o_symm', 'imr_rad_passive_h2o',
#           'imr_2xCO2', 'imr_fixed_h2o_2xCO2')]
#mp.run = [('control', '2xCO2', 'fixed_h2o',
#           'fixed_h2o_2xCO2', 'asym_e5', 'asym_t5', 'asym_e15',
#           'asym_t15', 'asym_t20', 'conv_off')]
#mp.run = [('control', 'asym_e5', 'asym_e15', 'asym_e18', 'asym_t5', 'asym_t15',
#           'asym_t18', 'asym_t20', 'asym_e5_conv_off', 'asym_t5_conv_off')]

#mp.run = conv_off + asym + eq + fixed_h2o
#mp.run = fixed_h2o
#mp.run = net_zero_solar
#mp.run = conv_off + conv_off_fixed_h2o
#mp.run = ['control']
#mp.run = ['control', 'conv_off', 'fixed_h2o']
#mp.run = conv_off_fixed_h2o
#mp.run = ['control', 'fixed_h2o']# 'conv_off', 'fixed_h2o_conv_off']
#mp.run = ['asym_e15', 'asym_t15', 'asym_e15_fixed_h2o', 'asym_t15_fixed_h2o']
#mp.run = fixed_h2o + asym + conv_off + conv_off_fixed_h2o
#mp.run = ['control'] #, 'fixed_h2o']
#mp.run = ['asym_t15_fixed_h2o', 'asym_e15_fixed_h2o']
#mp.run = ['earth_land_seasons_mld']
#mp.run = gray_land_conv
mp.run = [r for r in land if 'conv' in r]
mp.run = ['fixed_h2o']
#mp.run = land
#mp.run = ['control']
#mp.run = asym + conv_off + conv_off_fixed_h2o + fixed_h2o
#mp.run = ['asym_e15_fixed_h2o', 'asym_t15_fixed_h2o']
#mp.run = ['asym_t5_conv_off', 'asym_e5_conv_off', 'asym_e15_conv_off', 'asym_e18_conv_off']
#mp.run = ['asym_e18_conv_off']
#mp.run = ['control']
#mp.run = [('eq_5', 'eq_6', 'eq_7', 'eq_8', 'eq_15', 'eq_25', 'eq_35')]
#mp.run = [('legendre_1', 'legendre_2', 'legendre_3')]
#mp.run = ['control']
#mp.run = [('control_gaussian_T42')]
#mp.run = [('control_gaussian_T42',
#          'tropics_gaussian_5.0_T42',
#          'extratropics_gaussian_5.0_T42',
#          'tropics_gaussian_15.0_T42',
#          'extratropics_gaussian_15.0_T42',
#          'tropics_gaussian_25.0_T42',
#          'extratropics_gaussian_25.0_T42')]
#    mp.run = [('am2_HadISST_control', 'am2_reyoi_extratropics_sp_SI', 'am2_reyoi_tropics_sp_SI')]
#    mp.run = ['control_T85']
#    mp.run = ['control_alb_T42']
mp.ens_mem = [False]
#    mp.var = ['Q_diff']
#    mp.var = ['mse']
#    mp.var = ['msf']
#    mp.var = ['mse']
#    mp.var = ['precip', 't_surf', 'Q_diff', 'ucomp', 'vcomp', 'mse']
#    mp.var = ['dp_sigma', 'ucomp', 'vcomp', 'mse']
#    mp.var = ['net_sw']
#mp.var = ['tdt_sw', 'tdt_lw', 'tdt_rad'] # 'tdt_vdif', 'qdt_vdif']#, 'vcomp_mb', 'mse']
#mp.var = ['mse_im', 'aht_im', 'condensation_rain', 'convection_rain', 'precip_im',
#          'p_minus_e_im', 'dp_sigma', 'dse_im', 'flux_lhe', 'flux_t', 'msf', 'omega',
#          'sphum', 'tdt_rad', 'temp', 't_surf', 'ucomp', 'vcomp', 'vcomp_mb']
#mp.var = ['msf', 'temp']
#    mp.var = ['aht', 'msf', 'olr', 'swdn_toa', 'swdn_sfc', 'lwdn_sfc', 'mse',
#              'precip_im']
#mp.var = ['temp', 'sphum', 'flux_t', 'flux_lhe', 'ucomp', 'vcomp', 't_surf',
#          'mse_im', 'netrad_toa_imr', 'condensation_rain',
#          'vert_int_tdt_rad_imr',
#          'vert_int_tdtsw_rad_imr', 'vert_int_tdtlw_rad_imr', 'aht_imr',
#          'Q_diff_imr', 'msf', 'omega']
#mp.var = ['aht_imr', 't_surf', 'dp_sigma', 'mse_im',
#          'condensation_rain', 'ucomp', 'vcomp', 'vert_int_tdtlw_rad_imr',
#          'vert_int_tdtsw_rad_imr', 'vert_int_tdt_rad_imr', 'flux_lhe',
#          'msf', 'sphum', 'flux_t', 'netrad_toa_imr', 'temp',
#          'lwdn_sfc', 'swdn_sfc', 'omega', 'Q_diff_imr', 'olr_imr',
#          'alet_cond_imr', 'cond_minus_e_im']
#mp.var = ['msf', 'precip_im', 'omega', 'aht_imr', 'p_minus_e_im',
#          'Q_diff_imr', 'alet_imr', 't_surf']
#mp.var = ['olr_imr', 'vert_av_temp']
#mp.var = ['rh']
mp.var = ['Q_diff_imr', 'olr_imr']
#mp.var = ['omega', 'mse_im']
#mp.var = ['condensation_rain']
#mp.var = ['olr_imr', 'swnet_toa_imr', 'vert_av_temp']
#mp.var = ['energy_horiz_advec_eta_upwind_adj_time_mean']  # an101
#mp.var = ['energy_column_divg_adj_eddy']  # an102
#mp.var = ['energy_column_vert_advec_as_resid_eta_time_mean']  # an103
#mp.var = ['energy_column_tendency_each_timestep', 'Q_diff_imr']  # an104
#mp.var = ['netrad_toa_imr', 'Q_sfc_imr']
#mp.var = ['energy_column_divg_adj']
#mp.var = ['energy_column_divg']
#mp.var = ['mse_stat_im', 'vcomp_stat', 'dp_sigma']
#mp.var = ['alet_imr', 'p_minus_e_im']
#mp.var = ['msf', 'condensation_rain', 'omega', 'aht_imr', 'cond_minus_e_im',
#          'alet_cond_imr', 'Q_diff_imr', 't_surf']
#mp.var = ['mse_im', 'omega']
#mp.var = ['vert_int_tdtlw_rad_imr', 'vert_int_tdtsw_rad_imr', 'sphum']
#mp.var = ['msf', 'precip_im', 'omega', 'aht_imr', 'p_minus_e_im', 'Q_diff_imr', 'alet_imr', 't_surf']
#mp.var = ['energy_column_divg_adj_time_mean']
#mp.var = ['precip_im']
#mp.var = ['vert_av_temp']
#mp.var = ['Q_diff_imr', 'precip_im', 'msf', 'aht_imr', 'olr_imr',
#          'swnet_toa_imr']
#mp.var = ['simple_aht_imr']
#mp.var = ['swnet_toa_imr', 'olr_imr']
#mp.var = ['aht_im', 'Q_diff_im', 'precip_im', 'msf']
#mp.var = ['Q_toa_im', 'Q_sfc_im']
#mp.var = ['netrad_toa_imr', 'lwdn_sfc', 'swdn_sfc', 'flux_t', 'flux_lhe',
#          'vert_int_tdtsw_rad_imr', 'vert_int_tdtlw_rad_imr',
#          'vert_int_tdt_rad_imr', 't_surf']

#mp.var = ['sphum']


#mp.var = ['msf', 'aht_imr', 'mse_im', 'vcomp_mb', 'dp_sigma', 'swdn_sfc',
#          'lwdn_sfc', 't_surf', 'vert_int_tdtsw_rad_imr',
#          'vert_int_tdtlw_rad_imr']
#mp.var = ['aht_imr', 'lwdn_sfc', 'p_minus_e_im', 't_surf', 'dp_sigma',
#          'mse_im', 'precip_im', 'msf',
#          'vcomp', 'vcomp_mb', 'Q_diff_imr', 'netrad_toa_imr', 'olr_imr']
#mp.var = ['swnet_toa_imr', 'Q_sfc_imr', 'netrad_toa_imr']
#mp.var = ['tdt_sw', 'tdt_lw', 'tdt_rad']
#mp.var = ['sphum']

#mp.var = ['vcomp_mb', 'mse_im', 'dp_sigma', 'mse_stat_im', 'vcomp_stat',
#          'aht_imr']

#mp.var = ['precip_im', 'flux_lhe', 't_surf', 'convection_rain',
#          'condensation_rain']
#mp.var = ['condensation_rain', 'flux_lhe', 't_surf', 'msf',
#          'aht_imr', 'olr_imr']

mp.var = ['height_full']

#mp.var = ['divg', 'vort', 'omega']
#mp.var = ['condensation_rain']
#mp.var = ['height_full', 'gz']

#mp.var = ['netrad_toa_imr']

#mp.var = ['Q_diff_imr', 'p_minus_e_im']
#mp.var = ['rh']
#mp.var = ['tdt_rad', 'tdt_sw', 'tdt_lw']

#mp.var = ['p_minus_e_im', 'ucomp', 'vcomp', 'sphum', 'omega', 'temp']

#mp.var = ['omega', 'sphum', 'temp', 'ps', 'vcomp', 'flux_t', 'flux_lhe',
#          'convection_rain', 'condensation_rain', 'precip_im', 'p_minus_e_im',
#          'ucomp', 't_surf', 'mse_im', 'swdn_sfc',
#          'lwdn_sfc', 'vert_int_tdt_rad_imr', 'vert_int_tdtsw_rad_imr',
#          'vert_int_tdtlw_rad_imr', 'netrad_toa_imr', 'dse_im']
#    mp.var = ['swdn_sfc', 'olr', 'lwdn_sfc', 'lwup_sfc', 'flux_t', 'flux_lhe']
#    mp.var = ['dp_sigma']
#    mp.var = ['olr','t_surf','swdn_toa','lwdn_sfc','swdn_sfc','lwup_sfc','evap','precip',
#              'swup_toa','swup_toa_clr','swdn_sfc_clr','lwup_sfc_clr','lwdn_sfc_clr',
#              ]#, 'mse_vert_advec_upwind']
    #mp.date_range = [('1983-01-01', '2012-12-31')
#mp.date_range = [('0011-01-01', '0020-12-31')]
mp.date_range = [('0003-01-01', '0006-12-31')]
#mp.date_range=[('0002-12-22', '0004-12-11')] # Leap year in datetime... Last 720 days.
#mp.date_range=[('0002-12-22', '0006-12-1')] # Leap year in datetime... Last 1440 days.
#mp.date_range = [('0021-01-01', '0080-12-31')]
    #    mp.date_range = [('1983-01-01', '1998-12-31')]
#mp.date_range = [('0002-02-05', '0002-05-16')]
#mp.date_range = [('0001-12-27', '0002-12-22')]
mp.region = ['globe', 'tropics', 'sahel']
#    mp.region = ['sahel', 'nh', 'sh', 'nh_tropics', 'sh_tropics',
#                 'nh_extratropics', 'sh_extratropics']
mp.intvl_in = ['monthly']
#mp.intvl_in = ['3-hourly']
#mp.intvl_in = ['rad_month']
#mp.intvl_in = ['20-day']
#mp.intvl_out = ['ann', 'djf', 'mam', 'jja', 'son']
#mp.intvl_out = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12] # 'jas', 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
#mp.intvl_out = ['ann', 'djf', 'mam', 'jja', 'son']
mp.intvl_out = ['ann']
mp.dtype_in_time = ['ts']
#mp.dtype_in_time = ['inst']
mp.dtype_in_vert = [False]
#mp.dtype_in_vert = ['pressure']
mp.dtype_in_vert = ['sigma']
# mp.dtype_out_time = [('reg.av',)]
mp.dtype_out_time = [('av', 'ts', 'reg.av', 'reg.ts')]# 'reg.av', 'reg.ts')]# 'ts', 'reg.av', 'reg.ts')]# 'reg.av', 'reg.ts')]
mp.dtype_out_time = [('av',)]
#mp.dtype_out_time = [('av', 'reg.av')]
#    mp.dtype_out_time = [('av', 'reg.av', 'reg.ts')]
#    mp.dtype_out_time = [('av','reg.std','reg.av','reg.ts')]
#mp.dtype_out_vert = ['vert_int']
mp.dtype_out_vert = [False]
mp.level = [False]
mp.chunk_len = [False]
mp.verbose = [True]
mp.compute = True
mp.print_table = False

if __name__ == '__main__':
    calcs = aospy_user.main(mp, prompt_verify=False)

# Unusual dates seem to work -- test
# mp.intvl_out = [12]
# mp.dtype_out_time = [('ts')]
# This returns three points for Dec; this is expected
# the number of days is at the end of the averaging period in the
# idealized model.
