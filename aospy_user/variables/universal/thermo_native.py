from aospy.var import Var
from aospy_user import units


sphum = Var(
    name='sphum',
    alt_names=('hus',),
    units=units.specific_mass,
    domain='atmos',
    description='Specific humidity.',
    def_time=True,
    def_vert='pfull',
    def_lat=True,
    def_lon=True,
    in_nc_grid=False,
    colormap='Greys'
)
rh = Var(
    name='rh',
    alt_names=('hur',),
    units=units.unitless,
    domain='atmos',
    description='Relative humidity',
    def_time=True,
    def_vert=True,
    def_lat=True,
    def_lon=True,
    in_nc_grid=False
)
rh_ref = Var(
    name='rh_ref',
    units=units.unitless,
    domain='atmos',
    description='Relative humidity at 2m above surface',
    def_time=True,
    def_vert=False,
    def_lat=True,
    def_lon=True,
    in_nc_grid=False
)
temp = Var(
    name='temp',
    alt_names=('ta',),
    units=units.K,
    domain='atmos',
    description='Air temperature.',
    def_time=True,
    def_vert='pfull',
    def_lat=True,
    def_lon=True,
    in_nc_grid=False,
    colormap='RdBu_r'
)
t_surf = Var(
    name='t_surf',
    alt_names=('tas', 'tmp'),
    units=units.K,
    domain='atmos',
    description='Surface air temperature.',
    def_time=True,
    def_vert=False,
    def_lat=True,
    def_lon=True,
    in_nc_grid=False
)
tdt_conv = Var(
    name='tdt_conv',
    units=units.K_s1,
    domain='atmos',
    description='Convective heating rate.',
    def_time=True,
    def_vert=True,
    def_lat=True,
    def_lon=True,
    in_nc_grid=False,
    valid_range=(-20, 20)
)
qdt_vdif = Var(
    name='qdt_vdif',
    units=units.kg_kg1_s1,
    domain='atmos',
    description='Time tendency of specific humidity',
    def_time=True,
    def_vert=True,
    def_lat=True,
    def_lon=True,
    in_nc_grid=False
)
tdt_ls = Var(
    name='tdt_ls',
    units=units.K_s1,
    domain='atmos',
    description='Large-scale heating rate.',
    def_time=True,
    def_vert=True,
    def_lat=True,
    def_lon=True,
    in_nc_grid=False
)
tdt_lw = Var(
    name='tdt_lw',
    units=units.K_s1,
    domain='atmos',
    description='All-sky longwave heating rate.',
    def_time=True,
    def_vert=True,
    def_lat=True,
    def_lon=True,
    in_nc_grid=False
)
tdt_lw_clr = Var(
    name='tdt_lw_clr',
    units=units.K_s1,
    domain='atmos',
    description='Clear-sky longwave heating rate.',
    def_time=True,
    def_vert=True,
    def_lat=True,
    def_lon=True,
    in_nc_grid=False
)
tdt_sw = Var(
    name='tdt_sw',
    units=units.K_s1,
    domain='atmos',
    description='All-sky shortwave heating rate.',
    def_time=True,
    def_vert=True,
    def_lat=True,
    def_lon=True,
    in_nc_grid=False
)
tdt_sw_clr = Var(
    name='tdt_sw_clr',
    units=units.K_s1,
    domain='atmos',
    description='Clear-sky shortwave heating rate.',
    def_time=True,
    def_vert=True,
    def_lat=True,
    def_lon=True,
    in_nc_grid=False
)
tdt_vdif = Var(
    name='tdt_vdif',
    units=units.K_s1,
    domain='atmos',
    description='Temperature tendency from vertical diffusion.',
    def_time=True,
    def_vert=True,
    def_lat=True,
    def_lon=True,
    in_nc_grid=False
)
ice_wat = Var(
    name='ice_wat',
    units=units.specific_mass,
    domain='atmos',
    description='Cloud ice water specific humidity.',
    def_time=True,
    def_vert=True,
    def_lat=True,
    def_lon=True,
    in_nc_grid=False
)
liq_wat = Var(
    name='liq_wat',
    units=units.specific_mass,
    domain='atmos',
    description='Cloud liquid water specific humidity.',
    def_time=True,
    def_vert=True,
    def_lat=True,
    def_lon=True,
    in_nc_grid=False
)
mc = Var(
    name='mc',
    units=units.kg_m2_s1_mass,
    domain='atmos',
    description='Convective mass flux.',
    def_time=True,
    def_vert=True,
    def_lat=True,
    def_lon=True,
    in_nc_grid=False
)
mc_full = Var(
    name='mc_full',
    units=units.kg_m2_s1_mass,
    domain='atmos',
    description='Convective mass flux at full levels.',
    def_time=True,
    def_vert=True,
    def_lat=True,
    def_lon=True,
    in_nc_grid=False
)
mc_half = Var(
    name='mc_half',
    units=units.kg_m2_s1_mass,
    domain='atmos',
    description='Convective mass flux at half levels.',
    def_time=True,
    def_vert=True,
    def_lat=True,
    def_lon=True,
    in_nc_grid=False
)
sst = Var(
    name='sst',
    alt_names=('ts', 'SST'),
    units=units.K,
    domain='ocean',
    description='Sea surface temperature.',
    def_time=True,
    def_vert=False,
    def_lat=True,
    def_lon=True,
    in_nc_grid=False
)
