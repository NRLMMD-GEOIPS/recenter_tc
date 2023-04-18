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

run_procflow \
    $GEOIPS_BASEDIR/test_data/test_data_viirs/data/jpss/20210209/073600/VJ102DNB.A2021040.0736.002.2021040145245.nc \
    $GEOIPS_BASEDIR/test_data/test_data_viirs/data/jpss/20210209/073600/VJ102IMG.A2021040.0736.002.2021040145245.nc \
    $GEOIPS_BASEDIR/test_data/test_data_viirs/data/jpss/20210209/073600/VJ102MOD.A2021040.0736.002.2021040145245.nc \
    $GEOIPS_BASEDIR/test_data/test_data_viirs/data/jpss/20210209/073600/VJ103DNB.A2021040.0736.002.2021040142228.nc \
    $GEOIPS_BASEDIR/test_data/test_data_viirs/data/jpss/20210209/073600/VJ103IMG.A2021040.0736.002.2021040142228.nc \
    $GEOIPS_BASEDIR/test_data/test_data_viirs/data/jpss/20210209/073600/VJ103MOD.A2021040.0736.002.2021040142228.nc \
    $GEOIPS_BASEDIR/test_data/test_data_viirs/data/jpss/20210209/074200/VJ102DNB.A2021040.0742.002.2021040143010.nc \
    $GEOIPS_BASEDIR/test_data/test_data_viirs/data/jpss/20210209/074200/VJ102IMG.A2021040.0742.002.2021040143010.nc \
    $GEOIPS_BASEDIR/test_data/test_data_viirs/data/jpss/20210209/074200/VJ102MOD.A2021040.0742.002.2021040143010.nc \
    $GEOIPS_BASEDIR/test_data/test_data_viirs/data/jpss/20210209/074200/VJ103DNB.A2021040.0742.002.2021040140938.nc \
    $GEOIPS_BASEDIR/test_data/test_data_viirs/data/jpss/20210209/074200/VJ103IMG.A2021040.0742.002.2021040140938.nc \
    $GEOIPS_BASEDIR/test_data/test_data_viirs/data/jpss/20210209/074200/VJ103MOD.A2021040.0742.002.2021040140938.nc \
    --procflow single_source \
    --reader_name viirs_netcdf \
    --product_name Infrared-Gray \
    --compare_path "$GEOIPS_BASEDIR/geoips_packages/recenter_tc/tests/outputs/viirs.tc.Infrared-Gray.imagery_clean" \
    --output_formatter imagery_clean \
    --filename_formatter tc_clean_fname \
    --adjust_area_def recenter_tc \
    --metadata_filename_formatter metadata_default_fname \
    --metadata_output_formatter metadata_default \
    --trackfile_parser bdeck_parser \
    --trackfiles $GEOIPS/tests/sectors/tc_bdecks/bsh192021.dat
ss_retval=$?

exit $((ss_retval))
