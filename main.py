#! /usr/bin/env python
"""Main script for automating computations using aospy."""
from datetime import datetime

import aospy_user
import groupings


mp = aospy_user.MainParams()
mp.proj = 'itcz'
mp.model = ['idealized_moist_rad']
mp.run = groupings.MS_EXPERIMENTS
mp.ens_mem = [None]
mp.var = ['msf', 'aht_imr']
mp.date_range = [(datetime(3, 1, 1), datetime(6, 12, 31))]
mp.intvl_in = ['monthly']
mp.intvl_out = ['ann']
mp.dtype_in_time = ['ts']
mp.dtype_in_vert = ['sigma']
mp.dtype_out_time = [('av',)]
mp.region = ['globe']
mp.dtype_out_vert = [False]
mp.level = [False]
mp.verbose = [True]
mp.time_offset = [{'days': -15}]
mp.compute = True
mp.print_table = False

if __name__ == '__main__':
    calcs = aospy_user.main(mp, prompt_verify=False, parallelize=True)
