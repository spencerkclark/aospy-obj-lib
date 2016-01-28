from aospy.var import Var
from aospy_user import units


precip = Var(
    name='precip',
    alt_names=('pr', 'pre'),
    units=units.kg_m2_s1,
    domain='atmos',
    description='Liquid precipitation reaching surface.',
    def_time=True,
    def_vert=False,
    def_lat=True,
    def_lon=True,
    in_nc_grid=False,
    colormap='BrBG'
)
prec_conv = Var(
    name='prec_conv',
    alt_names=('prc',),
    units=units.kg_m2_s1,
    domain='atmos',
    description='Liquid precip reaching surface from convection scheme.',
    def_time=True,
    def_vert=False,
    def_lat=True,
    def_lon=True,
    in_nc_grid=False,
    colormap='BrBG'
)
prec_ls = Var(
    name='prec_ls',
    units=units.kg_m2_s1,
    domain='atmos',
    description='Liquid precip reaching surface from large scale ascent.',
    def_time=True,
    def_vert=False,
    def_lat=True,
    def_lon=True,
    in_nc_grid=False,
    colormap='BrBG'
)
evap = Var(
    name='evap',
    alt_names=('ET_mean', 'evspsbl'),
    math_str=r"$E$",
    units=units.kg_m2_s1,
    domain='atmos',
    description='Surface evaporation',
    def_time=True,
    def_vert=False,
    def_lat=True,
    def_lon=True,
    in_nc_grid=False
)
snow_conv = Var(
    name='snow_conv',
    units=units.kg_m2_s1,
    domain='atmos',
    description='Snow reaching surface from convection scheme.',
    def_time=True,
    def_vert=False,
    def_lat=True,
    def_lon=True,
    in_nc_grid=False
)
snow_ls = Var(
    name='snow_ls',
    units=units.kg_m2_s1,
    domain='atmos',
    description='Snow reaching surface from large scale ascent.',
    def_time=True,
    def_vert=False,
    def_lat=True,
    def_lon=True,
    in_nc_grid=False
)
soil_liq = Var(
    name='soil_liq',
    units=units.kg_m2,
    domain='land',
    description='Soil liquid in each level of land model',
    def_time=True,
    def_vert=True,
    def_lat=True,
    def_lon=True,
    in_nc_grid=False
)
soil_moisture = Var(
    name='soil_moisture',
    alt_names=('water', 'water_soil',),
    units=units.kg_m2,
    domain='land',
    description='Mass of water in land bucket',
    def_time=True,
    def_vert=False,
    def_lat=True,
    def_lon=True,
    in_nc_grid=False
)
high_cld_amt = Var(
    name='high_cld_amt',
    units=units.unitless,
    domain='atmos',
    description='High cloud fraction.',
    def_time=True,
    def_vert=False,
    def_lat=True,
    def_lon=True,
    in_nc_grid=False
)
low_cld_amt = Var(
    name='low_cld_amt',
    units=units.unitless,
    domain='atmos',
    description='Low cloud fraction.',
    def_time=True,
    def_vert=False,
    def_lat=True,
    def_lon=True,
    in_nc_grid=False
)
mid_cld_amt = Var(
    name='mid_cld_amt',
    units=units.unitless,
    domain='atmos',
    description='Mid-level cloud fraction.',
    def_time=True,
    def_vert=False,
    def_lat=True,
    def_lon=True,
    in_nc_grid=False
)
tot_cld_amt = Var(
    name='tot_cld_amt',
    alt_names=('clt',),
    units=units.unitless,
    domain='atmos',
    description='Total cloud fraction.',
    def_time=True,
    def_vert=False,
    def_lat=True,
    def_lon=True,
    in_nc_grid=False
)
cld_amt = Var(
    name='cld_amt',
    alt_names=('cl',),
    units=units.unitless,
    domain='atmos',
    description='Cloud fraction at each level.',
    def_time=True,
    def_vert=True,
    def_lat=True,
    def_lon=True,
    in_nc_grid=False
)
wvp = Var(
    name='wvp',
    alt_names=('WVP', 'prw'),
    units=units.kg_m2,
    domain='atmos',
    description='Water vapor path',
    def_time=True,
    def_vert=False,
    def_lat=True,
    def_lon=True,
    in_nc_grid=False,
    colormap='Greys'
)
