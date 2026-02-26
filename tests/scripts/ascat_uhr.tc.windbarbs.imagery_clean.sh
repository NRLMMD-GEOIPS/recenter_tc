# # # This source code is subject to the license referenced at
# # # https://github.com/NRLMMD-GEOIPS.

#!/bin/bash

geoips run single_source \
    $GEOIPS_TESTDATA_DIR/test_data_scat/data/20210421_metopc_byu_uhr_tc2021wp02surigae/210421_0142_12730_SURIGAE_210421_0000.WRave3.nc \
    --procflow single_source \
    --reader_name  ascat_uhr_netcdf \
    --product_name windbarbs \
    --tc_spec_template tc_web_ascatuhr_barbs \
    --compare_path "$GEOIPS_PACKAGES_DIR/recenter_tc/tests/outputs/ascat_uhr.tc.windbarbs.imagery_clean" \
    --output_formatter imagery_clean \
    --filename_formatter tc_clean_fname \
    --metadata_filename_formatter metadata_default_fname \
    --metadata_output_formatter metadata_default \
    --trackfile_parser bdeck_parser \
    --trackfiles $GEOIPS_PACKAGES_DIR/geoips/tests/sectors/tc_bdecks/bwp022021.dat \
    --sector_adjuster recenter_tc
ss_retval=$?

exit $((ss_retval))
