# # # This source code is protected under the license referenced at
# # # https://github.com/NRLMMD-GEOIPS.

#!/bin/bash

run_procflow \
    $GEOIPS_TESTDATA_DIR/test_data_scat/data/oscat_250/oscat_20210209_022459_scasa1_23155_o_250_2202_ovw_l2.nc \
    --procflow single_source \
    --reader_name scat_knmi_winds_netcdf \
    --product_name windspeed \
    --compare_path "$GEOIPS_PACKAGES_DIR/recenter_tc/tests/outputs/oscat.tc.windspeed.imagery_clean" \
    --output_formatter imagery_clean \
    --filename_formatter tc_clean_fname \
    --metadata_filename_formatter metadata_default_fname \
    --metadata_output_formatter metadata_default \
    --trackfile_parser bdeck_parser \
    --trackfiles $GEOIPS_PACKAGES_DIR/geoips/tests/sectors/tc_bdecks/bsh192021.dat \
    --sector_adjuster recenter_tc
ss_retval=$?

exit $((ss_retval))
