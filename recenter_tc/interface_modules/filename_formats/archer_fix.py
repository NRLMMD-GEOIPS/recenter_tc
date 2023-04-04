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

""" Specifications for output filename formats for tc product types. """

import logging

from os.path import join as pathjoin, splitext as pathsplitext
from os.path import dirname as pathdirname, basename as pathbasename
from datetime import datetime, timedelta
from glob import glob
from os import unlink as osunlink

from recenter_tc.filenames.base_paths import PATHS as gpaths
from geoips.data_manipulations.merge import minrange

filename_type = "xarray_metadata_to_filename"

LOG = logging.getLogger(__name__)


def get_basin_letter(tc_basin, tc_clon, tc_clat):
    # atcf/form_sectorfile.py has Q listed as both SL and LS, include both here.
    # Only IO and SH can have possibly multiple basin designators, dependent on longitude.
    # Note we want to determine the basin designator at the start of the storm, and do not change if the storm
    # happens to cross over the longitude line.  Thus, check for existing directory first, and if it doesn't exist,
    # create based on current center lat/lon of storm.  Note this could potentially cause a problem if we run a
    # storm for the first time in the middle of the storm, but I'm going to take that risk at this point.
    basin_letters = {
        "AL": ["L"],
        "SL": ["Q"],
        "LS": ["Q"],
        "IO": ["A", "B"],
        "SH": ["S", "P"],
        "CP": ["C"],
        "EP": ["E"],
        "WP": ["W"],
    }

    if tc_basin in ["AL", "CP", "EP", "WP", "SL", "LS"]:
        basin_letter = basin_letters[tc_basin][0]
    elif tc_basin == "IO":
        if tc_clon >= 77.5 and tc_clon < 100.0:
            basin_letter = "B"
        elif tc_clon >= 40.0 and tc_clon < 77.5:
            basin_letter = "A"
    elif tc_basin == "SH":
        if tc_clon >= 20.0 and tc_clon < 135.0:
            basin_letter = "S"
        else:
            basin_letter = "P"

    return basin_letter


def archer_fix(
    xarray_obj,
    extension=None,
    basedir=gpaths["ARCHER_FIX_PATH"],
    variable_name=None,
    archer_channel_type=None,
    use_storm_subdirs=False,
):
    area_def = xarray_obj.area_definition
    basin_letter = get_basin_letter(
        area_def.sector_info["storm_basin"],
        area_def.sector_info["clon"],
        area_def.sector_info["clat"],
    )
    return assemble_archer_fname(
        basedir=basedir,
        variable_name=variable_name,
        archer_channel_type=archer_channel_type,
        tc_area_id=area_def.area_id,
        tc_year=int(area_def.sector_info["storm_year"]),
        tc_basin=area_def.sector_info["storm_basin"],
        tc_stormnum=int(area_def.sector_info["storm_num"]),
        source_name=xarray_obj.source_name,
        platform_name=xarray_obj.platform_name,
        product_datetime=xarray_obj.start_datetime,
        data_provider=xarray_obj.data_provider,
        basin_letter=basin_letter,
        extension=extension,
        use_storm_subdirs=use_storm_subdirs,
    )


def assemble_archer_fname(
    basedir,
    variable_name,
    archer_channel_type,
    tc_area_id,
    tc_year,
    tc_basin,
    tc_stormnum,
    source_name,
    platform_name,
    product_datetime,
    data_provider,
    basin_letter,
    extension=".txt",
    use_storm_subdirs=False,
):
    """Produce full output product path from product / sensor specifications.

    Args:
        basedir (str) :  base directory
        tc_year (int) :  Full 4 digit storm year
        tc_basin (str) :  2 character basin designation
                               SH Southern Hemisphere
                               WP West Pacific
                               EP East Pacific
                               CP Central Pacific
                               IO Indian Ocean
                               AL Atlantic
        tc_stormnum (int) : 2 digit storm number
                               90 through 99 for invests
                               01 through 69 for named storms
        platform_name (str) : Name of platform (satellite)
        product_datetime (datetime) : Start time of data used to generate product

    Returns:
        str: to full path of output filename of the format:
          <basedir>/tc<tc_year>/<tc_basin>/<tc_basin><tc_stormnum><tc_year>/txt/
          <source_name>_<platform_name>_surface_winds_<data_provider>_<YYYYMMDDHHMN>

    Usage:
        >>> startdt = datetime.strptime('20200216T001412', '%Y%m%dT%H%M%S')
        >>> assemble_windspeeds_text_tc_fname('/outdir', 2020, 'SH', 16, 'smap-spd', 'smap', startdt, 'remss')
        '/outdir/tc2020/SH/SH162020/txt/archer
    """

    from geoips.interface_modules.filename_formats.utils.tc_file_naming import (
        tc_storm_basedir,
    )

    if use_storm_subdirs:
        path = pathjoin(
            tc_storm_basedir(basedir, tc_year, tc_basin, tc_stormnum), "txt", "archer"
        )
    else:
        path = basedir
    # MUST end in _02W_FIX (for example)
    fname = "_".join(
        [
            product_datetime.strftime("%Y%m%d.%H%M"),
            tc_area_id,
            "archer",
            source_name,
            variable_name,
            archer_channel_type,
            data_provider,
            platform_name,
            "{0:02d}{1}".format(tc_stormnum, basin_letter),
            "FIX",
        ]
    )
    if extension is not None:
        fname = f"{fname}{extension}"
    return pathjoin(path, fname)
