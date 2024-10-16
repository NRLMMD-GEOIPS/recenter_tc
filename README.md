    # # # This source code is protected under the license referenced at
    # # # https://github.com/NRLMMD-GEOIPS.

Tropical Cyclone Recentering GeoIPS Plugin
===========================================

The recenter_tc package is a GeoIPS-compatible plugin, intended to be used within the GeoIPS ecosystem.
Please see the
[GeoIPS Documentation](https://github.com/NRLMMD-GEOIPS/geoips#readme)
for more information on the GeoIPS plugin architecture and base infrastructure.

Package Overview
-----------------

The recenter_tc package provides the capability for identifying the most accurate storm center
based on best track and storm forecast information, as well as the data itself.

Two separate packages are used in determining the most accurate storm center:

### akima86 fortran based interpolation

H. Akima 1986, Python adaptation D. Ryglicki 2020

This takes in all current best track information, forecasted storm locations, as well as the
actual time of the data file itself.  The 6-hourly storm location information is interpolated
to the actual data time.

### Automated Rotational Center Hurricane Eye Retrieval (ARCHER)

T. Wimmers University of Wisconsin Cooperative Institute for Meteorological Satellite Studies

Using the akima86 interpolated center as a starting point, ARCHER identifies the actual storm
center from the data itself.  ARCHER operates on passive microwave, visible, and infrared data types

### recenter_tc wrapper "area_def_adjuster"

akima86 and archer are called via the recenter_tc "area_def_adjuster" plugin.  Currently, the recenter_tc
area_def_adjuster is accessed by specifying the "--adjust_area_def recenter_tc" command line argument,
and the procflows handle calling akima86, calling archer, adjusting the area definition appropriately,
and generating related ARCHER f-deck and image outputs.

ARCHER output currently defaults to $GEOIPS_OUTDIRS/preprocessed/archer, and filename formats and locations
can be adjusted via adjustments to filename_format plugins.  Future updates to the recenter_tc plugin package
will provide easier access to adjusting the ARCHER output - it is currently controlled via environment variables
specifying which filename format plugins to use for both image and fix outputs.

The default filename format plugins currently in use within recenter_tc are:
* export ARCHER_IMAGE_FILENAME_FORMAT=archer_image
    * Located in recenter_tc/interface_modules/filename_formats/archer_image.py
* export ARCHER_FIX_FILENAME_FORMAT=archer_fix
    * Located in recenter_tc/interface_modules/filename_formats/archer_fix.py

System Requirements
---------------------

* geoips >= 1.10.0
* akima86 Python package, and required dependencies
* archer Python package, and required dependencies
* Test data repos contained in $GEOIPS_TESTDATA_DIR for tests to pass.

IF REQUIRED: Install base geoips package
------------------------------------------------------------
SKIP IF YOU HAVE ALREADY INSTALLED BASE GEOIPS ENVIRONMENT

If GeoIPS Base is not yet installed, follow the
[installation instructions](https://github.com/NRLMMD-GEOIPS/geoips#installation)
within the geoips source repo documentation:

Install recenter_tc package
----------------------------
```bash
    # Assuming you followed the fully supported installation,
    # using $GEOIPS_PACKAGES_DIR and $GEOIPS_CONFIG_FILE:
    source $GEOIPS_CONFIG_FILE
    git clone https://github.com/NRLMMD-GEOIPS/recenter_tc $GEOIPS_PACKAGES_DIR/recenter_tc
    pip install -e $GEOIPS_PACKAGES_DIR/recenter_tc
    create_plugin_registries
```

Test recenter_tc installation
-----------------------------
```bash

    # Ensure GeoIPS Python environment is enabled.

    # If you have the full ABI and AMSR2 test datasets:
    $GEOIPS_PACKAGES_DIR/recenter_tc/tests/scripts/abi.tc.Visible.imagery_clean.sh
    $GEOIPS_PACKAGES_DIR/recenter_tc/tests/scripts/amsr2.tc.color37.imagery_clean.sh

    # If you have all test data repos available:
    $GEOIPS_PACKAGES_DIR/recenter_tc/tests/test_all.sh
```
