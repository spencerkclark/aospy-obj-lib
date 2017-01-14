#! /usr/bin/env python
"""Main script for automating computations using aospy."""
from datetime import datetime

import aospy_user


control = ['control']

mp = aospy_user.MainParams()
mp.proj = 'test'
# mp.model = ['idealized_moist_rad']
mp.model = ['am2']
# mp.run = control
mp.run = ['am2_control']
mp.ens_mem = [False]
mp.var = ['msf']
mp.date_range = [(datetime(21, 1, 1), datetime(25, 12, 31))]
# mp.date_range = [(datetime(3, 1, 1), datetime(6, 12, 31))]
mp.intvl_in = ['monthly']
mp.intvl_out = ['ann']
mp.dtype_in_time = ['ts']
mp.dtype_in_vert = ['sigma']
mp.dtype_out_time = [('av', 'ts')]# 'reg.av', 'reg.ts')]
mp.region = ['globe']
# mp.dtype_out_time = [('av',)]
# mp.dtype_out_vert = ['vert_int']
mp.dtype_out_vert = [False]
mp.level = [False]
mp.chunk_len = [False]
mp.verbose = [True]
mp.compute = True
mp.print_table = False

if __name__ == '__main__':
    calcs = aospy_user.main(mp, prompt_verify=False, parallelize=False)

# Unusual dates seem to work -- test
# mp.intvl_out = [12]
# mp.dtype_out_time = [('ts')]
# This returns three points for Dec; this is expected
# the number of days is at the end of the averaging period in the
# idealized model.
