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

run_procflow \
    $GEOIPS_BASEDIR/test_data/test_data_modis/data/aqua/20210104/200500/MYD021KM.A2021004.2005.061.NRT.hdf \
    $GEOIPS_BASEDIR/test_data/test_data_modis/data/aqua/20210104/200500/MYD03.A2021004.2005.061.NRT.hdf \
    $GEOIPS_BASEDIR/test_data/test_data_modis/data/aqua/20210104/200500/MYD14.A2021004.2005.006.NRT.hdf \
    $GEOIPS_BASEDIR/test_data/test_data_modis/data/aqua/20210104/201000/MYD021KM.A2021004.2010.061.NRT.hdf \
    $GEOIPS_BASEDIR/test_data/test_data_modis/data/aqua/20210104/201000/MYD03.A2021004.2010.061.NRT.hdf \
    $GEOIPS_BASEDIR/test_data/test_data_modis/data/aqua/20210104/201000/MYD14.A2021004.2010.006.NRT.hdf \
    $GEOIPS_BASEDIR/test_data/test_data_modis/data/aqua/20210104/201500/MYD021KM.A2021004.2015.061.NRT.hdf \
    $GEOIPS_BASEDIR/test_data/test_data_modis/data/aqua/20210104/201500/MYD03.A2021004.2015.061.NRT.hdf \
    $GEOIPS_BASEDIR/test_data/test_data_modis/data/aqua/20210104/201500/MYD14.A2021004.2015.006.NRT.hdf \
    --procflow single_source \
    --reader_name modis_hdf4\
    --product_name Infrared \
    --compare_path "$GEOIPS_BASEDIR/geoips_packages/recenter_tc/tests/outputs/modis_<product>" \
    --output_format imagery_clean \
    --filename_format tc_clean_fname \
    --adjust_area_def recenter_tc \
    --metadata_filename_format metadata_default_fname \
    --metadata_output_format metadata_default \
    --trackfile_parser bdeck_parser \
    --trackfiles $GEOIPS/tests/sectors/tc_bdecks/bsh082021.dat
ss_retval=$?

exit $((ss_retval))
