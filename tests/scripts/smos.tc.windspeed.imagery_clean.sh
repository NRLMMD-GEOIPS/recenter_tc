# # # This source code is protected under the license referenced at
# # # https://github.com/NRLMMD-GEOIPS.

#!/bin/bash

run_procflow \
    $GEOIPS_TESTDATA_DIR/test_data_smos/data/SM_OPER_MIR_SCNFSW_20200216T120839_20200216T135041_110_001_7.nc \
    --procflow single_source \
    --reader_name smos_winds_netcdf \
    --product_name windspeed \
    --compare_path "$GEOIPS_PACKAGES_DIR/recenter_tc/tests/outputs/smos.tc.windspeed.imagery_clean" \
    --output_formatter imagery_clean \
    --filename_formatter tc_clean_fname \
    --metadata_filename_formatter metadata_default_fname \
    --metadata_output_formatter metadata_default \
    --trackfile_parser bdeck_parser \
    --trackfiles $GEOIPS_PACKAGES_DIR/geoips/tests/sectors/tc_bdecks/bsh162020.dat \
    --sector_adjuster recenter_tc
ss_retval=$?

exit $((ss_retval))
