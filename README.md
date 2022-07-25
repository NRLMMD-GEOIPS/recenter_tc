    # # # Distribution Statement A. Approved for public release. Distribution unlimited.
    # # # 
    # # # Author:
    # # # Naval Research Laboratory, Marine Meteorology Division
    # # # 
    # # # This program is free software:
    # # # you can redistribute it and/or modify it under the terms
    # # # of the NRLMMD License included with this program.
    # # # 
    # # # If you did not receive the license, see
    # # # https://github.com/U-S-NRL-Marine-Meteorology-Division/
    # # # for more information.
    # # # 
    # # # This program is distributed WITHOUT ANY WARRANTY;
    # # # without even the implied warranty of MERCHANTABILITY
    # # # or FITNESS FOR A PARTICULAR PURPOSE.
    # # # See the included license for more details.

Installation Guide
==================

This installation guide has installation steps specific to installing this plugin, including
the base geoips conda install if not already installed.


System Requirements
---------------------

* Fortran compiler supported by f2py required for akima86 dependency - load appropriately prior to installation.
* git > 2.19.1 for "git -C" clone commands
* Test data repos contained in $GEOIPS_BASEDIR/test_data/ for tests to pass.


Setup System Environment Variables
----------------------------------

```bash
    # Set up appropriate environment variables for all conda-based geoips_template_plugin setup steps
    # within this geoips_template_plugin README below

    # These steps will need to be copied and pasted into your shell any time you want to run the 
    # setup commands within this README.
    
    # Typical users do not have to make any modifications to the commands
    # within this README, and can copy and paste directly.

    # Once geoips_template_plugin has been installed, the "GEOIPS_CONFIG_FILE" specified below will be
    # sourced when running geoips_template_plugin, and the direct environment variable assignments
    # within this section are no longer required.

    # If you would like to have the GEOIPS_CONFIG_FILE automatically sourced so you do not have to manually run the 
    # source command for every new shell, you can add 
    # source </full/path/to/config/file>
    # to your ~/.bashrc file

    # GEOIPS_REPO_URL should point to the base URL for git clone commands
    export GEOIPS_REPO_URL=https://github.com/NRLMMD-GeoIPS

    # GEOIPS_BASEDIR will contain all source, output, and external dependencies
    # Ensure this is consistently set for all installation / setup steps below
    export GEOIPS_BASEDIR=$HOME/geoproc

    # This config file must be sourced ANY TIME you want to run the geoips geoips_template_plugin plugin
    export GEOIPS_CONFIG_FILE=$GEOIPS_BASEDIR/geoips_packages/geoips_nrl/setup/config_geoips_nrl

```

Clone recenter_tc git repositories required for setup scripts
-------------------------------------------------------------
```bash
    mkdir -p $GEOIPS_BASEDIR/geoips_packages/

    git clone $GEOIPS_REPO_URL/geoips.git $GEOIPS_BASEDIR/geoips_packages/geoips
    git -C $GEOIPS_BASEDIR/geoips_packages/geoips pull
    git -C $GEOIPS_BASEDIR/geoips_packages/geoips checkout -t origin/dev
    git -C $GEOIPS_BASEDIR/geoips_packages/geoips checkout dev
    git -C $GEOIPS_BASEDIR/geoips_packages/geoips pull

    git clone $GEOIPS_REPO_URL/recenter_tc.git ${GEOIPS_BASEDIR}/geoips_packages/recenter_tc
    git -C ${GEOIPS_BASEDIR}/geoips_packages/recenter_tc pull
    git -C ${GEOIPS_BASEDIR}/geoips_packages/recenter_tc checkout -t origin/dev
    git -C ${GEOIPS_BASEDIR}/geoips_packages/recenter_tc checkout dev
    git -C ${GEOIPS_BASEDIR}/geoips_packages/recenter_tc pull
```

IF REQUIRED: Install and test base geoips conda environment
------------------------------------------------------------
```bash
    # SKIP IF YOU HAVE ALREADY INSTALLED BASE GEOIPS CONDA ENVIRONMENT 
    # This prompts you through all the steps of installing the geoips conda environment from scratch,
    # using the parameters specified above.  This only needs to be done once per system, skip if you
    # already ran this step.
    $GEOIPS_BASEDIR/geoips_packages/geoips/base_install_and_test.sh dev
```

Install recenter_tc package
-------------------------
```bash
    $GEOIPS_BASEDIR/geoips_packages/recenter_tc/setup.sh repo_clone
    $GEOIPS_BASEDIR/geoips_packages/recenter_tc/setup.sh repo_update
    source $GEOIPS_CONFIG_FILE
    pip install -e $GEOIPS_BASEDIR/geoips_packages/geoips
    $GEOIPS_BASEDIR/geoips_packages/recenter_tc/setup.sh install
```

Test recenter_tc installation - these test scripts provide you with the full command line calls
---------------------------------------------------------------------------------------------
```bash
    source $GEOIPS_CONFIG_FILE
    # These "old" style test scripts will later be replaced with "new" test scripts
    $GEOIPS_PACKAGES_DIR/recenter_tc/tests/scripts/amsr2.sh
    $GEOIPS_PACKAGES_DIR/recenter_tc/tests/scripts/smap.sh
```
