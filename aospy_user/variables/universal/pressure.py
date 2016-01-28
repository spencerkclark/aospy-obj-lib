from aospy.var import Var
from aospy_user import calcs, units
from aospy_user.variables.universal.thermo_native import temp


p = Var(
    name='p',
    units=units.Pa,
    domain='atmos',
    description='Pressure of model half levels.',
    def_time=True,
    def_vert=True,
    def_lat=True,
    def_lon=True,
    in_nc_grid=False
)
ps = Var(
    name='ps',
    units=units.Pa,
    domain='atmos',
    description='Surface pressure.',
    def_time=True,
    def_vert=False,
    def_lat=True,
    def_lon=True,
    in_nc_grid=False
)
bk = Var(
    name='bk',
    units=units.Pa,
    domain='atmos_level',
    description='Sigma part of hybrid sigma coordinate.',
    def_time=False,
    def_vert=True,
    def_lat=False,
    def_lon=False,
    in_nc_grid=True
)
pk = Var(
    name='pk',
    units=units.Pa,
    domain='atmos_level',
    description='Pressure part of hybrid sigma coordinate.',
    def_time=False,
    def_vert=True,
    def_lat=False,
    def_lon=False,
    in_nc_grid=True
)
dp = Var(
    name='dp',
    domain='atmos',
    description=('Pressure thickness of model levels.  For data interpolated '
                 'to uniform pressure levels, this does not vary in time or '
                 'space.  For data on model native coordinates, this varies '
                 'in space and time due to the spatiotemporal variations in '
                 'surface pressure.'),
    variables=(ps, bk, pk, temp),
    def_time=True,
    def_vert=True,
    def_lat=True,
    def_lon=True,
    in_nc_grid=False,
    func=calcs.dp,
    units=units.Pa,
)
dp_sigma = Var(
    name='dp_sigma',
    domain='atmos',
    description=('dp_sigma'),
    variables=(temp, dp),
    def_time=True,
    def_vert=True,
    def_lat=True,
    def_lon=True,
    func=calcs.dp_sigma,
    units=units.Pa
)
pfull = Var(
    name='pfull',
    domain='atmos',
    description=('pressure at the level midpoints'),
    variables=(p),
    def_time=True,
    def_vert=True,
    def_lat=True,
    def_lon=True,
    func=calcs.pfull,
    units=units.Pa
)
