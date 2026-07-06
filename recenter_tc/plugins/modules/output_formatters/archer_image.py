# # # This source code is subject to the license referenced at
# # # https://github.com/NRLMMD-GEOIPS.

"""Plot ARCHER diagnostic 3 panel plot."""

import logging
from os.path import dirname

from geoips.filenames.base_paths import make_dirs
import archer.utilities.DisplayToolbox as ditbx

LOG = logging.getLogger(__name__)

interface = "output_formatters"
family = "xrdict_to_outlist"
name = "archer_image"


def call(xarray_dict, output_filename=None):
    """Call archer plot_diag_3panel routine."""
    LOG.info("Calling archer plot_diag_3panel")
    make_dirs(dirname(output_filename))
    ditbx.plot_diag_3panel(
        {x: y.data for x, y in xarray_dict["image"].items()},
        {x: y.data for x, y in xarray_dict["attrib"].items()},
        {x: y.data for x, y in xarray_dict["in_dict"].items()},
        {x: y.data for x, y in xarray_dict["out_dict"].items()},
        {x: y.data for x, y in xarray_dict["score_dict"].items()},
        display_filename=output_filename,
    )
    return [output_filename]
