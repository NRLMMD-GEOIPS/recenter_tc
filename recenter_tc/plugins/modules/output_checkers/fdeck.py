# # # This source code is subject to the license referenced at
# # # https://github.com/NRLMMD-GEOIPS.

"""Test script for representative product comparisons."""

import logging

from geoips.plugins.modules.output_checkers.text import outputs_match
from geoips.geoips_utils import get_numpy_seeded_random_generator

LOG = logging.getLogger(__name__)

interface = "output_checkers"
family = "standard"
name = "fdeck"


def get_test_files(test_data_dir):
    """Return a series of varied fdeck files."""
    from shutil import copy
    from os import makedirs
    from os.path import exists, join

    savedir = join(test_data_dir, "scratch", "unit_tests", "test_fdecks")
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
    comp_file = join(savedir, "compare._FIX")
    with open(comp_file, mode="w") as comp_txt:
        comp_txt.writelines([fdeck_str])
    match_file = join(savedir, "matched._FIX")
    close_file = join(savedir, "close_mismatch._FIX")
    bad_file = join(savedir, "bad_mismatch._FIX")
    clear_text(match_file, close_file, bad_file)
    copy(comp_file, match_file)
    with open(comp_file, mode="r") as comp_txt:
        close_mismatch = open(close_file, "w")
        bad_mismatch = open(bad_file, "w")
        predictable_random = get_numpy_seeded_random_generator()
        for char in comp_txt.readline():
            for version in range(2):
                rand = predictable_random.random((0, 100))
                if version == 0:  # Close but mismatched
                    if rand > 5:
                        close_mismatch.write(char)
                else:  # Mismatched -- not close
                    if rand > 25:
                        bad_mismatch.write(char)
        close_mismatch.close()
        bad_mismatch.close()
    return comp_file, [match_file, close_file, bad_file]


def perform_test_comparisons(plugin, compare_file, test_files):
    """Test the comparison of two text files with the Text Output Checker."""
    for path_idx in range(len(test_files)):
        retval = outputs_match(
            plugin,
            test_files[path_idx],
            compare_file,
        )
        if path_idx == 0:
            assert retval is True
        else:
            assert retval is False


def clear_text(match_path, close_path, bad_path):
    """Clear output text files so they can be written again."""
    open(match_path, "w").close()
    open(close_path, "w").close()
    open(bad_path, "w").close()


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
