# # # This source code is subject to the license referenced at
# # # https://github.com/NRLMMD-GEOIPS.

"""Specifications for output filename formats for tc product types."""

import logging

from os.path import join as pathjoin
from recenter_tc.filenames.base_paths import PATHS as gpaths

interface = "filename_formatters"
family = "xarray_metadata_to_filename"
name = "archer_fix"

LOG = logging.getLogger(__name__)


def get_basin_letter(tc_basin, tc_clon, tc_clat):
    """Return basin designation.

    Parameters
    ----------
    tc_basin: string
        basin letters
    tc_clon: float
        longitude
    tc_clat: float
        latitude

    Returns
    -------
    str: basin letter designation
    """
    # atcf/form_sectorfile.py has Q listed as both SL and LS, include both here.
    # Only IO and SH can have possibly multiple basin designators,
    # dependent on longitude.
    # Note we want to determine the basin designator at the start of the storm,
    # and do not change if the storm happens to cross over the longitude line.
    # Thus, check for existing directory first, and if it doesn't exist,
    # create based on current center lat/lon of storm.
    # Potentially causes a problem if we run a storm for the first time in
    # the middle of the storm, but I'm going to take that risk at this point.
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


def call(
    xarray_obj,
    extension=None,
    basedir=gpaths["ARCHER_FIX_PATH"],
    variable_name=None,
    archer_channel_type=None,
    use_storm_subdirs=False,
):
    """Given an xarray, creates the archer filename."""
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
        source_name=xarray_obj.source_name,
        platform_name=xarray_obj.platform_name,
        product_datetime=xarray_obj.start_datetime,
        data_provider=xarray_obj.data_provider,
        basin_letter=basin_letter,
        extension=extension,
        use_storm_subdirs=use_storm_subdirs,
        sector_info=area_def.sector_info,
    )


def assemble_archer_fname(
    basedir,
    variable_name,
    archer_channel_type,
    source_name,
    platform_name,
    product_datetime,
    data_provider,
    basin_letter,
    sector_info,
    extension=".txt",
    use_storm_subdirs=False,
):
    """Produce full output product path from product/sensor specifications.

    Parameters
    ----------
    basedir: string
        base directory
    sector_info: dict
        Dictionary of TC sector info, including storm_year, storm_basin, storm_id, etc.
    variable_name: string
        Name of variable (e.g., 'B09BT')
    archer_channel_type: string
        Type of archer channel (e.g., 'Vis', 'IR', etc)
    source_name: string
        Name of data source (e.g., 'amsr2', 'smap', etc)
    data_provider: string
        Name of data provider (e.g., 'remss', 'ospo', etc)
    basin_letter: string
        Single letter basin designation (e.g., 'W', 'E', 'S', etc)
    platform_name: string
        Name of platform (satellite)
    product_datetime: datetime
        Start time of data used to generate product

    Returns
    -------
    str: to full path of output filename of the format:
        <basedir>/tc<tc_year>/<tc_basin>/<tc_basin><tc_stormnum><tc_year>/txt/
        <source_name>_<platform_name>_surface_winds_<data_provider>_<YYYYMMDDHHMN>

    Usage
    -----
        >>> startdt = datetime.strptime('20200216T001412', '%Y%m%dT%H%M%S')
        >>> assemble_windspeeds_text_tc_fname('/outdir', 2020, 'SH', 16,\
            'smap-spd', 'smap', startdt, 'remss')
        >>> '/outdir/tc2020/SH/SH162020/txt/\
             archer_smap_surface_winds_remss_20200216001412.txt
    """
    from geoips.plugins.modules.filename_formatters.utils.tc_file_naming import (
        tc_storm_basedir,
    )

    if use_storm_subdirs:
        path = pathjoin(tc_storm_basedir(basedir, sector_info), "txt", "archer")
    else:
        path = basedir
    # MUST end in _02W_FIX (for example)
    fname = "_".join(
        [
            product_datetime.strftime("%Y%m%d.%H%M"),
            sector_info["storm_id"].upper(),
            "archer",
            source_name,
            variable_name,
            archer_channel_type,
            data_provider,
            platform_name,
            "{0:02d}{1}".format(sector_info["storm_num"], basin_letter),
            "FIX",
        ]
    )
    if extension is not None:
        fname = f"{fname}{extension}"
    return pathjoin(path, fname)
