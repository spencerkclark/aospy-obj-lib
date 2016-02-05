from aospy.var import Var
from aospy_user import units


# Model native variables
olr = Var(
    name='olr',
    alt_names=('rlut',),
    units=units.W_m2,
    domain='atmos',
    description='All-sky outgoing longwave radiation at TOA.',
    def_time=True,
    def_vert=False,
    def_lat=True,
    def_lon=True,
    in_nc_grid=False
)
olr_clr = Var(
    name='olr_clr',
    alt_names=('rlutcs',),
    units=units.W_m2,
    domain='atmos',
    description='Clear-sky outgoing longwave radiation at TOA.',
    def_time=True,
    def_vert=False,
    def_lat=True,
    def_lon=True,
    in_nc_grid=False
)
lwdn_sfc = Var(
    name='lwdn_sfc',
    alt_names=('rlds', 'lw_down_sfc'),
    math_str="$R^{LW\downarrow_{sfc}$",
    description='All-sky downwelling longwave radiation at the surface.',
    domain='atmos',
    units=units.W_m2,
    def_time=True,
    def_vert=False,
    def_lat=True,
    def_lon=True,
    in_nc_grid=False
)
lwdn_sfc_clr = Var(
    name='lwdn_sfc_clr',
    alt_names=('rldscs',),
    units=units.W_m2,
    domain='atmos',
    description='Clear-sky downwelling longwave radiation at the surface.',
    def_time=True,
    def_vert=False,
    def_lat=True,
    def_lon=True,
    in_nc_grid=False
)
lwup_sfc = Var(
    name='lwup_sfc',
    alt_names=('rlus',),
    units=units.W_m2,
    domain='atmos',
    description='All-sky upwelling longwave radiation at the surface.',
    def_time=True,
    def_vert=False,
    def_lat=True,
    def_lon=True,
    in_nc_grid=False
)
lwup_sfc_clr = Var(
    name='lwup_sfc_clr',
    alt_names=('rluscs',),
    units=units.W_m2,
    domain='atmos',
    description='Clear-sky upwelling longwave radiation at the surface.',
    def_time=True,
    def_vert=False,
    def_lat=True,
    def_lon=True,
    in_nc_grid=False
)
swdn_sfc = Var(
    name='swdn_sfc',
    alt_names=('rsds', 'sw_down_sfc'),
    units=units.W_m2,
    domain='atmos',
    description='All-sky downwelling shortwave radiation at the surface.',
    def_time=True,
    def_vert=False,
    def_lat=True,
    def_lon=True,
    in_nc_grid=False
)
swdn_sfc_clr = Var(
    name='swdn_sfc_clr',
    alt_names=('rsdscs',),
    units=units.W_m2,
    domain='atmos',
    description='Clear-sky downwelling shortwave radiation at the surface.',
    def_time=True,
    def_vert=False,
    def_lat=True,
    def_lon=True,
    in_nc_grid=False
)
swup_sfc = Var(
    name='swup_sfc',
    alt_names=('rsus',),
    units=units.W_m2,
    domain='atmos',
    description='All-sky upwelling shortwave radiation at the surface.',
    def_time=True,
    def_vert=False,
    def_lat=True,
    def_lon=True,
    in_nc_grid=False
)
swup_sfc_clr = Var(
    name='swup_sfc_clr',
    alt_names=('rsuscs',),
    units=units.W_m2,
    domain='atmos',
    description='Clear-sky upwelling shortwave radiation at the surface.',
    def_time=True,
    def_vert=False,
    def_lat=True,
    def_lon=True,
    in_nc_grid=False
)
swdn_toa = Var(
    name='swdn_toa',
    alt_names=('rsdt',),
    units=units.W_m2,
    domain='atmos',
    description='Downwelling shortwave radiation at TOA.',
    def_time=True,
    def_vert=False,
    def_lat=True,
    def_lon=True,
    in_nc_grid=False
)
swdn_toa_clr = Var(
    name='swdn_toa_clr',
    alt_names=('rsdtcs',),
    units=units.W_m2,
    domain='atmos',
    description='Downwelling shortwave radiation at TOA.',
    def_time=True,
    def_vert=False,
    def_lat=True,
    def_lon=True,
    in_nc_grid=False
)
swup_toa = Var(
    name='swup_toa',
    alt_names=('rsut',),
    units=units.W_m2,
    domain='atmos',
    description='All-sky Upwelling shortwave radiation at TOA.',
    def_time=True,
    def_vert=False,
    def_lat=True,
    def_lon=True,
    in_nc_grid=False
)
swup_toa_clr = Var(
    name='swup_toa_clr',
    alt_names=('rsutcs',),
    units=units.W_m2,
    domain='atmos',
    description='Clear-sky upwelling shortwave radiation at TOA.',
    def_time=True,
    def_vert=False,
    def_lat=True,
    def_lon=True,
    in_nc_grid=False
)
alb_sfc = Var(
    name='alb_sfc',
    units=units.unitless,
    domain='atmos',
    description='Surface albedo.',
    def_time=True,
    def_vert=False,
    def_lat=True,
    def_lon=True,
    in_nc_grid=False
)
shflx = Var(
    name='shflx',
    alt_names=('hfss',),
    units=units.W_m2,
    domain='atmos',
    description='Surface sensible heat flux into the atmosphere.',
    def_time=True,
    def_vert=False,
    def_lat=True,
    def_lon=True,
    in_nc_grid=False
)
