# # # This source code is subject to the license referenced at
# # # https://github.com/NRLMMD-GEOIPS.

#!/bin/bash

run_procflow \
    $GEOIPS_TESTDATA_DIR/test_data_scat/data/metopc_knmi_125/ascat_20210421_010000_metopc_12730_eps_o_coa_3203_ovw.l2.nc \
    --procflow single_source \
    --reader_name scat_knmi_winds_netcdf \
    --product_name windbarbs \
    --compare_path "$GEOIPS_PACKAGES_DIR/recenter_tc/tests/outputs/metopc_knmi_125.tc.windbarbs.imagery_clean" \
    --tc_spec_template tc_web_ascat_high_barbs \
    --output_formatter imagery_clean \
    --filename_formatter tc_clean_fname \
    --metadata_filename_formatter metadata_default_fname \
    --metadata_output_formatter metadata_default \
    --trackfile_parser bdeck_parser \
    --trackfiles $GEOIPS_PACKAGES_DIR/geoips/tests/sectors/tc_bdecks/bwp022021.dat \
    --sector_adjuster recenter_tc
ss_retval=$?

exit $((ss_retval))
