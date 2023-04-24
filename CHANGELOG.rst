 | # # # Distribution Statement A. Approved for public release. Distribution unlimited.
 | # # #
 | # # # Author:
 | # # # Naval Research Laboratory, Marine Meteorology Division
 | # # #
 | # # # This program is free software: you can redistribute it and/or modify it under
 | # # # the terms of the NRLMMD License included with this program. This program is
 | # # # distributed WITHOUT ANY WARRANTY; without even the implied warranty of
 | # # # MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the included license
 | # # # for more details. If you did not receive the license, for more information see:
 | # # # https://github.com/U-S-NRL-Marine-Meteorology-Division/

Please see geoips/CHANGELOG_TEMPLATE.rst for instructions on updating
CHANGELOG appropriately with each PR

Release notes for previous versions can be found in docs/source/releases, for reference

Breaking Changes
================

Update interface naming and move to plugins directory
-------------------------------------------------

*From issue GEOIPS/recenter_tc#10: 2023-04-18*

* Moved interface_modules to plugins/modules

  * Updated related imports
  * Updated entry points
* Renamed filename_format to filename_formatter
* Renamed output_format to output_formatter

::

    moved: recenter_tc/interface_modules to recenter_tc/plugins/modules
    modified: tests/scripts/*
    renamed: recenter_tc/plugins/modules/filename_formats -> recenter_tc/plugins/modules/filename_formatters
    renamed: recenter_tc/plugins/modules/area_def_adjusters -> recenter_tc/plugins/modules/sector_adjusters