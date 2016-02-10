from aospy.region import Region


# Globe
globe = Region(
    name='globe',
    description='Entire globe',
    lat_bounds=(-90, 90),
    lon_bounds=(0, 360),
    do_land_mask=False
)
# Land.
land = Region(
    name='land',
    description='Land',
    lat_bounds=(-90, 90),
    lon_bounds=(0, 360),
    do_land_mask=True
)
# Ocean.
ocean = Region(
    name='ocean',
    description='Ocean',
    lat_bounds=(-90, 90),
    lon_bounds=(0, 360),
    do_land_mask='ocean'
)
# Northern Hemisphere.
nh = Region(
    name='nh',
    description='Northern Hemisphere',
    lat_bounds=(0, 90),
    lon_bounds=(0, 360),
    do_land_mask=False
)
# North Pole
np = Region(
    name='np',
    description='North Pole',
    lat_bounds=(60, 90),
    lon_bounds=(0, 360),
    do_land_mask=False
)
# Southern Hemisphere.
sh = Region(
    name='sh',
    description='Southern Hemisphere',
    lat_bounds=(-90, 0),
    lon_bounds=(0, 360),
    do_land_mask=False
)
# South Pole
sp = Region(
    name='sp',
    description='South Pole',
    lat_bounds=(-90, -60),
    lon_bounds=(0, 360),
    do_land_mask=False
)
nh_tropics = Region(
    name='nh_tropics',
    description='Northern Hemisphere Tropics',
    lat_bounds=(0, 30),
    lon_bounds=(0, 360),
    do_land_mask=False,
)
sh_tropics = Region(
    name='sh_tropics',
    description='Southern Hemisphere Tropics',
    lat_bounds=(-30, 0),
    lon_bounds=(0, 360),
    do_land_mask=False,
)
nh_extratropics = Region(
    name='nh_extratropics',
    description='Northern Hemisphere Extratropics',
    lat_bounds=(30, 90),
    lon_bounds=(0, 360),
    do_land_mask=False
)
sh_extratropics = Region(
    name='sh_extratropics',
    description='Southern Hemisphere Extratropics',
    lat_bounds=(-90, -30),
    lon_bounds=(0, 360),
    do_land_mask=False
)
# Eastern Hemisphere.
eh = Region(
    name='eh',
    description='Eastern Hemisphere',
    lat_bounds=(-90, 90),
    lon_bounds=(0, 180),
    do_land_mask=False
)
# Western Hemisphere.
wh = Region(
    name='wh',
    description='Western Hemisphere',
    lat_bounds=(-90, 90),
    lon_bounds=(180, 360),
    do_land_mask=False
)
# Tropics.
tropics = Region(
    name='tropics',
    description='Tropics (30S-30N)',
    lat_bounds=(-30, 30),
    lon_bounds=(0, 360),
    do_land_mask=False
)
# Tropical land
trop_land = Region(
    name='tropics_land',
    description='All land 30S-30N',
    lat_bounds=(-30, 30),
    lon_bounds=(0, 360),
    do_land_mask=True
)
# Tropical ocean
trop_ocean = Region(
    name='tropics_ocean',
    description='All ocean 30S-30N',
    lat_bounds=(-30, 30),
    lon_bounds=(0, 360),
    do_land_mask='ocean'
)
# Deep tropics.
deep_tropics = Region(
    name='deep tropics',
    description='Deep tropics (10S-10N)',
    lat_bounds=(-10, 10),
    lon_bounds=(0, 360),
    do_land_mask=False
)
# Sahel.
sahel = Region(
    name='sahel',
    description='African Sahel',
    mask_bounds=[((10, 20), (0, 40)), ((10, 20), (342, 360))],
    do_land_mask=True
)

### Below this line are deprecated Regions ###

# Alternate Sahel: narrower latitude range & strict land mask
sahel2 = Region()
sahel2.name = 'sahel2'
sahel2.description = 'African Sahel w/ longitude bounds 15W-30E'
sahel2.mask_bounds = [((10, 20), (0, 30)), ((10, 20), (345, 360))]
sahel2.do_land_mask = 'strict'
# Alternate Sahel: only 20W-15E
sahel3 = Region()
sahel3.name = 'sahel3'
sahel3.description = (
    'Western part of African Sahel.  Used by some to '
    'specify the whole Sahel (incorrectly, in my view.  '
    'No land mask -- unclear if the other studies use '
    'one or not.')
