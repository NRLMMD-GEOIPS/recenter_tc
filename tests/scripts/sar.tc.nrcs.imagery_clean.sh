# # # This source code is subject to the license referenced at
# # # https://github.com/NRLMMD-GEOIPS.

#!/bin/bash

geoips run single_source \
    $GEOIPS_TESTDATA_DIR/test_data_sar/data/STAR_SAR_20181025203206_WP312018_31W_FIX_3km.nc \
    --procflow single_source \
    --reader_name sar_winds_netcdf \
    --product_name nrcs \
    --compare_path "$GEOIPS_PACKAGES_DIR/recenter_tc/tests/outputs/sar.tc.nrcs.imagery_clean" \
    --output_formatter imagery_clean \
    --filename_formatter tc_clean_fname \
    --sector_adjuster recenter_tc \
    --metadata_filename_formatter metadata_default_fname \
    --metadata_output_formatter metadata_default \
    --trackfile_parser bdeck_parser \
    --trackfiles $GEOIPS_PACKAGES_DIR/geoips/tests/sectors/tc_bdecks/bwp312018.dat \
    --sector_adjuster_kwargs '{
    "recenter_tc_config": {
        "recenter_algs": ["archer","akima"],
        "archer_config": {
            "recenter_variables": ["tb89hA","tb89vA","tc36h","tb36v"],
            "include_archer_metadata_in_sector_info": True,
            "required_vmax_kts": 50,
            "output_products_dict": {
                "archer_image": {
                    "output_formatter": "archer_image",
                    "filename_formatter": "archer_image",
                },
                "archer_fix": {
                    "output_formatter": "archer_fix",
                    "filename_formatter": "archer_fix",
                    }
                }
            }
        }
    }'
ss_retval=$?

exit $((ss_retval))
