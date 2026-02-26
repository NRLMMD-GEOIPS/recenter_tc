# # # This source code is subject to the license referenced at
# # # https://github.com/NRLMMD-GEOIPS.

#!/bin/bash

# This one doesn't work!!!
geoips run single_source \
    $GEOIPS_TESTDATA_DIR/test_data_atms/data/j01/20210809_0838/* \
    --procflow single_source \
    --reader_name  atms_hdf5 \
    --product_name 165H \
    --compare_path "$GEOIPS_PACKAGES_DIR/recenter_tc/tests/outputs/atms.tc.165H.imagery_clean" \
    --output_formatter imagery_clean \
    --filename_formatter tc_clean_fname \
    --metadata_filename_formatter metadata_default_fname \
    --metadata_output_formatter metadata_default \
    --trackfile_parser bdeck_parser \
    --trackfiles $GEOIPS_PACKAGES_DIR/geoips/tests/sectors/tc_bdecks/bep112021.dat \
    --sector_adjuster recenter_tc
ss_retval=$?

exit $((ss_retval))
