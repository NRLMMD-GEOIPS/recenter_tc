# # # Distribution Statement A. Approved for public release. Distribution unlimited.
# # # 
# # # Author:
# # # Naval Research Laboratory, Marine Meteorology Division
# # # 
# # # This program is free software:
# # # you can redistribute it and/or modify it under the terms
# # # of the NRLMMD License included with this program.
# # # 
# # # If you did not receive the license, see
# # # https://github.com/U-S-NRL-Marine-Meteorology-Division/
# # # for more information.
# # # 
# # # This program is distributed WITHOUT ANY WARRANTY;
# # # without even the implied warranty of MERCHANTABILITY
# # # or FITNESS FOR A PARTICULAR PURPOSE.
# # # See the included license for more details.

#!/bin/bash

run_procflow \
    ${GEOIPS_BASEDIR}/test_data/test_data_hy2/data/hscat_20211202_080644_hy_2b__15571_o_250_2204_ovw_l2.nc \
    --procflow single_source \
    --reader_name scat_knmi_winds_netcdf \
    --product_name windspeed \
    --compare_path "$GEOIPS_BASEDIR/geoips_packages/recenter_tc/tests/outputs/hy2b_<product>" \
    --output_format imagery_clean \
    --filename_format tc_clean_fname \
    --metadata_filename_format metadata_default_fname \
    --metadata_output_format metadata_default \
    --trackfile_parser bdeck_parser \
    --trackfiles $GEOIPS/tests/sectors/tc_bdecks/bwp272021.dat \
    --adjust_area_def recenter_tc
ss_retval=$?

exit $((ss_retval))
