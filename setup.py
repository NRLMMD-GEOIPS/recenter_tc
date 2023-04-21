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

"""Installation instructions for recenter_tc package"""

import setuptools

package_name = "recenter_tc"

setuptools.setup(
    name=package_name,
    use_scm_version={
        "write_to": f"{package_name}/version.py",  # Writes hard coded version to file
        "version_scheme": "post-release",  # Use current version .postN vs incrementing
        "local_scheme": "no-local-version",
    },  # Does not include extra hash info
    setup_requires=["setuptools_scm"],
    packages=setuptools.find_packages(),
    install_requires=[
        "archer @ git+https://github.com/ajwimmers/archer.git",
        "akima86 @ git+https://github.com/NRLMMD-GEOIPS/akima86.git",
    ],
    entry_points={
        "geoips.sector_adjusters": [
            "recenter_tc=recenter_tc.plugins.modules.sector_adjusters.recenter_tc:recenter_tc",
        ],
        "geoips.filename_formatters": [
            "archer_fix=recenter_tc.plugins.modules.filename_formatters.archer_fix:archer_fix",
            "archer_image=recenter_tc.plugins.modules.filename_formatters.archer_image:archer_image",
        ],
        "geoips.output_comparisons": [
            "compare_outputs_recenter_tc=recenter_tc.compare_outputs_recenter_tc:compare_outputs_recenter_tc",
        ],
    },
)
