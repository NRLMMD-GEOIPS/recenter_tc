# # # This source code is protected under the license referenced at
# # # https://github.com/NRLMMD-GEOIPS.

#!/bin/bash

run_procflow \
    $GEOIPS_TESTDATA_DIR/test_data_viirs/data/jpss/20210209/073600/VJ102DNB.A2021040.0736.002.2021040145245.nc \
    $GEOIPS_TESTDATA_DIR/test_data_viirs/data/jpss/20210209/073600/VJ102IMG.A2021040.0736.002.2021040145245.nc \
    $GEOIPS_TESTDATA_DIR/test_data_viirs/data/jpss/20210209/073600/VJ102MOD.A2021040.0736.002.2021040145245.nc \
    $GEOIPS_TESTDATA_DIR/test_data_viirs/data/jpss/20210209/073600/VJ103DNB.A2021040.0736.002.2021040142228.nc \
    $GEOIPS_TESTDATA_DIR/test_data_viirs/data/jpss/20210209/073600/VJ103IMG.A2021040.0736.002.2021040142228.nc \
    $GEOIPS_TESTDATA_DIR/test_data_viirs/data/jpss/20210209/073600/VJ103MOD.A2021040.0736.002.2021040142228.nc \
    $GEOIPS_TESTDATA_DIR/test_data_viirs/data/jpss/20210209/074200/VJ102DNB.A2021040.0742.002.2021040143010.nc \
    $GEOIPS_TESTDATA_DIR/test_data_viirs/data/jpss/20210209/074200/VJ102IMG.A2021040.0742.002.2021040143010.nc \
    $GEOIPS_TESTDATA_DIR/test_data_viirs/data/jpss/20210209/074200/VJ102MOD.A2021040.0742.002.2021040143010.nc \
    $GEOIPS_TESTDATA_DIR/test_data_viirs/data/jpss/20210209/074200/VJ103DNB.A2021040.0742.002.2021040140938.nc \
    $GEOIPS_TESTDATA_DIR/test_data_viirs/data/jpss/20210209/074200/VJ103IMG.A2021040.0742.002.2021040140938.nc \
    $GEOIPS_TESTDATA_DIR/test_data_viirs/data/jpss/20210209/074200/VJ103MOD.A2021040.0742.002.2021040140938.nc \
    --procflow single_source \
    --reader_name viirs_netcdf \
    --product_name Infrared-Gray \
    --compare_path "$GEOIPS_PACKAGES_DIR/recenter_tc/tests/outputs/viirs.tc.Infrared-Gray.imagery_clean" \
    --output_formatter imagery_clean \
    --filename_formatter tc_clean_fname \
    --sector_adjuster recenter_tc \
    --metadata_filename_formatter metadata_default_fname \
    --metadata_output_formatter metadata_default \
    --trackfile_parser bdeck_parser \
    --trackfiles $GEOIPS_PACKAGES_DIR/geoips/tests/sectors/tc_bdecks/bsh192021.dat
ss_retval=$?

exit $((ss_retval))
