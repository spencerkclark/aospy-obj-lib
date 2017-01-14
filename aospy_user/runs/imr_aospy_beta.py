import os
from datetime import datetime

from aospy import Run
from aospy.data_loader import DictDataLoader

# New albedo -- last 1860 days of each run; haven't addressed 3 hourly output
# yet.
ROOT = ('/archive/Spencer.Clark/imr_skc/'
        'control/gfdl.ncrc3-default-repro/1/'
        'history')
control = Run(
    name='control',
    description=(
        'Control simulation of idealized moist run with realistic'
        'radiative transfer.'
    ),
    data_loader=DictDataLoader({'monthly': os.path.join(
                ROOT, '000[1-6]0101.atmos_month.nc'),
                                'rad_month': os.path.join(
                ROOT, '000[1-6]0101.atmos_rad_month.nc'),
                                '3-hourly': os.path.join(
                ROOT, '000[1-6]0101.atmos_8xday.nc')}),
    default_start_date=datetime(3, 1, 1),
    default_end_date=datetime(6, 12, 31),
)
