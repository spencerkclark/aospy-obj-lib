"""Some global variables pointing to groups of Run names for convenient
use in the main script.
"""

FORCINGS = ['e5', 'e15', 'e18', 't5', 't15', 't18']
CONTROL = ['control', 'fixed_h2o', 'conv_off', 'fixed_h2o_conv_off']
DEFAULT = ['asym_{}'.format(forcing) for forcing in FORCINGS]
FIXED_H2O = ['asym_{}_fixed_h2o'.format(forcing) for forcing in FORCINGS]
CONV_OFF = ['asym_{}_conv_off'.format(forcing) for forcing in FORCINGS]
CONV_OFF_FIXED_H2O = ['asym_{}_conv_off_fixed_h2o'.format(forcing)
                      for forcing in FORCINGS]
MS_EXPERIMENTS = DEFAULT + FIXED_H2O + CONV_OFF + CONV_OFF_FIXED_H2O

SELECTIVE = ['asym_t15_fixed_h2o_tropics',
             'asym_e15_fixed_h2o_tropics',
             'asym_t15_fixed_h2o_extratropics',
             'asym_e15_fixed_h2o_extratropics']
ANTI = ['anti_t15',
        'anti_e15',
        'anti_t15_fixed_h2o',
        'anti_e15_fixed_h2o',
        'anti_t15_fixed_h2o_tropics',
        'anti_e15_fixed_h2o_tropics',
        'anti_t15_fixed_h2o_extratropics',
        'anti_e15_fixed_h2o_extratropics']
CONTROL_GRAY = ['control_gray', 'control_gray_solar']
