# # # This source code is protected under the license referenced at
# # # https://github.com/NRLMMD-GEOIPS.

#!/bin/bash

run_procflow \
    $GEOIPS_TESTDATA_DIR/test_data_modis/data/aqua/20210104/200500/MYD021KM.A2021004.2005.061.NRT.hdf \
    $GEOIPS_TESTDATA_DIR/test_data_modis/data/aqua/20210104/200500/MYD03.A2021004.2005.061.NRT.hdf \
    $GEOIPS_TESTDATA_DIR/test_data_modis/data/aqua/20210104/200500/MYD14.A2021004.2005.006.NRT.hdf \
    $GEOIPS_TESTDATA_DIR/test_data_modis/data/aqua/20210104/201000/MYD021KM.A2021004.2010.061.NRT.hdf \
    $GEOIPS_TESTDATA_DIR/test_data_modis/data/aqua/20210104/201000/MYD03.A2021004.2010.061.NRT.hdf \
    $GEOIPS_TESTDATA_DIR/test_data_modis/data/aqua/20210104/201000/MYD14.A2021004.2010.006.NRT.hdf \
    $GEOIPS_TESTDATA_DIR/test_data_modis/data/aqua/20210104/201500/MYD021KM.A2021004.2015.061.NRT.hdf \
    $GEOIPS_TESTDATA_DIR/test_data_modis/data/aqua/20210104/201500/MYD03.A2021004.2015.061.NRT.hdf \
    $GEOIPS_TESTDATA_DIR/test_data_modis/data/aqua/20210104/201500/MYD14.A2021004.2015.006.NRT.hdf \
    --procflow single_source \
    --reader_name modis_hdf4\
    --product_name Infrared \
    --compare_path "$GEOIPS_PACKAGES_DIR/recenter_tc/tests/outputs/modis.tc.Infrared.imagery_clean" \
    --output_formatter imagery_clean \
    --filename_formatter tc_clean_fname \
    --sector_adjuster recenter_tc \
    --metadata_filename_formatter metadata_default_fname \
    --metadata_output_formatter metadata_default \
    --trackfile_parser bdeck_parser \
    --trackfiles $GEOIPS_PACKAGES_DIR/geoips/tests/sectors/tc_bdecks/bsh082021.dat
ss_retval=$?

exit $((ss_retval))
