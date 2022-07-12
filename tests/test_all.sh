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

# This should contain test calls to cover ALL required functionality tests for the recenter_tc repo.

# The $GEOIPS tests modules sourced within this script handle:
   # setting up the appropriate associative arrays for tracking the overall return value,
   # calling the test scripts appropriately, and 
   # setting the final return value.

# Note you must use the variable "call" in the for the loop

# NOTE saphir and atms DON'T WORK!!

. $GEOIPS/tests/utils/test_all_pre.sh recenter_tc

echo ""
# "call" used in test_all_run.sh
for call in \
\
            "$GEOIPS_PACKAGES_DIR/recenter_tc/tests/scripts/abi.sh" \
            "$GEOIPS_PACKAGES_DIR/recenter_tc/tests/scripts/ahi.sh" \
            "$GEOIPS_PACKAGES_DIR/recenter_tc/tests/scripts/amsr2.sh" \
            "$GEOIPS_PACKAGES_DIR/recenter_tc/tests/scripts/amsr2_winds.sh" \
            "$GEOIPS_PACKAGES_DIR/recenter_tc/tests/scripts/amsub_hdf.sh" \
            "$GEOIPS_PACKAGES_DIR/recenter_tc/tests/scripts/amsub_mirs.sh" \
            "$GEOIPS_PACKAGES_DIR/recenter_tc/tests/scripts/ascat_uhr_nrcs.sh" \
            "$GEOIPS_PACKAGES_DIR/recenter_tc/tests/scripts/ascat_uhr.sh" \
            "$GEOIPS_PACKAGES_DIR/recenter_tc/tests/scripts/gmi.sh" \
            "$GEOIPS_PACKAGES_DIR/recenter_tc/tests/scripts/hy2.sh" \
            "$GEOIPS_PACKAGES_DIR/recenter_tc/tests/scripts/imerg.sh" \
            "$GEOIPS_PACKAGES_DIR/recenter_tc/tests/scripts/metopc_knmi_125.sh" \
            "$GEOIPS_PACKAGES_DIR/recenter_tc/tests/scripts/modis.sh" \
            "$GEOIPS_PACKAGES_DIR/recenter_tc/tests/scripts/oscat.sh" \
            "$GEOIPS_PACKAGES_DIR/recenter_tc/tests/scripts/sar.sh" \
            "$GEOIPS_PACKAGES_DIR/recenter_tc/tests/scripts/smap.sh" \
            "$GEOIPS_PACKAGES_DIR/recenter_tc/tests/scripts/smos.sh" \
            "$GEOIPS_PACKAGES_DIR/recenter_tc/tests/scripts/ssmi.sh" \
            "$GEOIPS_PACKAGES_DIR/recenter_tc/tests/scripts/ssmis.sh" \
            "$GEOIPS_PACKAGES_DIR/recenter_tc/tests/scripts/viirs.sh"
do
    . $GEOIPS/tests/utils/test_all_run.sh
done

. $GEOIPS/tests/utils/test_all_post.sh
