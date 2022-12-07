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

''' Functionality for recentering TC sectors, based on akima and archer algorithms'''

from os.path import dirname

import logging

from geoips.interface_modules.procflows.single_source import print_area_def
from recenter_tc.filenames.base_paths import PATHS as GPATHS
from geoips.filenames.base_paths import make_dirs
from geoips.interfaces import filename_formatters

ARCHER_REQUIRED_VMAX_KTS = 50
ARCHER_IMAGE_FILENAME_FORMAT = GPATHS['ARCHER_IMAGE_FILENAME_FORMAT']
ARCHER_FIX_FILENAME_FORMAT = GPATHS['ARCHER_FIX_FILENAME_FORMAT']

LOG = logging.getLogger(__name__)

adjuster_type='list_xarray_list_variables_to_area_def_out_fnames'


def run_archer(xarray_obj, varname):
    ''' Run archer on the variable varname found in the xarray_obj'''
    KtoC_conversion = -273.15
    if varname in ['tb89h', 'tb89v', 'tb89hA', 'tb89hB', 'tb89vA', 'tb89vB', 'tb85h', 'tb85v', 'tb91h', 'tb91v',
                   'H89', 'V89', 'H91', 'V91', 'H85', 'V85',
                   'Chan1_AT', # AMSU-B 89V
                   ]:
        archer_channel_type = '89GHz'
    elif varname in ['Chan3_AT', # AMSU-B/MHS 183-1H
                     'Chan4_AT', # AMSU-B/MHS 183-3H
                     'Chan5_AT', # AMSU-B/MHS 190V
                     ]:
        archer_channel_type = '183GHz'
    elif varname in ['tb37h', 'tb37v', 'tb36h', 'tb36v', 'H37', 'V37', 'ftb37h', 'ftb37v']:
        archer_channel_type = '37GHz'
    elif 'BT' in varname:
        archer_channel_type = 'IR'
    elif 'Ref' in varname:
        archer_channel_type = 'Vis'
    else:
        LOG.warning('Unsupported sensor %s / channel %s type for ARCHER, returning without recentering',
                    xarray_obj.source_name, varname)
        return {}, {}, {}, []
    image = {}
    attrib = {}
    first_guess = {}
    attrib['archer_channel_type'] = archer_channel_type
    # This is currently unused in ARCHER, so just use GeoIPS platform names for attrib['sat']
    attrib['sat'] = xarray_obj.platform_name
    # out_fname = 'archer_test_{1}_{2}_{3}.png'.format(xarray_obj.platform_name, xarray_obj.source_name,
    #                                                  archer_channel_type)

    archer_image_fname = None
    archer_fix_fname = None

    filenamer = filename_formatters.get(ARCHER_IMAGE_FILENAME_FORMAT)
    if filenamer.family != 'xarray_metadata_to_filename':
        LOG.warning('Unsupported filename type %s %s, not producing ARCHER IMAGE output',
                    filenamer.family, ARCHER_IMAGE_FILENAME_FORMAT)
    else:
        archer_image_fname = filenamer(xarray_obj, variable_name=varname, archer_channel_type=archer_channel_type)

    filenamer = filename_formatters.get(ARCHER_FIX_FILENAME_FORMAT)
    if filenamer.family != 'xarray_metadata_to_filename':
        LOG.warning('Unsupported filename type %s %s, not producing ARCHER FIX output',
                    filenamer.family, ARCHER_FIX_FILENAME_FORMAT)
    else:
        archer_fix_fname = filenamer(xarray_obj, variable_name=varname, archer_channel_type=archer_channel_type)

    image['lat_grid'] = xarray_obj['latitude'].to_masked_array()
    image['lon_grid'] = xarray_obj['longitude'].to_masked_array()

    image['data_grid'] = xarray_obj[varname].to_masked_array()
    import numpy
    num_masked = numpy.ma.count_masked(image['data_grid'])
    if num_masked > 0:
        LOG.warning('There are %s masked values in array of size %s, not attempting to run ARCHER', num_masked,
                    image['data_grid'].size)
        return {}, {}, {}, []
    # image['time_arr'] = Does not exist

    if 'BT' in varname:
        if hasattr(xarray_obj[varname], 'units') and xarray_obj[varname].units == 'celsius':
            image['data_grid'] = xarray_obj[varname].to_masked_array() - KtoC_conversion

    if xarray_obj.platform_name == 'himawari-8':
        attrib['sensor'] = 'Imager'
        attrib['scan_type'] = 'Geo'
        attrib['nadir_lon'] = 140.7
    if xarray_obj.platform_name == 'msg-4':
        attrib['sensor'] = 'Imager'
        attrib['scan_type'] = 'Geo'
        attrib['nadir_lon'] = -0.3
    if xarray_obj.platform_name == 'msg-1':
        attrib['sensor'] = 'Imager'
        attrib['scan_type'] = 'Geo'
        attrib['nadir_lon'] = 41.5
    if xarray_obj.platform_name == 'goes-16':
        attrib['sensor'] = 'Imager'
        attrib['scan_type'] = 'Geo'
        attrib['nadir_lon'] = -75.2
    if xarray_obj.platform_name == 'goes-17':
        attrib['sensor'] = 'Imager'
        attrib['scan_type'] = 'Geo'
        attrib['nadir_lon'] = 137.2
    if xarray_obj.source_name == 'ssmis':
        attrib['sensor'] = 'SSMIS'
        attrib['scan_type'] = 'Conical'
    if xarray_obj.source_name == 'ssmi':
        attrib['sensor'] = 'SSMI'
        attrib['scan_type'] = 'Conical'
    if xarray_obj.source_name == 'tmi':
        attrib['sensor'] = 'TMI'
        attrib['scan_type'] = 'Conical'
    if xarray_obj.source_name in ['amsre', 'amsr-e']:
        attrib['sensor'] = 'AMSRE'
        attrib['scan_type'] = 'Conical'
    if xarray_obj.source_name == 'amsr2':
        attrib['sensor'] = 'AMSR2'
        attrib['scan_type'] = 'Conical'
    if xarray_obj.source_name == 'gmi':
        attrib['sensor'] = 'GMI'
        attrib['scan_type'] = 'Conical'
    if xarray_obj.source_name in ['amsub', 'amsu-b']:
        attrib['sensor'] = 'AMSU-B'
        attrib['scan_type'] = 'Crosstrack'
    if xarray_obj.source_name == 'mhs':
        attrib['sensor'] = 'MHS'
        attrib['scan_type'] = 'Crosstrack'
    if xarray_obj.source_name == 'atms':
        attrib['sensor'] = 'ATMS'
        attrib['scan_type'] = 'Crosstrack'

    if 'sensor' not in attrib:
        LOG.warning('Unsupported sensor %s / channel %s type for ARCHER, returning without recentering',
                    xarray_obj.source_name, varname)
        return {}, {}, {}, []

    import calendar
    # This is currently unused by ARCHER - but it should probably be best track, not fx if using deck files ?
    first_guess['source'] = 'fx'
    first_guess['time'] = calendar.timegm(xarray_obj.start_datetime.timetuple())
    first_guess['vmax'] = xarray_obj.area_definition.sector_info['vmax']
    first_guess['lat'] = xarray_obj.area_definition.sector_info['clat']
    first_guess['lon'] = xarray_obj.area_definition.sector_info['clon']

    out_fnames = []
    if archer_image_fname is not None:
        make_dirs(dirname(archer_image_fname))
        out_fnames += [archer_image_fname]
        LOG.info('ARCHERSUCCESS Writing ARCHER image: %s', archer_image_fname)
    from archer.archer4 import archer4
    in_dict, out_dict, score_dict = \
        archer4(image, attrib, first_guess, para_fix=True, display_filename=archer_image_fname,
                sector_info=xarray_obj.area_definition.sector_info)

    if archer_fix_fname is not None:
        make_dirs(dirname(archer_fix_fname))
        out_fnames += [archer_fix_fname]
        with open(archer_fix_fname, 'w') as fobj:
            fobj.write(out_dict['fdeck_string'])
        LOG.info('ARCHERSUCCESS Wrote ARCHER fdeck: %s', archer_fix_fname)
    return in_dict, out_dict, score_dict, out_fnames


