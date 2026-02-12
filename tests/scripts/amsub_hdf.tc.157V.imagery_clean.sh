# # # This source code is subject to the license referenced at
# # # https://github.com/NRLMMD-GEOIPS.

#!/bin/bash

geoips run single_source \
    $GEOIPS_TESTDATA_DIR/test_data_amsub/data/NPR.MHOP.NP.D20134.S2106.E2252.B5805153.NS \
    --procflow single_source \
    --reader_name amsub_hdf \
    --product_name 157V \
    --compare_path "$GEOIPS_PACKAGES_DIR/recenter_tc/tests/outputs/amsub_hdf.tc.157V.imagery_clean" \
    --output_formatter imagery_clean \
    --filename_formatter tc_clean_fname \
    --sector_adjuster recenter_tc \
    --metadata_filename_formatter metadata_default_fname \
    --metadata_output_formatter metadata_default \
    --trackfile_parser bdeck_parser \
    --trackfiles $GEOIPS_PACKAGES_DIR/geoips/tests/sectors/tc_bdecks/bwp012020.dat
ss_retval=$?

exit $((ss_retval))
