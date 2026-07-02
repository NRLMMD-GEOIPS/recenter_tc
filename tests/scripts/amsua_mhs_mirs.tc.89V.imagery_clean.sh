# # # This source code is subject to the license referenced at
# # # https://github.com/NRLMMD-GEOIPS.

#!/bin/bash
geoips run single_source \
    $GEOIPS_TESTDATA_DIR/test_data_amsub/data/NPR-MIRS-IMG_v11r4_ma2_s202104192335000_e202104190118000_c202104200206490.nc \
    --procflow single_source \
    --reader_name amsua_mhs_mirs \
    --product_name 89V \
    --compare_path "$GEOIPS_PACKAGES_DIR/recenter_tc/tests/outputs/amsua_mhs_mirs.tc.89V.imagery_clean" \
    --output_formatter imagery_clean \
    --filename_formatter tc_clean_fname \
    --sector_adjuster recenter_tc \
    --metadata_filename_formatter metadata_default_fname \
    --metadata_output_formatter metadata_default \
    --trackfile_parser bdeck_parser \
    --trackfiles $GEOIPS_PACKAGES_DIR/geoips/tests/sectors/tc_bdecks/bwp022021.dat \
    --sector_adjuster_kwargs '{
        "archer_config": {
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
    }'
ss_retval=$?

exit $((ss_retval))