def recenter_tc(xobjs, area_def, variables, recenter_variables=None):
    LOG.info(f'\n\n************************************************************************************'\
             f'\n************************************************************************************'\
             f'\n************************************************************************************'\
             f'\n************************************************************************************'\
             f'\n***Attempting to recenter TC sector...\n')
    ret_area_def = area_def.copy()

    # If recenter_variables is not defined, produce ARCHER output from all variables,
    # and use the first variable alphabetically by default as the primary.
    if recenter_variables is None:
        recenter_variables = sorted(variables)
        recenter_variables += ['akima']

    recentered_area_defs = {}
    curr_recenter_variables = []
    out_fnames = []

    for xobj in xobjs:
        include_vars = list(set(variables).intersection(set(xobj.variables.keys())))
        curr_recenter_variables = list(set(recenter_variables).intersection(set(xobj.variables.keys())))
        if include_vars and curr_recenter_variables:
            curr_recentered_area_defs, curr_out_fnames = recenter_tc_area_def(area_def,
                                                                              xobj,
                                                                              variables=curr_recenter_variables)
            out_fnames += curr_out_fnames
            for varname in curr_recentered_area_defs:
                recentered_area_defs[varname] = curr_recentered_area_defs[varname]

    # If nothing worked, try akima
    if not recentered_area_defs:
        recentered_area_defs['akima'] = recenter_with_akima(xobjs[0], area_def)

    # If no ARCHER recenter, try akima recenter
    if 'akima' in recentered_area_defs:
        ret_area_def = recentered_area_defs['akima']

    # Select the first valid recenter variable, and return.
    for recenter_varname in recenter_variables:
        if recenter_varname in recentered_area_defs:
            LOG.info('USING recenter variable name %s', recenter_varname)
            print_area_def(recentered_area_defs[recenter_varname],
                           f'USING recenter variable name {recenter_varname} area def')
            ret_area_def = recentered_area_defs[recenter_varname]
            break

    LOG.info(f'\n\nout_fnames'
             f'\n{out_fnames}')

    LOG.info(f'\n\n********Done recentering TC sector'
             f'\n************************************************************************************'
             f'\n************************************************************************************'
             f'\n************************************************************************************'
             f'\n************************************************************************************')

    # If nothing recentered, return the original area_def
    return ret_area_def, out_fnames


