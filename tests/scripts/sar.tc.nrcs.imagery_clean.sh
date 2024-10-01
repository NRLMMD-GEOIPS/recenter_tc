# # # This source code is protected under the license referenced at
# # # https://github.com/NRLMMD-GEOIPS.

#!/bin/bash

run_procflow \
    $GEOIPS_TESTDATA_DIR/test_data_sar/data/STAR_SAR_20181025203206_WP312018_31W_FIX_3km.nc \
    --procflow single_source \
    --reader_name sar_winds_netcdf \
    --product_name nrcs \
    --compare_path "$GEOIPS_PACKAGES_DIR/recenter_tc/tests/outputs/sar.tc.nrcs.imagery_clean" \
    --output_formatter imagery_clean \
    --filename_formatter tc_clean_fname \
    --sector_adjuster recenter_tc \
    --metadata_filename_formatter metadata_default_fname \
    --metadata_output_formatter metadata_default \
    --trackfile_parser bdeck_parser \
    --trackfiles $GEOIPS_PACKAGES_DIR/geoips/tests/sectors/tc_bdecks/bwp312018.dat

ss_retval=$?

exit $((ss_retval))
