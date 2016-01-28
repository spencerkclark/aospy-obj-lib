from aospy.var import Var
from aospy_user import units


# Model native variables
height_half = Var(
    name='height_half',
    alt_names=('zg', 'height_half', 'hght'),
    units=units.m,
    domain='atmos',
    description='Geopotential height.',
    def_time=True,
    def_vert='phalf',
    def_lat=True,
    def_lon=True,
    in_nc_grid=False
)
height_full = Var(
    name='height_full',
    alt_names=('height',),
    units=units.m,
    domain='atmos',
    description=('Geopotential height on full levels'),
    def_time=True,
    def_vert=True,
    def_lat=True,
    def_lon=True,
    in_nc_grid=False
)
ucomp = Var(
    name='ucomp',
    alt_names=('ua',),
    units=units.m_s1,
    domain='atmos',
    description='Eastward velocity.',
    def_time=True,
    def_vert='pfull',
    def_lat=True,
    def_lon=True,
    in_nc_grid=False
)
u_ref = Var(
    name='u_ref',
    units=units.m_s1,
    domain='atmos',
    description='Eastward velocity at 2 meters above ground.',
    def_time=True,
    def_vert=False,
    def_lat=True,
    def_lon=True,
    in_nc_grid=False
)
vcomp = Var(
    name='vcomp',
    alt_names=('va',),
    units=units.m_s1,
    domain='atmos',
    description='Northward velocity.',
    def_time=True,
    def_vert='pfull',
    def_lat=True,
    def_lon=True,
    in_nc_grid=False
)
v_ref = Var(
    name='v_ref',
    units=units.m_s1,
    domain='atmos',
    description='Northward velocity at 2 meters above ground.',
    def_time=True,
    def_vert=False,
    def_lat=True,
    def_lon=True,
    in_nc_grid=False
)
omega = Var(
    name='omega',
    alt_names=('wap',),
    units=units.Pa_s1,
    domain='atmos',
    description='Pressure vertical velocity.',
    def_time=True,
    def_vert='pfull',
    def_lat=True,
    def_lon=True,
    in_nc_grid=False
)
vort = Var(
    name='vort',
    units=units.s1_vort,
    domain='atmos',
    description='Vorticity',
    def_time=True,
    def_vert=True,
    def_lat=True,
    def_lon=True,
    in_nc_grid=False
)
divg = Var(
    name='divg',
    math_str=r"\nabla\cdot\vec{v}",
    units=units.s1,
    domain='atmos',
    description='Divergence.',
    def_time=True,
    def_vert=True,
    def_lat=True,
    def_lon=True,
    in_nc_grid=False,
    colormap='RdBu'
)
pv = Var(
    name='pv',
    units=units.s1,
    domain='atmos',
    description='Potential vorticity',
    def_time=True,
    def_vert=True,
    def_lat=True,
    def_lon=True,
    in_nc_grid=False
)
esf = Var(
    name='esf',
    units=units.kg_s1,
    domain='atmos',
    description='Eddy streamfunction',
    def_time=True,
    def_vert=True,
    def_lat=True,
    def_lon=True,
    in_nc_grid=False
)
