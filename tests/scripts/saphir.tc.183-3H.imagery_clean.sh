# # # This source code is subject to the license referenced at
# # # https://github.com/NRLMMD-GEOIPS.

#!/bin/bash

# This one has no output!!
run_procflow \
    $GEOIPS_TESTDATA_DIR/test_data_saphir/data/MT1SAPSL1A__1.09_000_1_19_I_2021_02_09_00_30_03_2021_02_09_01_11_16_48144_48144_497_33_33_KUX_00.h5 \
    --procflow single_source \
    --reader_name  saphir_hdf5 \
    --product_name "183-3H" \
    --compare_path "$GEOIPS_PACKAGES_DIR/recenter_tc/tests/outputs/saphir.tc.183-3H.imagery_clean" \
    --output_formatter imagery_clean \
    --filename_formatter tc_clean_fname \
    --metadata_filename_formatter metadata_default_fname \
    --metadata_output_formatter metadata_default \
    --trackfile_parser bdeck_parser \
    --trackfiles $GEOIPS_PACKAGES_DIR/geoips/tests/sectors/tc_bdecks/bsh192021.dat \
    --sector_adjuster recenter_tc
ss_retval=$?

exit $((ss_retval))
