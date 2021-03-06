from aospy import Var
from aospy_user import calcs, units
from aospy_user.variables.universal.energy_native import (swdn_sfc, olr,
                                                          lwdn_sfc, lwup_sfc)
from aospy_user.variables.idealized_moist.energy import flux_t, flux_lhe


# Model native (or self-coded) diagnostics
umse_vint = Var(
    name='umse_vint',
    domain='atmos',
    description=('u*mse integrated vertically in the idealized model'),
    units=units.m3_s3_v,
    def_time=True,
    def_vert=False,
    def_lat=True,
    def_lon=True,
    in_nc_grid=False
)
vmse_vint = Var(
    name='vmse_vint',
    domain='atmos',
    description=('v*mse integrated vertically in the idealized model'),
    units=units.m3_s3_v,
    def_time=True,
    def_vert=False,
    def_lat=True,
    def_lon=True,
    in_nc_grid=False
)
omega_mse_vint = Var(
    name='omega_mse_vint',
    domain='atmos',
    description=('omega*mse integrated vertically in the idealized model'),
    units=units.J_Pa_kg_s_v,
    def_time=True,
    def_vert=False,
    def_lat=True,
    def_lon=True,
    in_nc_grid=False
)
umse = Var(
    name='umse',
    domain='atmos',
    description=('u*mse in idealized model'),
    units=units.m3_s3,
    def_time=True,
    def_vert=True,
    def_lat=True,
    def_lon=True,
    in_nc_grid=False
)
vmse = Var(
    name='vmse',
    domain='atmos',
    description=('v*mse in idealized model'),
    units=units.m3_s3,
    def_time=True,
    def_vert=True,
    def_lat=True,
    def_lon=True,
    in_nc_grid=False
)
omega_mse = Var(
    name='omega_mse',
    domain='atmos',
    description=('omega*mse in idealized model'),
    units=units.J_Pa_kg_s,
    def_time=True,
    def_vert=True,
    def_lat=True,
    def_lon=True,
    in_nc_grid=False
)


# Computed variables
aht_im = Var(
    name='aht_im',
    domain='atmos',
    description=('atmospheric heat transport'),
    variables=(swdn_sfc, olr, lwdn_sfc, lwup_sfc, flux_t, flux_lhe),
    def_time=True,
    def_vert=False,
    def_lat=True,
    def_lon=False,
    func=calcs.idealized_moist.energy.aht,
    units=units.W
)


# Continue supporting these?
dmv_dx_im = Var(
    name='dmv_dx_im',
    domain='atmos',
    description=('Zonal flux divergence of mse.'),
    variables=(umse,),
    def_time=True,
    def_vert=True,
    def_lat=True,
    def_lon=True,
    func=calcs.deprecated.mse_zonal_flux_divg_im,
    units=units.W
)
dmv_dx_v_im = Var(
    name='dmv_dx_v_im',
    domain='atmos',
    description=('Vertical integral of zonal flux divergence of mse.'),
    variables=(umse_vint,),
    def_time=True,
    def_vert=False,
    def_lat=True,
    def_lon=True,
    func=calcs.deprecated.mse_zonal_flux_divg_v_im,
    units=units.W
)
dmv_dy_v_im = Var(
    name='dmv_dy_v_im',
    domain='atmos',
    description=('Vertical integral of meridional flux divergence of mse.'),
    variables=(vmse_vint,),
    def_time=True,
    def_vert=False,
    def_lat=True,
    def_lon=True,
    func=calcs.deprecated.mse_merid_flux_divg_v_im,
    units=units.W
)
dmv_dy_im = Var(
    name='dmv_dy_im',
    domain='atmos',
    description=('Meridional flux divergence of mse.'),
    variables=(vmse,),
    def_time=True,
    def_vert=True,
    def_lat=True,
    def_lon=True,
    func=calcs.deprecated.mse_merid_flux_divg_im,
    units=units.W
)
