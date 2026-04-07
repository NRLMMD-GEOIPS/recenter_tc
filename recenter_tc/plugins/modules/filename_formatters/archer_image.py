# # # This source code is subject to the license referenced at
# # # https://github.com/NRLMMD-GEOIPS.

"""Specifications for output filename formats for tc product types."""

import logging

from os.path import join as pathjoin
from recenter_tc.filenames.base_paths import PATHS as gpaths

interface = "filename_formatters"
family = "xarray_metadata_to_filename"
name = "archer_image"

LOG = logging.getLogger(__name__)


def call(
    xarray_obj,
    extension=".png",
    basedir=gpaths["ARCHER_IMAGE_PATH"],
    variable_name=None,
    archer_channel_type=None,
):
    """Assembles the archer filename."""
    area_def = xarray_obj.area_definition
    return assemble_archer_fname(
        basedir=basedir,
        variable_name=variable_name,
        archer_channel_type=archer_channel_type,
        source_name=xarray_obj.source_name,
        platform_name=xarray_obj.platform_name,
        product_datetime=xarray_obj.start_datetime,
        data_provider=xarray_obj.data_provider,
        sector_info=area_def.sector_info,
        extension=extension,
    )


def assemble_archer_fname(
    basedir,
    variable_name,
    archer_channel_type,
    source_name,
    platform_name,
    product_datetime,
    data_provider,
    sector_info,
    extension=".png",
):
    """Produce full output product path from product / sensor specifications.

    Parameters
    ----------
    basedir: string
        base directory
    platform_name: string
        Name of platform (satellite)
    product_datetime: datetime
        Start time of data used to generate product
    sector_info: dict
        Dictionary of TC sector info, including storm_year, storm_basin, storm_id, etc.
    data_provider: string
        Name of data provider (e.g., 'remss', 'ospo', etc)
    source_name: string
        Name of data source (e.g., 'amsr2', 'smap', etc)
    variable_name: string
        Name of variable (e.g., 'B09BT')
    archer_channel_type: string
        Type of archer channel (e.g., 'pmw', 'ir', 'vis')
    extension: string
        File extension (including leading period), default '.png'

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
            archer_smap_surface_winds_remss_20200216001412.png'
    """
    from geoips.plugins.modules.filename_formatters.utils.tc_file_naming import (
        tc_storm_basedir,
    )

    # Use the standard tc storm basedir, as defined in geoips repo.
    path = pathjoin(tc_storm_basedir(basedir, sector_info), "png", "archer")
    # Upper case for storm_id in filenames, lower case internally.
    # Note since we are using storm_id explicitly, this will include
    # storm start datetime for invests and will NOT include storm
    # start datetime for numbered storms.
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
        ]
    )
    if extension is not None:
        fname = f"{fname}{extension}"
    return pathjoin(path, fname)
