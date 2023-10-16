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

"""Test script for running representative products.

Uses data and comparison outputs from geoips_test_data/_/*
"""
import logging

from geoips.compare_outputs import compare_outputs, test_product, text_match

LOG = logging.getLogger(__name__)


def is_fdeck(fname):
    """Check if fname is an fdeck file.

    Parameters
    ----------
    fname: str
        Name of file to check.

    Returns
    -------
    bool: boolean
        True if it is an fdeck file (``*_FIX``), False otherwise.
    """
    if fname.split("_")[-1] in ["FIX"]:
        with open(fname) as f:
            line = f.readline()
        if isinstance(line, str):
            return True
    return False


def test_product_recenter_tc(
    output_product, compare_product, goodcomps, badcomps, compare_strings
):
    """Test output_product against "good" product stored in "compare_path".

    Parameters
    ----------
        output_product
    """
    matched_one = True
    try:
        goodcomps, badcomps, compare_strings = test_product(
            output_product, compare_product, goodcomps, badcomps, compare_strings
        )
    except TypeError:
        matched_one = False

    LOG.info("Using test_product_recenter_tc")
    if is_fdeck(output_product):
        matched_one = True
        compare_strings += ["FDECK "]
        if text_match(output_product, compare_product):
            goodcomps += [f"FDECK {output_product}"]
        else:
            badcomps += [f"FDECK {output_product}"]

    if not matched_one:
        raise TypeError(f"MISSING TEST for output product: {output_product}")

    return goodcomps, badcomps, compare_strings


def compare_outputs_recenter_tc(compare_path, output_products):
    """Compare the "correct" imagery.

    Correct imagery found in comparepath with the list of current output_products.

    Parameters
    ----------
    comparepath: str
        Path to directory of "correct" products - filenames must match output_products
    output_products: list
        List of strings of current output products,
        to compare with products in compare_path

    Returns
    -------
    int: Binary code
        Good products, bad products, missing products
    """
    LOG.info("Using compare_outputs_recenter_tc")
    retval = compare_outputs(
        compare_path, output_products, test_product_func=test_product_recenter_tc
    )

    return retval
