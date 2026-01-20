# # # This source code is subject to the license referenced at
# # # https://github.com/NRLMMD-GEOIPS.

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
