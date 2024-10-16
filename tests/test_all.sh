#!/bin/bash

# # # This source code is protected under the license referenced at
# # # https://github.com/NRLMMD-GEOIPS.

# This should contain test calls to cover ALL required functionality tests for
# this repo.

# The $GEOIPS_PACKAGES_DIR/geoips tests modules sourced within this script handle:
   # setting up the appropriate associative arrays for tracking the overall return
   #   value,
   # calling the test scripts appropriately, and
   # setting the final return value.

if [[ ! -d $GEOIPS_PACKAGES_DIR/geoips ]]; then
    echo "Must CLONE geoips repository into \$GEOIPS_PACKAGES_DIR location"
    echo "to use test_all.sh testing utility."
    echo ""
    echo "export GEOIPS_PACKAGES_DIR=<path_to_geoips_cloned_packages>"
    echo "git clone https://github.com/NRLMMD-GEOIPS/geoips $GEOIPS_PACKAGES_DIR/geoips"
    echo ""
    exit 1
fi

repopath=`dirname $0`/../
pkgname=recenter_tc
. $GEOIPS_PACKAGES_DIR/geoips/tests/utils/test_all_pre.sh $pkgname

echo ""
# Note you must use the variable "call" in the for the loop
# "call" used in test_all_run.sh
for call in \
\
  "$GEOIPS_PACKAGES_DIR/geoips/tests/utils/check_code.sh all $repopath" \
  "$GEOIPS_PACKAGES_DIR/geoips/docs/build_docs.sh $repopath $pkgname html_only" \
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
    . $GEOIPS_PACKAGES_DIR/geoips/tests/utils/test_all_run.sh
done

. $GEOIPS_PACKAGES_DIR/geoips/tests/utils/test_all_post.sh
