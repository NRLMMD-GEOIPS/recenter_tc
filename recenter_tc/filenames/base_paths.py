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

"""Collection of base path names used throughout GeoIPS.

Everything defaults to subdirectories relative to the REQUIRED
environment variable GEOIPS_OUTDIRS.  Individual GEOIPS_OUTDIRS
relative paths can be overridden by setting appropriate environment variables.
"""


# Python Standard Libraries
import logging
from os import getenv
from os.path import join as pathjoin
from geoips.filenames.base_paths import PATHS as GPATHS

LOG = logging.getLogger(__name__)

PATHS = {}

if getenv("ARCHER_IMAGE_PATH"):
    PATHS["ARCHER_IMAGE_PATH"] = getenv("ARCHER_IMAGE_PATH").rstrip("/")
else:
    PATHS["ARCHER_IMAGE_PATH"] = pathjoin(
        GPATHS["GEOIPS_OUTDIRS"], "preprocessed", "archer", "image"
    )

if getenv("ARCHER_IMAGE_FILENAME_FORMAT"):
    PATHS["ARCHER_IMAGE_FILENAME_FORMAT"] = getenv(
        "ARCHER_IMAGE_FILENAME_FORMAT"
    ).rstrip("/")
else:
    PATHS["ARCHER_IMAGE_FILENAME_FORMAT"] = "archer_image"


if getenv("ARCHER_FIX_PATH"):
    PATHS["ARCHER_FIX_PATH"] = getenv("ARCHER_FIX_PATH").rstrip("/")
else:
    PATHS["ARCHER_FIX_PATH"] = pathjoin(
        GPATHS["GEOIPS_OUTDIRS"], "preprocessed", "archer", "fix"
    )

if getenv("ARCHER_FIX_FILENAME_FORMAT"):
    PATHS["ARCHER_FIX_FILENAME_FORMAT"] = getenv("ARCHER_FIX_FILENAME_FORMAT").rstrip(
        "/"
    )
else:
    PATHS["ARCHER_FIX_FILENAME_FORMAT"] = "archer_fix"
