# # # This source code is protected under the license referenced at
# # # https://github.com/NRLMMD-GEOIPS.

#!/bin/bash

run_procflow \
    $GEOIPS_TESTDATA_DIR/test_data_hy2/data/hscat_20211202_080644_hy_2b__15571_o_250_2204_ovw_l2.nc \
    --procflow single_source \
    --reader_name scat_knmi_winds_netcdf \
    --product_name windspeed \
    --compare_path "$GEOIPS_PACKAGES_DIR/recenter_tc/tests/outputs/hy2b.tc.windspeed.imagery_clean" \
    --output_formatter imagery_clean \
    --filename_formatter tc_clean_fname \
    --metadata_filename_formatter metadata_default_fname \
    --metadata_output_formatter metadata_default \
    --trackfile_parser bdeck_parser \
    --trackfiles $GEOIPS_PACKAGES_DIR/geoips/tests/sectors/tc_bdecks/bwp272021.dat \
    --sector_adjuster recenter_tc
ss_retval=$?

exit $((ss_retval))
