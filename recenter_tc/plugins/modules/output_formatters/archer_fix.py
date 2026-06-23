# # # This source code is subject to the license referenced at
# # # https://github.com/NRLMMD-GEOIPS.

"""Write ARCHER fix file."""

import logging
from os.path import dirname

from geoips.filenames.base_paths import make_dirs

LOG = logging.getLogger(__name__)

interface = "output_formatters"
family = "xrdict_to_outlist"
name = "archer_fix"


def call(xarray_dict, output_filename=None):
    """Write ARCHER fix to file."""
    make_dirs(dirname(output_filename))
    fdeck_string = xarray_dict["out_dict"]["fdeck_string"].item()
    with open(output_filename, "w") as fobj:
        fobj.write(fdeck_string)
    return [output_filename]
