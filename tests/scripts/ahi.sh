# # # Distribution Statement A. Approved for public release. Distribution unlimited.
# # # 
# # # Author:
# # # Naval Research Laboratory, Marine Meteorology Division
# # # 
# # # This program is free software:
# # # you can redistribute it and/or modify it under the terms
# # # of the NRLMMD License included with this program.
# # # 
# # # If you did not receive the license, see
# # # https://github.com/U-S-NRL-Marine-Meteorology-Division/
# # # for more information.
# # # 
# # # This program is distributed WITHOUT ANY WARRANTY;
# # # without even the implied warranty of MERCHANTABILITY
# # # or FITNESS FOR A PARTICULAR PURPOSE.
# # # See the included license for more details.

#!/bin/bash

# 160 files - 10 per channel
run_procflow \
    $GEOIPS_BASEDIR/test_data/test_data_ahi_day/data/20200405_0000/HS_H08_20200405_0000_B*_FLDK_R*_S*.DAT \
    --procflow single_source \
    --reader_name ahi_hsd \
    --product_name IR-BD \
    --compare_path "$GEOIPS_BASEDIR/geoips_packages/recenter_tc/tests/outputs/ahi_<product>" \
    --output_format imagery_clean \
    --filename_format tc_clean_fname \
    --adjust_area_def recenter_tc \
    --metadata_filename_format metadata_default_fname \
    --metadata_output_format metadata_default \
    --trackfile_parser bdeck_parser \
    --trackfiles $GEOIPS/tests/sectors/tc_bdecks/bsh252020.dat
ss_retval=$?

exit $((ss_retval))
