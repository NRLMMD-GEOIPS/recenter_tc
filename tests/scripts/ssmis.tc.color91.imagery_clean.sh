# # # This source code is protected under the license referenced at
# # # https://github.com/NRLMMD-GEOIPS.

#!/bin/bash

run_procflow \
    $GEOIPS_TESTDATA_DIR/test_data_ssmis/data/US058SORB-RAWspp.sdris_f16_d20200519_s084400_e102900_r85579_cfnoc.raw \
    --procflow single_source \
    --reader_name  ssmis_binary \
    --product_name color91 \
    --compare_path "$GEOIPS_PACKAGES_DIR/recenter_tc/tests/outputs/ssmis.tc.color91.imagery_clean" \
    --output_formatter imagery_clean \
    --filename_formatter tc_clean_fname \
    --metadata_filename_formatter metadata_default_fname \
    --metadata_output_formatter metadata_default \
    --trackfile_parser bdeck_parser \
    --trackfiles $GEOIPS_PACKAGES_DIR/geoips/tests/sectors/tc_bdecks/bio012020.dat \
    --sector_adjuster recenter_tc
ss_retval=$?

exit $((ss_retval))