sahel3.mask_bounds = [((10, 20), (0, 10)), ((10, 20), (340, 360))]
sahel3.do_land_mask = False
# Northern Sahel
sahel_north = Region()
sahel_north.name = 'sahel_north'
sahel_north.description = 'Northern half of African Sahel'
sahel_north.mask_bounds = [((15, 20), (0, 40)), ((15, 20), (342, 360))]
sahel_north.do_land_mask = True
# Southern Sahel
sahel_south = Region()
sahel_south.name = 'sahel_south'
sahel_south.description = 'Southern half of African Sahel.'
sahel_south.mask_bounds = [((10, 15), (0, 40)), ((10, 15), (342, 360))]
sahel_south.do_land_mask = True
# Western Sahel
sahel_west = Region()
sahel_west.name = 'sahel_west'
sahel_west.description = 'Western half of African Sahel'
sahel_west.mask_bounds = [((10, 20), (0, 11)), ((10, 20), (342, 360))]
sahel_west.do_land_mask = True
# Eastern Sahel
sahel_east = Region()
sahel_east.name = 'sahel_east'
sahel_east.description = 'Eastern half of African Sahel.'
sahel_east.lat_bnds = (10, 20)
sahel_east.lon_bnds = (11, 40)
sahel_east.do_land_mask = True
# Sahara.
sahara = Region()
sahara.name = 'sahara'
sahara.description = 'African Sahara, as defined by Biasutti et al 2009'
sahara.mask_bounds = [((20, 30), (0, 35)), ((20, 30), (350, 360))]
sahara.do_land_mask = True
# Indian monsoon.
ind_monsoon = Region()
ind_monsoon.name = 'ind_monsoon'
ind_monsoon.description = 'Indian monsoon'
ind_monsoon.lat_bnds = (10, 30)
ind_monsoon.lon_bnds = (60, 100)
ind_monsoon.do_land_mask = False
# Warm Pool.
warm_pool = Region()
warm_pool.name = 'warm_pool'
warm_pool.description = 'Indo-Pacific warm pool. Ocean mask.'
warm_pool.lat_bnds = (-20, 20)
warm_pool.lon_bnds = (60, 180)
warm_pool.do_land_mask = 'ocean'
# West Pacific Warm Pool.
wpwp = Region()
wpwp.name = 'wpwp'
wpwp.description = 'West Pacific Warm Pool'
wpwp.lat_bnds = (-5, 5)
wpwp.lon_bnds = (80, 160)
wpwp.do_land_mask = False
# East Pacific cold tongue.
epac = Region()
epac.name = 'epac'
epac.description = 'East Pacific cold tongue'
epac.lat_bnds = (-5, 5)
epac.lon_bnds = (200, 280)
epac.do_land_mask = False
# East Pacific/West Atlantic.
epac_watl = Region()
epac_watl.name = 'epac_watl'
epac_watl.description = 'East Pacific and West Atlantic, including C. and S. America'
epac_watl.lat_bnds = (0, 15)
epac_watl.lon_bnds = (240, 300)
epac_watl.do_land_mask = False
# East Pacific ITCZ.
epac_itcz = Region()
epac_itcz.name = 'epac_itcz'
epac_itcz.description = 'East Pacific ITCZ for NH summer'
epac_itcz.lat_bnds = (0, 20)
epac_itcz.lon_bnds = (180, 250)
epac_itcz.do_land_mask = False
# Atlantic ITCZ.
atl_itcz = Region()
atl_itcz.name = 'atl_itcz'
atl_itcz.description = 'Atlantic ITCZ for NH summer'
atl_itcz.lat_bnds = (0, 20)
atl_itcz.lon_bnds = (300, 345)
atl_itcz.do_land_mask = False
# Burls W. Pacific
burls_wpac = Region()
burls_wpac.name = 'burls_wpac'
burls_wpac.description = 'Equatorial W. Pacific region used by Burls and Fedorov 2014'
burls_wpac.lat_bnds = (-8, 8)
burls_wpac.lon_bnds = (130, 205)
burls_wpac.do_land_mask = False
# Burls E. Pacific
burls_epac = Region()
burls_epac.name = 'burls_epac'
burls_epac.description = 'Equatorial E. Pacific region used by Burls and Fedorov 2014'
burls_epac.lat_bnds = (-8, 8)
burls_epac.lon_bnds = (205, 280)
burls_epac.do_land_mask = False
# Burls Pacific
burls_pac = Region()
burls_pac.name = 'burls_pac'
burls_pac.description = 'Pacific region used by Burls and Fedorov 2014.'
burls_pac.mask_bounds = [(( 15, 65), (100, 260)),
                         (( 10, 15), (100, 275)),
                         (( -5, 10), (100, 290)),
                         ((-65, -5), (130, 290))]
burls_pac.do_land_mask = 'strict_ocean'
# Burls Tropical Pacific
burls_trop_pac = Region()
burls_trop_pac.name = 'burls_trop_pac'
burls_trop_pac.description = 'Tropical Pacific region used by Burls and Fedorov 2014.'
burls_trop_pac.mask_bounds = [(( -5, 8), (100, 290)),
                              (( -8,  -5), (130, 290))]
burls_trop_pac.do_land_mask = 'strict_ocean'
# Burls Extratropical Pacific
burls_ext_pac = Region()
burls_ext_pac.name = 'burls_ext_pac'
burls_ext_pac.description = 'Extratropical Pacific region used by Burls and Fedorov 2014.'
burls_ext_pac.mask_bounds = [(( 15, 65), (100, 260)),
                              (( 10, 15), (100, 275)),
                              (( 8, 10), (100, 290)),
                              ((-65, -8), (130, 290))]
