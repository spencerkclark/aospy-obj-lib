from aospy.model import Model
import aospy_user.runs.idealized_moist_rad as imr


idealized_moist_rad = Model(
    name='idealized_moist_rad',
    grid_file_paths=('/home/skc/archive/testing_2015_12_22/idealized_moist_rad/'
                     'gfdl.ncrc2-default-repro/1x0m360d_32pe/history/'
                     '00010101.atmos_1x20day.nc',
                     '/home/skc/scratch_nbs/04-18-2016/imr.landmask.nc'),
    runs=[imr.control, imr.conv_off,
          imr.double_CO2, imr.fixed_h2o, imr.fixed_h2o_2xCO2, imr.asym_e5,
          imr.asym_t5, imr.asym_e15, imr.asym_t15, imr.asym_t20,
          imr.asym_e18, imr.asym_t18, imr.asym_e15_conv_off,
          imr.asym_t15_conv_off, imr.eq_5, imr.eq_6, imr.eq_7, imr.eq_8,
          imr.eq_15, imr.eq_25, imr.eq_35, imr.asym_e5_conv_off,
          imr.asym_t5_conv_off, imr.asym_e18_conv_off, imr.asym_t18_conv_off,
          imr.asym_e5_conv_off_fixed_h2o, imr.asym_t5_conv_off_fixed_h2o,
          imr.asym_e15_conv_off_fixed_h2o, imr.asym_t15_conv_off_fixed_h2o,
          imr.asym_e18_conv_off_fixed_h2o, imr.asym_t18_conv_off_fixed_h2o,
          imr.asym_e15_fixed_h2o,
          imr.asym_t15_fixed_h2o, imr.asym_t15_net_zero_solar,
          imr.asym_e15_net_zero_solar, imr.fixed_h2o_conv_off,
          imr.asym_e5_fixed_h2o, imr.asym_t5_fixed_h2o, imr.asym_e18_fixed_h2o,
          imr.asym_t18_fixed_h2o, imr.land_test, imr.earth_land,
          imr.earth_land_seasons, imr.rect_seasons,
          imr.asym_t15_fixed_h2o_tropics, imr.asym_e15_fixed_h2o_tropics,
          imr.asym_t15_fixed_h2o_extratropics,
          imr.asym_e15_fixed_h2o_extratropics, imr.zero_o3,
          imr.anti_t15, imr.anti_e15, imr.anti_t15_fixed_h2o,
          imr.anti_e15_fixed_h2o, imr.anti_t15_fixed_h2o_tropics,
          imr.anti_e15_fixed_h2o_tropics, imr.anti_t15_fixed_h2o_extratropics,
          imr.anti_e15_fixed_h2o_extratropics, imr.control_gray,
          imr.control_gray_solar, imr.control_raw],
    default_runs=[]
)
