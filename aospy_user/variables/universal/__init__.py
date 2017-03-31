"""Universal variables (appear in multiple models) or apply to
standard GCM's.
"""
# Import native variables, then pressure, then the computed variables.
from . import dynamics_native
from . import energy_native
from . import thermo_native
from . import water_native
from . import pressure
from . import dynamics_computed
from . import energy_computed
from . import thermo_computed
from . import water_computed