burls_ext_pac.do_land_mask = 'strict_ocean'
# Nino 1+2:0-10S, 90W-80W
nino1_2 = Region()
nino1_2.name = 'nino1_2'
nino1_2.description = 'Standard Nino 1+2 regions of equatorial E. Pacific'
nino1_2.lat_bnds = (-10, 0)
nino1_2.lon_bnds = (270, 280)
nino1_2.do_land_mask = False
# Nino 3: 5S-5N, 150W-90W
nino3 = Region()
nino3.name = nino3
nino3.description = 'Standard Nino 3 region of equatorial E. Pacific'
nino3.lat_bnds = (-5, 5)
nino3.lon_bnds = (210, 270)
nino3.do_land_mask = False
# Nino 3.4: 5S-5N, 170W-120W
nino3_4 = Region()
nino3_4.name='nino3.4'
nino3_4.description = 'Standard Nino 3.4 region of equatorial E. Pacific'
nino3_4.lat_bnds = (-5, 5)
nino3_4.lon_bnds = (190, 240)
nino3_4.do_land_mask = False
# Nino 4: 5S-5N, 160E-150W
nino4 = Region()
nino4.name = 'nino4'
nino4.description = 'Standard Nino 4 region of equatorial E. Pacific'
nino4.lat_bnds = (-5, 5)
nino4.lon_bnds = (160, 210)
nino4.do_land_mask = False
# Cloud seeding NP region: 24E-64E, 10N-30N
cld_seed_np = Region()
cld_seed_np.name = 'cld_seed_np'
cld_seed_np.description = 'North Pacific region of Hill & Ming 2012 GRL cloud brightening geoengineering study'
cld_seed_np.lat_bnds = (10, 30)
cld_seed_np.lon_bnds = (204, 244)
cld_seed_np.do_land_mask = 'ocean'
# Cloud seeding SP region: 60E-105E, 30S-5S
cld_seed_sp = Region()
cld_seed_sp.name = 'cld_seed_sp'
cld_seed_sp.description = 'South Pacific region of Hill & Ming 2012 GRL cloud brightening geoengineering study'
cld_seed_sp.lat_bnds = (-30, -5)
cld_seed_sp.lon_bnds = (240, 285)
cld_seed_sp.do_land_mask = 'ocean'
# Cloud seeding SA region: 18W-12E, 30S-5S
cld_seed_sa = Region()
cld_seed_sa.name = 'cld_seed_sa'
cld_seed_sa.description = 'South Atlantic region of Hill & Ming 2012 GRL cloud brightening geoengineering study'
cld_seed_sa.mask_bounds = [((-30, 5), (0, 12)),
                           ((-30, 5), (342, 360))]
cld_seed_sa.do_land_mask = 'ocean'
# Cloud seeding all 3 regions
cld_seed_all = Region()
cld_seed_all.name = 'cld_seed_all'
cld_seed_all.description = 'All 3 regions from Hill & Ming 2012 GRL'
cld_seed_all.mask_bounds = [((-30, 5), (0, 12)),
                            ((-30, 5), (342, 360)),
                            ((-30, -5), (240, 285)),
                            ((10, 30), (204, 244))]
cld_seed_all.do_land_mask = 'ocean'

# # Extratropics.
# extrop = Region()
# extrop.name = 'extrop'
# extrop.description = 'Extratropics (poleward of 30S/N)'
# extrop.lat_bnds = (-90, -30)
# extrop.lon_bnds = (0, 360)
# extrop.do_land_mask = False
# # NH tropics
# names.append('nh_tropics')
# lat_bnds = (0, 30)
# lon_bnds = (0, 360)
# mask = None
# # SH tropics
# names.append('sh_tropics')
# lat_bnds = (-30, 0)
# lon_bnds = (0, 360)
# mask = None
# # NH land
# names.append('nh_land')
# lat_bnds = (0, 90)
# lon_bnds = (0, 360)
# mask = do_land_mask
# # NH ocean
# names.append('nh_ocean')
# lat_bnds = (0, 90)
# lon_bnds = (0, 360)
# mask = 1. - do_land_mask
# # SH land
# names.append('sh_land')
# lat_bnds = (-90, 0)
# lon_bnds = (0, 360)
# mask = do_land_mask
# # SH ocean
# names.append('sh_ocean')
# lat_bnds = (-90, 0)
# lon_bnds = (0, 360)
# mask = 1. - do_land_mask
# # Extratrop land
# names.append('extratrop_land')
# lat_bnds = (30, -30)
# lon_bnds = (0, 360)
# mask = do_land_mask
# # Extratrop ocean
# names.append('extratrop_ocean')
# lat_bnds = (30, -30)
# lon_bnds = (0, 360)
# mask = 1. - do_land_mask
# # NH extratropics
# names.append('nh_extratrop')
# lat_bnds = (30, 90)
# lon_bnds = (0, 360)
# mask = 1. - do_land_mask
# # SH extratropics
# names.append('sh_extratrop')
# lat_bnds = (-90, -30)
# lon_bnds = (0, 360)
# mask = 1. - do_land_mask
