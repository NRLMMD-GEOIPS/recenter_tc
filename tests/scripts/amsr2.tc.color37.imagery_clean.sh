# # # This source code is protected under the license referenced at
# # # https://github.com/NRLMMD-GEOIPS.

#!/bin/bash

run_procflow \
    $GEOIPS_TESTDATA_DIR/test_data_amsr2/data/AMSR2-MBT_v2r2_GW1_s202005180620480_e202005180759470_c202005180937100.nc \
    --procflow single_source \
    --reader_name  amsr2_netcdf \
    --product_name color37 \
    --compare_path "$GEOIPS_PACKAGES_DIR/recenter_tc/tests/outputs/amsr2.tc.color37.imagery_clean" \
    --output_formatter imagery_clean \
    --filename_formatter tc_clean_fname \
    --metadata_filename_formatter metadata_default_fname \
    --metadata_output_formatter metadata_default \
    --trackfile_parser bdeck_parser \
    --trackfiles $GEOIPS_PACKAGES_DIR/geoips/tests/sectors/tc_bdecks/bio012020.dat \
    --sector_adjuster recenter_tc
ss_retval=$?

exit $((ss_retval))
