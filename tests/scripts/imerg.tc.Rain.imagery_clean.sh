# # # This source code is subject to the license referenced at
# # # https://github.com/NRLMMD-GEOIPS.

#!/bin/bash

run_procflow \
    $GEOIPS_TESTDATA_DIR/test_data_gpm/data/3B-HHR-L.MS.MRG.3IMERG.20200917-S170000-E172959.1020.V06B.RT-H5 \
    --procflow single_source \
    --reader_name  imerg_hdf5 \
    --product_name Rain \
    --compare_path "$GEOIPS_PACKAGES_DIR/recenter_tc/tests/outputs/imerg.tc.Rain.imagery_clean" \
    --output_formatter imagery_clean \
    --filename_formatter tc_clean_fname \
    --metadata_filename_formatter metadata_default_fname \
    --metadata_output_formatter metadata_default \
    --trackfile_parser bdeck_parser \
    --trackfiles $GEOIPS_PACKAGES_DIR/geoips/tests/sectors/tc_bdecks/bal202020.dat \
    --sector_adjuster recenter_tc
ss_retval=$?

exit $((ss_retval))
