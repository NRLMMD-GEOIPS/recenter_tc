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
    $GEOIPS_TESTDATA_DIR/test_data_sar/data/STAR_SAR_20181025203206_WP312018_31W_FIX_3km.nc \
    --procflow single_source \
    --reader_name sar_winds_netcdf \
    --product_name nrcs \
    --compare_path "$GEOIPS_PACKAGES_DIR/recenter_tc/tests/outputs/sar.tc.nrcs.imagery_clean" \
    --output_formatter imagery_clean \
    --filename_formatter tc_clean_fname \
    --adjust_area_def recenter_tc \
    --metadata_filename_formatter metadata_default_fname \
    --metadata_output_formatter metadata_default \
    --trackfile_parser bdeck_parser \
    --trackfiles $GEOIPS/tests/sectors/tc_bdecks/bwp312018.dat

ss_retval=$?

exit $((ss_retval))
