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


clear_text = text.clear_text


def get_test_files():
    """Return a series of varied fdeck files."""
    import numpy as np
    from shutil import copy
    from os import environ, mkdir
    from os.path import exists

    savedir = str(environ["GEOIPS_OUTDIRS"]) + "/scratch/unit_tests/test_fdecks/"
    if not exists(savedir):
        mkdir(savedir)
    comp_path = savedir + "compare._FIX"
    match_path = savedir + "matched._FIX"
    close_path = savedir + "close_mismatch._FIX"
    bad_path = savedir + "bad_mismatch._FIX"
    clear_text(match_path, close_path, bad_path)
    copy(comp_path, match_path)
    with open(comp_path, mode="r") as comp_txt:
        close_mismatch = open(close_path, "w")
        bad_mismatch = open(bad_path, "w")
        for line in comp_txt.readlines():
            for version in range(2):
                rand = np.random.rand()
                if version == 0:  # Close but mismatched
                    if rand > 0.05:
                        close_mismatch.write(line)
                else:  # Mismatched -- not close
                    if rand > 0.25:
                        bad_mismatch.write(line)
        close_mismatch.close()
        bad_mismatch.close()
    return comp_path, [match_path, close_path, bad_path]


perform_test_comparisons = text.perform_test_comparisons


def correct_file_format(fname):
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
