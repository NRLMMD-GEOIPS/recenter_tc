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

"""Test script for representative product comparisons."""

import logging
from geoips.plugins.modules.output_checkers import text

LOG = logging.getLogger(__name__)

interface = "output_checkers"
family = "standard"
name = "fdeck"


def correct_type(fname):
    """Check if fname is an fdeck file.

    Parameters
    ----------
    fname (str) : Name of file to check.

    Returns
    -------
    bool: True if it is an fdeck file r(\*_FIX), False otherwise. # NOQA
    """
    if fname.split("_")[-1] in ["FIX"]:
        with open(fname) as f:
            line = f.readline()
        if isinstance(line, str):
            return True
    return False


outputs_match = text.outputs_match

call = text.call
