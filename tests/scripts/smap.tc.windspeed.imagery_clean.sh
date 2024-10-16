# # # This source code is protected under the license referenced at
# # # https://github.com/NRLMMD-GEOIPS.

#!/bin/bash

run_procflow \
    $GEOIPS_TESTDATA_DIR/test_data_smap/data/RSS_smap_wind_daily_2021_09_26_NRT_v01.0.nc \
    --procflow single_source \
    --reader_name smap_remss_winds_netcdf \
    --product_name windspeed \
    --compare_path "$GEOIPS_PACKAGES_DIR/recenter_tc/tests/outputs/smap.tc.windspeed.imagery_clean" \
    --output_formatter imagery_clean \
    --filename_formatter tc_clean_fname \
    --metadata_filename_formatter metadata_default_fname \
    --metadata_output_formatter metadata_default \
    --trackfile_parser bdeck_parser \
    --trackfiles $GEOIPS_PACKAGES_DIR/geoips/tests/sectors/tc_bdecks/bwp202021.dat \
    --sector_adjuster recenter_tc
ss_retval=$?

exit $((ss_retval))
