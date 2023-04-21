# # # Distribution Statement A. Approved for public release. Distribution unlimited.
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

# This should contain test calls to cover ALL required functionality tests for the recenter_tc repo.

# The $GEOIPS tests modules sourced within this script handle:
   # setting up the appropriate associative arrays for tracking the overall return value,
   # calling the test scripts appropriately, and
   # setting the final return value.

# Note you must use the variable "call" in the for the loop

# NOTE atms DOESN'T WORK!!

. $GEOIPS/tests/utils/test_all_pre.sh recenter_tc

echo ""
# "call" used in test_all_run.sh
for call in \
\
            "$GEOIPS_PACKAGES_DIR/recenter_tc/tests/scripts/abi.tc.Visible.imagery_clean.sh" \
            "$GEOIPS_PACKAGES_DIR/recenter_tc/tests/scripts/ahi.tc.IR-BD.imagery_clean.sh" \
            "$GEOIPS_PACKAGES_DIR/recenter_tc/tests/scripts/amsr2.tc.color37.imagery_clean.sh" \
            "$GEOIPS_PACKAGES_DIR/recenter_tc/tests/scripts/amsr2.tc.windspeed.imagery_clean.sh" \
            "$GEOIPS_PACKAGES_DIR/recenter_tc/tests/scripts/amsub_hdf.tc.157V.imagery_clean.sh" \
            "$GEOIPS_PACKAGES_DIR/recenter_tc/tests/scripts/amsub_mirs.tc.89V.imagery_clean.sh" \
            "$GEOIPS_PACKAGES_DIR/recenter_tc/tests/scripts/ascat_uhr.tc.nrcs.imagery_clean.sh" \
            "$GEOIPS_PACKAGES_DIR/recenter_tc/tests/scripts/ascat_uhr.tc.windbarbs.imagery_clean.sh" \
            "$GEOIPS_PACKAGES_DIR/recenter_tc/tests/scripts/gmi.tc.89pct.imagery_clean.sh" \
            "$GEOIPS_PACKAGES_DIR/recenter_tc/tests/scripts/hy2b.tc.windspeed.imagery_clean.sh" \
            "$GEOIPS_PACKAGES_DIR/recenter_tc/tests/scripts/imerg.tc.Rain.imagery_clean.sh" \
            "$GEOIPS_PACKAGES_DIR/recenter_tc/tests/scripts/metopc_knmi_125.tc.windbarbs.imagery_clean.sh" \
            "$GEOIPS_PACKAGES_DIR/recenter_tc/tests/scripts/modis.tc.Infrared.imagery_clean.sh" \
            "$GEOIPS_PACKAGES_DIR/recenter_tc/tests/scripts/oscat.tc.windspeed.imagery_clean.sh" \
            "$GEOIPS_PACKAGES_DIR/recenter_tc/tests/scripts/saphir.tc.183-3H.imagery_clean.sh" \
            "$GEOIPS_PACKAGES_DIR/recenter_tc/tests/scripts/sar.tc.nrcs.imagery_clean.sh" \
            "$GEOIPS_PACKAGES_DIR/recenter_tc/tests/scripts/smap.tc.windspeed.imagery_clean.sh" \
            "$GEOIPS_PACKAGES_DIR/recenter_tc/tests/scripts/smos.tc.windspeed.imagery_clean.sh" \
            "$GEOIPS_PACKAGES_DIR/recenter_tc/tests/scripts/ssmis.tc.color91.imagery_clean.sh" \
            "$GEOIPS_PACKAGES_DIR/recenter_tc/tests/scripts/ssmi.tc.37pct.imagery_clean.sh" \
            "$GEOIPS_PACKAGES_DIR/recenter_tc/tests/scripts/viirs.tc.Infrared-Gray.imagery_clean.sh"
do
    . $GEOIPS/tests/utils/test_all_run.sh
done

. $GEOIPS/tests/utils/test_all_post.sh
