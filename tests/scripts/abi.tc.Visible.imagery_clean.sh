# # # Distribution Statement A. Approved for public release. Distribution unlimited.
# # #
# # # Author:
# # # Naval Research Laboratory, Marine Meteorology Division
# # #
# # # This program is free software: you can redistribute it and/or modify it under
# # # the terms of the NRLMMD License included with this program. This program is
# # # distributed WITHOUT ANY WARRANTY; without even the implied warranty of
# # # MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the included license
# # # for more details. If you did not receive the license, for more information see:
# # # https://github.com/U-S-NRL-Marine-Meteorology-Division/

#!/bin/bash

run_procflow \
    $GEOIPS_TESTDATA_DIR/test_data_noaa_aws/data/goes16/20200918/1950/OR_ABI-L1b-RadF-M6C01_G16_s20202621950205_e20202621959513_c20202621959567.nc \
    $GEOIPS_TESTDATA_DIR/test_data_noaa_aws/data/goes16/20200918/1950/OR_ABI-L1b-RadF-M6C02_G16_s20202621950205_e20202621959513_c20202621959546.nc \
    $GEOIPS_TESTDATA_DIR/test_data_noaa_aws/data/goes16/20200918/1950/OR_ABI-L1b-RadF-M6C03_G16_s20202621950205_e20202621959513_c20202621959570.nc \
    $GEOIPS_TESTDATA_DIR/test_data_noaa_aws/data/goes16/20200918/1950/OR_ABI-L1b-RadF-M6C04_G16_s20202621950205_e20202621959513_c20202621959534.nc \
    $GEOIPS_TESTDATA_DIR/test_data_noaa_aws/data/goes16/20200918/1950/OR_ABI-L1b-RadF-M6C05_G16_s20202621950205_e20202621959513_c20202621959562.nc \
    $GEOIPS_TESTDATA_DIR/test_data_noaa_aws/data/goes16/20200918/1950/OR_ABI-L1b-RadF-M6C06_G16_s20202621950205_e20202621959518_c20202621959556.nc \
    $GEOIPS_TESTDATA_DIR/test_data_noaa_aws/data/goes16/20200918/1950/OR_ABI-L1b-RadF-M6C07_G16_s20202621950205_e20202621959524_c20202621959577.nc \
    $GEOIPS_TESTDATA_DIR/test_data_noaa_aws/data/goes16/20200918/1950/OR_ABI-L1b-RadF-M6C08_G16_s20202621950205_e20202621959513_c20202621959574.nc \
    $GEOIPS_TESTDATA_DIR/test_data_noaa_aws/data/goes16/20200918/1950/OR_ABI-L1b-RadF-M6C09_G16_s20202621950205_e20202621959518_c20202621959588.nc \
    $GEOIPS_TESTDATA_DIR/test_data_noaa_aws/data/goes16/20200918/1950/OR_ABI-L1b-RadF-M6C10_G16_s20202621950205_e20202621959524_c20202621959578.nc \
    $GEOIPS_TESTDATA_DIR/test_data_noaa_aws/data/goes16/20200918/1950/OR_ABI-L1b-RadF-M6C11_G16_s20202621950205_e20202621959513_c20202621959583.nc \
    $GEOIPS_TESTDATA_DIR/test_data_noaa_aws/data/goes16/20200918/1950/OR_ABI-L1b-RadF-M6C12_G16_s20202621950205_e20202621959518_c20202621959574.nc \
    $GEOIPS_TESTDATA_DIR/test_data_noaa_aws/data/goes16/20200918/1950/OR_ABI-L1b-RadF-M6C13_G16_s20202621950205_e20202621959525_c20202622000005.nc \
    $GEOIPS_TESTDATA_DIR/test_data_noaa_aws/data/goes16/20200918/1950/OR_ABI-L1b-RadF-M6C14_G16_s20202621950205_e20202621959513_c20202622000009.nc \
    $GEOIPS_TESTDATA_DIR/test_data_noaa_aws/data/goes16/20200918/1950/OR_ABI-L1b-RadF-M6C15_G16_s20202621950205_e20202621959518_c20202621959594.nc \
    $GEOIPS_TESTDATA_DIR/test_data_noaa_aws/data/goes16/20200918/1950/OR_ABI-L1b-RadF-M6C16_G16_s20202621950205_e20202621959524_c20202622000001.nc \
    --procflow single_source \
    --reader_name abi_netcdf \
    --resampled_read \
    --product_name Visible \
    --compare_path "$GEOIPS_PACKAGES_DIR/recenter_tc/tests/outputs/abi.tc.Visible.imagery_clean" \
    --output_formatter imagery_clean \
    --filename_formatter tc_clean_fname \
    --metadata_filename_formatter metadata_default_fname \
    --metadata_output_formatter metadata_default \
    --trackfile_parser bdeck_parser \
    --trackfiles $GEOIPS_PACKAGES_DIR/geoips/tests/sectors/tc_bdecks/bal202020.dat
ss_retval=$?

exit $((ss_retval))
