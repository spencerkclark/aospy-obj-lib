#! /usr/bin/env python
"""Main script for automating computations using aospy."""
import aospy_user

mp = aospy_user.MainParams()
mp.proj = 'itcz'
#    mp.proj = 'dargan_test'
mp.model = ['am2']
#mp.model = ['dargan_T42']
#mp.model = ['idealized_moist_rad']
#    mp.model = ['am2_reyoi']
#    mp.model = ['dargan']
mp.run = [('am2_control','am2_tropics', 'am2_extratropics','am2_tropics+extratropics')]
#mp.run = [('imr_control_yi')]
#mp.run = [('control_gaussian_T42',
#           'tropics_gaussian_5.0_T42',
#           'extratropics_gaussian_5.0_T42',
#           'tropics_gaussian_15.0_T42',
#           'extratropics_gaussian_15.0_T42',
#           'tropics_gaussian_25.0_T42',
#           'extratropics_gaussian_25.0_T42')]
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
#    mp.var = ['tdt_sw', 'tdt_lw', 'tdt_vdif', 'qdt_vdif']#, 'vcomp_mb', 'mse']
#    mp.var = ['aht', 'msf', 'olr', 'swdn_toa', 'swdn_sfc', 'lwdn_sfc', 'mse',
#              'precip_im']
mp.var = ['p_minus_e']
#    mp.var = ['swdn_sfc', 'olr', 'lwdn_sfc', 'lwup_sfc', 'flux_t', 'flux_lhe']
#    mp.var = ['dp_sigma']
#    mp.var = ['olr','t_surf','swdn_toa','lwdn_sfc','swdn_sfc','lwup_sfc','evap','precip',
#              'swup_toa','swup_toa_clr','swdn_sfc_clr','lwup_sfc_clr','lwdn_sfc_clr',
#              ]#, 'mse_vert_advec_upwind']
    #mp.date_range = [('1983-01-01', '2012-12-31')
mp.date_range = [('0021-01-01', '0080-12-31')]
    #    mp.date_range = [('1983-01-01', '1998-12-31')]
#mp.date_range = [('0002-02-05', '0002-05-16')]
#mp.date_range = [('0001-12-27', '0002-12-22')]
mp.region = ['nh', 'sh', 'globe']
#    mp.region = ['sahel', 'nh', 'sh', 'nh_tropics', 'sh_tropics',
#                 'nh_extratropics', 'sh_extratropics']
mp.intvl_in = ['monthly']
#mp.intvl_in = ['20-day']
#    mp.intvl_in = ['20-day']
#    mp.intvl_out = ['ann', 'jas', 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12] # 'jas', 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
mp.intvl_out = ['ann']
mp.dtype_in_time = ['ts']
mp.dtype_in_vert = [False]
mp.dtype_in_vert = ['pressure']
#mp.dtype_in_vert = ['sigma']
# mp.dtype_out_time = [('reg.av',)]
mp.dtype_out_time = [('av')]# 'ts', 'reg.av', 'reg.ts')]# 'reg.av', 'reg.ts')]
#    mp.dtype_out_time = [('av', 'reg.av', 'reg.ts')]
#    mp.dtype_out_time = [('av','reg.std','reg.av','reg.ts')]
#    mp.dtype_out_vert = ['vert_int']
mp.dtype_out_vert = [False]
mp.level = [False]
mp.chunk_len = [False]
mp.verbose = [True]
mp.compute = True
mp.print_table = False

if __name__ == '__main__':
    calcs = aospy_user.main(mp, prompt_verify=True)

# Unusual dates seem to work -- test
# mp.intvl_out = [12]
# mp.dtype_out_time = [('ts')]
# This returns three points for Dec; this is expected
# the number of days is at the end of the averaging period in the
# idealized model.