def recenter_area_def(area_def, fields):
    from geoips.sector_utils.tc_tracks import get_tc_long_description
    from geoips.interface_modules.area_def_generators.clat_clon_resolution_shape import clat_clon_resolution_shape
    new_area_def = clat_clon_resolution_shape(area_id=area_def.area_id,
                                              long_description=get_tc_long_description(area_def.area_id,
                                                                                       fields),
                                              clat=fields['clat'],
                                              clon=fields['clon'],
                                              projection=area_def.proj_dict['proj'],
                                              num_lines=area_def.y_size,
                                              num_samples=area_def.x_size,
                                              pixel_width=area_def.pixel_size_x,
                                              pixel_height=area_def.pixel_size_y)
    from geoips.sector_utils.utils import copy_sector_info
    new_area_def = copy_sector_info(area_def, new_area_def)
    new_area_def.sector_info = fields.copy()
    return new_area_def


def recenter_with_archer(sect_xarray, variables, area_def_to_recenter):
    recentered_area_defs = {}
    out_fnames = []
    if area_def_to_recenter.sector_info['vmax'] < ARCHER_REQUIRED_VMAX_KTS:
        LOG.info('***SKIPPING not attempting to run archer, vmax of %s less than required %s kts',
                 area_def_to_recenter.sector_info['vmax'], ARCHER_REQUIRED_VMAX_KTS)
        return recentered_area_defs, out_fnames
    # I believe ARCHER can not have any masked data within the data grid, so create a separate smaller sector for
    # running archer.  The size of the "new" ARCHER sector could probably use some tweaking, though this worked
    # "out of the box" for my test case.
    # Probably in the end want to just run ARCHER first, get the new center, then create a new area_def with
    # the ARCHER center. and sector / register based on the ARCHER centered area_def. Ok, I'll just do that
    # really quickly.
    LOG.info(f'\n\n************************************************************************************'\
             f'\n************************************************************************************'\
             f'\n********Attempting to run ARCHER...\n')

    from geoips.xarray_utils.data import sector_xarray_spatial
    clat = area_def_to_recenter.sector_info['clat']
    clon = area_def_to_recenter.sector_info['clon']
    minlat = clat - 2 # 2
    maxlat = clat + 2 # 2
    minlon = clon - 2 # 2
    maxlon = clon + 2 # 2
    lat_pad = 0
    lon_pad = 0
    # Need full swath width for AMSU-B and MHS for ARCHER. Need a better solution for this.
    if sect_xarray.source_name in ['amsu-b', 'mhs']:
        lat_pad = 15
        lon_pad = 15
    archer_xarray = sector_xarray_spatial(sect_xarray,
                                          [minlon, minlat, maxlon, maxlat],
                                          variables+['latitude', 'longitude'],
                                          lon_pad=lon_pad, lat_pad=lat_pad, drop=True)
    archer_xarray.attrs['area_definition'] = area_def_to_recenter

    new_fields = area_def_to_recenter.sector_info.copy()

    for varname in sorted(variables):
        LOG.info(f'\n\n************************************************************************************'\
                 f'\n********Running ARCHER on {varname}...\n')

        in_dict, out_dict, score_dict, curr_out_fnames = run_archer(archer_xarray, varname)
        out_fnames += curr_out_fnames
        # YAML output fails on numpy.float64, so cast as float
        if out_dict and out_dict['center_lat']:
            new_fields['clat'] = round(float(out_dict['center_lat']), 2)
            new_fields['clon'] = round(float(out_dict['center_lon']), 2)
            new_fields['archer_fdeck'] = out_dict['fdeck_string']
            new_fields['recenter_type'] = varname
            # short ID used to identify which adjustment was used - to be used in filenames, etc
            new_fields['adjustment_id'] = 'ar'+varname
            recentered_area_defs[varname] = recenter_area_def(area_def_to_recenter, new_fields)
            # print_area_def(area_def_to_recenter, 'Final ARCHER recentered area def')
            LOG.info(f'\n\n********ARCHER run successful'\
                     f'\n************************************************************************************\n')
        else:
            LOG.info(f'\n\n********ARCHER run unsuccessful'\
                     f'\n************************************************************************************\n')
    LOG.info(f'\n\n********Done running ARCHER'\
             f'\n************************************************************************************'\
             f'\n************************************************************************************')
    return recentered_area_defs, out_fnames


