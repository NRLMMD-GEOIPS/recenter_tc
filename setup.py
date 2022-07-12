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

'''Installation instructions for recenter_tc package'''

from os.path import realpath, join, dirname

import setuptools

with open(join(dirname(realpath(__file__)), 'VERSION'), encoding='utf-8') as version_file:
    version = version_file.read().strip()

setuptools.setup(
    name='recenter_tc',
    version=version,
    packages=setuptools.find_packages(),
    entry_points={
        'geoips.area_def_adjusters': [
            'recenter_tc=recenter_tc.interface_modules.area_def_adjusters.recenter_tc:recenter_tc',
        ],
        'geoips.filename_formats': [
            'archer_fix=recenter_tc.interface_modules.filename_formats.archer_fix:archer_fix',
            'archer_image=recenter_tc.interface_modules.filename_formats.archer_image:archer_image',
        ],
    }
)
