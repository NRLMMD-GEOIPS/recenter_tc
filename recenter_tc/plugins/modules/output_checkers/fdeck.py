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


def outputs_match(output_product, compare_product):
    """Check if two fdeck files match.

    Parameters
    ----------
    plugin: OutputCheckerPlugin
        The corresponding geotiff OutputCheckerPlugin that has access to needed methods
    output_product : str
        Full path to current output product
    compare_product : str
        Full path to "good" comparison product

    Returns
    -------
    bool
        Return True if products match, False if they differ
    """
    LOG.info("Comparing FDECK products.")
    from geoips.plugins.modules.output_checkers.text import outputs_match

    return outputs_match(output_product, compare_product)


def call(plugin, compare_path, output_products):
    """Compare the "correct" imagery found in comparepath with list of output_products.

    Parameters
    ----------
    plugin: OutputCheckerPlugin
        - The corresponding fdeck OutputCheckerPlugin that has access to needed methods
    comparepath (str) :
        - Path to directory of "correct" products - filenames must match
          output_products
    output_products (list) :
        - List of strings of current output products, to compare with products in
          compare_path

    Returns
    -------
    int: Binary code: Good products, bad products, missing products
    """
    LOG.info("Using compare_outputs_recenter_tc")
    retval = plugin.compare_outputs(compare_path, output_products)
    return retval
