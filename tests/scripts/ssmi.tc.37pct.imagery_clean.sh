# # # This source code is subject to the license referenced at
# # # https://github.com/NRLMMD-GEOIPS.

#!/bin/bash

geoips run single_source \
    $GEOIPS_TESTDATA_DIR/test_data_ssmi/data/US058SORB-DEFspp.sdrmi_f15_d20200519_s080800_e095300_r05633_cfnoc.def \
    --procflow single_source \
    --reader_name  ssmi_binary \
    --product_name 37pct \
    --compare_path "$GEOIPS_PACKAGES_DIR/recenter_tc/tests/outputs/ssmi.tc.37pct.imagery_clean" \
    --output_formatter imagery_clean \
    --filename_formatter tc_clean_fname \
    --metadata_filename_formatter metadata_default_fname \
    --metadata_output_formatter metadata_default \
    --trackfile_parser bdeck_parser \
    --trackfiles $GEOIPS_PACKAGES_DIR/geoips/tests/sectors/tc_bdecks/bio012020.dat \
    --sector_adjuster recenter_tc
ss_retval=$?

exit $((ss_retval))
