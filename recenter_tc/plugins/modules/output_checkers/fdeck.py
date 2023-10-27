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


def get_test_files(output_path):
    """Return a series of varied fdeck files."""
    import numpy as np
    from shutil import copy
    from os import makedirs
    from os.path import exists, join

    savedir = join(output_path, "scratch/unit_tests/test_fdecks/")
    if not exists(savedir):
        makedirs(savedir)
    # Sample fdeck - this is the output from the abi Visible test
    fdeck_str = (
        "AL, 20, 2009181950,  70, VISI,          C,  ,"
        " 2289N,  5670W,      ,"
        " 3,    ,  ,     ,  ,     ,    ,     ,     ,     ,     ,"
        "     ,  ,  ,  ,  ,  ,    ,    ,  ,  CIMS,"
        " AUT,    ,             ,             ,    ,"
        "     ,                        v, "
        "irad=0.15 | r50=0.48 | r95=1.36 | ep=-99 | src=ARCH"
    )
    comp_path = join(savedir, "compare._FIX")
    with open(comp_path, mode="w") as comp_txt:
        comp_txt.writelines([fdeck_str])
    match_path = join(savedir, "matched._FIX")
    close_path = join(savedir, "close_mismatch._FIX")
    bad_path = join(savedir, "bad_mismatch._FIX")
    clear_text(match_path, close_path, bad_path)
    copy(comp_path, match_path)
    with open(comp_path, mode="r") as comp_txt:
        close_mismatch = open(close_path, "w")
        bad_mismatch = open(bad_path, "w")
        for char in comp_txt.readline():
            for version in range(2):
                rand = np.random.rand()
                if version == 0:  # Close but mismatched
                    if rand > 0.05:
                        close_mismatch.write(char)
                else:  # Mismatched -- not close
                    if rand > 0.25:
                        bad_mismatch.write(char)
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
