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
    $GEOIPS_TESTDATA_DIR/test_data_scat/data/metopc_knmi_125/ascat_20210421_010000_metopc_12730_eps_o_coa_3203_ovw.l2.nc \
    --procflow single_source \
    --reader_name scat_knmi_winds_netcdf \
    --product_name windbarbs \
    --compare_path "$GEOIPS_PACKAGES_DIR/recenter_tc/tests/outputs/metopc_knmi_125.tc.windbarbs.imagery_clean" \
    --tc_template_yaml $GEOIPS/geoips/plugins/yaml/sectors/dynamic/tc_web_ascat_high_barbs_template.yaml \
    --output_formatter imagery_clean \
    --filename_formatter tc_clean_fname \
    --metadata_filename_formatter metadata_default_fname \
    --metadata_output_formatter metadata_default \
    --trackfile_parser bdeck_parser \
    --trackfiles $GEOIPS/tests/sectors/tc_bdecks/bwp022021.dat \
    --sector_adjuster recenter_tc
ss_retval=$?

exit $((ss_retval))
