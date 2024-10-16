# # # This source code is protected under the license referenced at
# # # https://github.com/NRLMMD-GEOIPS.

#!/bin/bash

# 160 files - 10 per channel
run_procflow \
    $GEOIPS_TESTDATA_DIR/test_data_ahi_day/data/20200405_0000/HS_H08_20200405_0000_B*_FLDK_R*_S*.DAT \
    --procflow single_source \
    --reader_name ahi_hsd \
    --product_name IR-BD \
    --compare_path "$GEOIPS_PACKAGES_DIR/recenter_tc/tests/outputs/ahi.tc.IR-BD.imagery_clean" \
    --output_formatter imagery_clean \
    --filename_formatter tc_clean_fname \
    --metadata_filename_formatter metadata_default_fname \
    --metadata_output_formatter metadata_default \
    --trackfile_parser bdeck_parser \
    --trackfiles $GEOIPS_PACKAGES_DIR/geoips/tests/sectors/tc_bdecks/bsh252020.dat \
    --sector_adjuster recenter_tc
ss_retval=$?

exit $((ss_retval))
