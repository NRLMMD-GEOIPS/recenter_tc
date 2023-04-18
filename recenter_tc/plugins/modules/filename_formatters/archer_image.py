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

''' Specifications for output filename formats for tc product types. '''

import logging

from os.path import join as pathjoin, splitext as pathsplitext
from os.path import dirname as pathdirname, basename as pathbasename
from datetime import datetime, timedelta
from glob import glob
from os import unlink as osunlink

from recenter_tc.filenames.base_paths import PATHS as gpaths
from geoips.data_manipulations.merge import minrange

filename_type = 'xarray_metadata_to_filename'

LOG = logging.getLogger(__name__)


def archer_image(xarray_obj,
                 extension='.png', basedir=gpaths['ARCHER_IMAGE_PATH'],
                 variable_name=None, archer_channel_type=None):
    area_def = xarray_obj.area_definition
    return assemble_archer_fname(basedir=basedir,
                                 variable_name=variable_name,
                                 archer_channel_type=archer_channel_type,
                                 tc_area_id=area_def.area_id,
                                 tc_year=int(area_def.sector_info['storm_year']),
                                 tc_basin=area_def.sector_info['storm_basin'],
                                 tc_stormnum=int(area_def.sector_info['storm_num']),
                                 source_name=xarray_obj.source_name,
                                 platform_name=xarray_obj.platform_name,
                                 product_datetime=xarray_obj.start_datetime,
                                 data_provider=xarray_obj.data_provider,
                                 extension=extension)


def assemble_archer_fname(basedir, variable_name, archer_channel_type,
                          tc_area_id, tc_year, tc_basin, tc_stormnum, source_name,
                          platform_name, product_datetime, data_provider, extension='.png'):
    ''' Produce full output product path from product / sensor specifications.

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
    '''

    from geoips.plugins.modules.filename_formatters.utils.tc_file_naming import tc_storm_basedir
    path = pathjoin(tc_storm_basedir(basedir, tc_year, tc_basin, tc_stormnum),
                    'png', 'archer')
    fname = '_'.join([product_datetime.strftime('%Y%m%d.%H%M'),
                      tc_area_id,
                      'archer',
                      source_name,
                      variable_name,
                      archer_channel_type,
                      data_provider,
                      platform_name])
    if extension is not None:
        fname = f'{fname}{extension}'
    return pathjoin(path, fname)
