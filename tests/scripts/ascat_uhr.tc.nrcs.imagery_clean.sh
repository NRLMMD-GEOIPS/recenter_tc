# # # Distribution Statement A. Approved for public release. Distribution is unlimited.
# # #
# # # Author:
# # # Naval Research Laboratory, Marine Meteorology Division
# # #
# # # This program is free software: you can redistribute it and/or modify it under
# # # the terms of the NRLMMD License included with this program. This program is
# # # distributed WITHOUT ANY WARRANTY; without even the implied warranty of
# # # MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the included license
# # # for more details. If you did not receive the license, for more information see:
# # # https://github.com/U-S-NRL-Marine-Meteorology-Division/

#!/bin/bash

run_procflow \
    $GEOIPS_TESTDATA_DIR/test_data_scat/data/20210421_metopc_byu_uhr_tc2021wp02surigae/210421_0142_12730_SURIGAE_210421_0000.avewr.nc \
    --procflow single_source \
    --reader_name  ascat_uhr_netcdf \
    --product_name nrcs \
    --compare_path "$GEOIPS_PACKAGES_DIR/recenter_tc/tests/outputs/ascat_uhr.tc.nrcs.imagery_clean" \
    --output_formatter imagery_clean \
    --filename_formatter tc_clean_fname \
    --metadata_filename_formatter metadata_default_fname \
    --metadata_output_formatter metadata_default \
    --trackfile_parser bdeck_parser \
    --trackfiles $GEOIPS_PACKAGES_DIR/geoips/tests/sectors/tc_bdecks/bwp022021.dat \
    --sector_adjuster recenter_tc
ss_retval=$?

exit $((ss_retval))