def recenter_with_akima(sect_xarray, area_def):
    LOG.info(f'\n\n************************************************************************************'\
             f'\n************************************************************************************'\
             f'\n********Running AKIMA center interpolation...\n')
    from geoips.sector_utils.tc_tracks import trackfile_to_area_defs
    from geoips.sector_utils.utils import remove_duplicate_storm_positions
    from os.path import expandvars
    # Grab the center time of the actual TC sector, not the start_datetime or end_datetime
    center_time = sect_xarray.start_datetime + (sect_xarray.end_datetime - sect_xarray.start_datetime) / 2
    LOG.info('***  Using center time %s for akima', center_time)
    if 'parser_name' in area_def.sector_info and area_def.sector_info['parser_name']:
        trackfile_name = expandvars(area_def.sector_info['source_filename'])
        trackfile_parser = area_def.sector_info['parser_name']

        LOG.info(f'***  Obtaining all area_defs from {trackfile_name}...')
        area_defs = trackfile_to_area_defs(trackfile_name, trackfile_parser)
    else:
        return area_def
    clats = []
    clons = []
    pressures = []
    vmaxes = []
    times = []
    aid_types = []
    idx = 0
    area_defs = remove_duplicate_storm_positions(area_defs)
    for curr_area_def in area_defs:
        # Only include one forecast
        if aid_types and aid_types[-1] != 'BEST' and curr_area_def.sector_info['aid_type'] != 'BEST':
            continue
        sector_info = curr_area_def.sector_info.copy()
        check_sector_info = ['clat', 'clon', 'pressure', 'vmax']
        # Replace empty sector info keys with bad value flag -9999
        for skey, val in sector_info.items():
            if isinstance(val, str) and skey in check_sector_info:
                LOG.info(f"Missing {skey} sector information for {sector_info['synoptic_time']}")
                sector_info[skey] = -9999
        clats += [sector_info['clat']]
        clons += [sector_info['clon']]
        pressures += [sector_info['pressure']]
        vmaxes += [sector_info['vmax']]
        times += [sector_info['synoptic_time'].timestamp()]
        aid_types += [sector_info['aid_type']]
        if curr_area_def.sector_info['synoptic_time'] == area_def.sector_info['synoptic_time']:
            closest_idx = idx
        idx += 1

    LOG.info(f'***Interpolating new center from {len(clats)} best track positions, closest position {closest_idx}...')
    from akima86.akima86 import interpolate
    import numpy
    times_arr = numpy.array(times)
    ctime_arr = numpy.array([center_time.timestamp()])
    clats_arr = numpy.array(clats)
    recenter_clat = interpolate(times_arr[clats_arr != -9999],
                                clats_arr[clats_arr != -9999],
                                ctime_arr)[0].astype(float)
    clons_arr = numpy.array(clons)
    recenter_clon = interpolate(times_arr[clons_arr != -9999],
                                clons_arr[clons_arr != -9999],
                                ctime_arr)[0].astype(float)
    vmax_arr = numpy.array(vmaxes[:-1])
    recenter_vmax = interpolate(times_arr[:-1][vmax_arr != -9999],
                                vmax_arr[vmax_arr != -9999],
                                ctime_arr)[0].astype(float)
    pres_arr = numpy.array(pressures[:-1])
    recenter_pressure = interpolate(times_arr[:-1][pres_arr != -9999],
                                    pres_arr[pres_arr != -9999],
                                    ctime_arr)[0].astype(float)
    new_fields = area_def.sector_info.copy()
    # YAML output fails on numpy.float64, so cast as float
    new_fields['clat'] = round(float(recenter_clat), 2)
    new_fields['clon'] = round(float(recenter_clon), 2)
    new_fields['vmax'] = round(float(recenter_vmax), 2)
    new_fields['pressure'] = round(float(recenter_pressure), 2)
    new_fields['interpolated_time'] = center_time
    new_fields['recenter_type'] = 'akima'
    # short ID used to identify which adjustment was used - to be used in filenames, etc
    new_fields['adjustment_id'] = 'akima'

    recentered_area_def = recenter_area_def(area_def, new_fields)

    # print_area_def(recentered_area_def, 'New akima center')
    # print_area_def(area_def, 'Original center')
    LOG.info(f'\n\n********Akima interpolation successful'\
             f'\n************************************************************************************'\
             f'\n************************************************************************************')
    return recentered_area_def


def recenter_tc_area_def(area_def, sect_xarray, variables):
    from geoips.sector_utils.utils import is_sector_type
    # Only recenter if this is a TC sector
    recentered_area_defs = {}
    out_fnames = []
    if is_sector_type(area_def, 'tc'):

        recentered_area_defs['akima'] = recenter_with_akima(sect_xarray, area_def)

        archer_recentered_area_defs, out_fnames = recenter_with_archer(sect_xarray,
                                                                       variables,
                                                                       recentered_area_defs['akima'])

        print_area_def(area_def, 'Original area def')
        for varname in archer_recentered_area_defs:
            recentered_area_defs[varname] = archer_recentered_area_defs[varname]
        for varname in recentered_area_defs:
            print_area_def(recentered_area_defs[varname], f'{varname} area def')

    else:
        recentered_area_defs['orig'] = area_def

    return recentered_area_defs, out_fnames
