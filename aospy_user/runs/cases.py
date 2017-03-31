from datetime import datetime

from aospy import Run
from aospy.data_loader import GFDLDataLoader

am2_control = Run(
    name='am2_control',
    description=(
        'Preindustrial control simulation.'
    ),
    data_loader=GFDLDataLoader(data_direc=('/archive/Yi.Ming/sm2.1_fixed/'
                                           'SM2.1U_Control-1860_lm2_aie_rerun6'
                                           '.YIM/pp'),
                               data_dur=5,
                               data_start_date=datetime(1, 1, 1),
                               data_end_date=datetime(80, 12, 31)),
    default_start_date=datetime(21, 1, 1),
    default_end_date=datetime(31, 1, 1)
)
