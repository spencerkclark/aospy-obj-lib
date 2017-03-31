#! /usr/bin/env python
"""Main script for automating computations using aospy."""
from datetime import datetime

import aospy_user
import groupings


mp = aospy_user.MainParams()
mp.proj = 'itcz'
mp.model = ['idealized_moist_rad']
# mp.run = ['control'] + groupings.CONTROL_GRAY
mp.run = ['control']
# mp.run = groupings.CONTROL_GRAY
# mp.run = ['control_raw']
mp.ens_mem = [None]
# mp.var = ['olr_diag_imr', 'lwdn_sfc_imr', 'lwup_sfc_imr']
mp.var = ['vert_int_tdtlw_rad_imr', 'lwup_sfc', 'lwdn_sfc', 'swdn_sfc']
mp.var = ['lwdn_sfc', 'lwup_sfc_im', 'swdn_sfc', 'olr']
mp.var = ['vert_int_tdtlw_rad_imr', 'vert_int_tdtsw_rad_imr']
mp.date_range = [(datetime(3, 1, 1), datetime(6, 12, 31))]
# mp.date_range = [(datetime(1, 1, 1), datetime(2, 12, 31))]
mp.intvl_in = ['monthly']
mp.intvl_out = ['ann']
mp.dtype_in_time = ['ts']
mp.dtype_in_vert = ['sigma']
mp.dtype_out_time = [('av', 'reg.av')]
# mp.dtype_out_time = [('av',)]
mp.region = ['globe']
mp.dtype_out_vert = [False]
mp.level = [False]
mp.verbose = [True]
mp.time_offset = [{'days': -15}]
mp.compute = True
mp.print_table = False

if __name__ == '__main__':
    calcs = aospy_user.main(mp, prompt_verify=False, parallelize=False)
