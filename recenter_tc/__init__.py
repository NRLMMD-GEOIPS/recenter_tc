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

"""Recenter tropical cyclone imagery.

The recenter_tc package provides the capability for identifying the most accurate
storm center based on best track and storm forecast information, as well as the
data itself.

Two separate packages are used in determining the most accurate storm center:

akima86 fortran based interpolation
H. Akima 1986, Python adaptation D. Ryglicki 2020

This takes in all current best track information, forecasted storm locations,
as well as the actual time of the data file itself. The 6-hourly storm location
information is interpolated to the actual data time.

Automated Rotational Center Hurricane Eye Retrieval (ARCHER)
T. Wimmers
University of Wisconsin Cooperative Institute for Meteorological Satellite Studies

Using the akima86 interpolated center as a starting point, ARCHER identifies the
actual storm center from the data itself. ARCHER operates on passive microwave,
visible, and infrared data types

recenter_tc wrapper "area_def_adjuster"
akima86 and archer are called via the recenter_tc "area_def_adjuster" plugin.
Currently, the recenter_tc area_def_adjuster is accessed by specifying the
"--adjust_area_def recenter_tc" command line argument, and the procflows
handle calling akima86, calling archer, adjusting the area definition
appropriately, and generating related ARCHER f-deck and image outputs.

ARCHER output currently defaults to $GEOIPS_OUTDIRS/preprocessed/archer,
and filename formats and locations can be adjusted via adjustments to
filename_format plugins. Future updates to the recenter_tc plugin
package will provide easier access to adjusting the ARCHER output -
it is currently controlled via environment variables specifying which
filename format plugins to use for both image and fix outputs.

The default filename format plugins currently in use within recenter_tc are:

export ARCHER_IMAGE_FILENAME_FORMAT=archer_image
Located in recenter_tc/interface_modules/filename_formats/archer_image.py
export ARCHER_FIX_FILENAME_FORMAT=archer_fix
Located in recenter_tc/interface_modules/filename_formats/archer_fix.py
"""

from ._version import __version__, __version_tuple__
