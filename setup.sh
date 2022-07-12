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

#!/bin/bash

if [[ -z "$GEOIPS_BASEDIR" ]]; then
    echo "Must define GEOIPS_BASEDIR environment variable prior to setting up geoips packages"
    exit 1
fi

# This sets required environment variables for setup - without requiring sourcing a geoips config in advance
. $GEOIPS_BASEDIR/geoips_packages/geoips/setup/repo_clone_update_install.sh setup

# Do not include geoips and geoips_system_nrl in list.
# These are both required to get setup scripts, so handle separately
internal_plugins=""
internal_algs="akima86"
external_repos="archer"
test_repos=""

if [[ "$1" == "repo_clone" ]]; then

    # Uses internal_plugins, internal_algs, external_repos, and test_repos variables
    . $GEOIPS_PACKAGES_DIR/geoips/setup/repo_clone_update_install.sh repo_clone

elif [[ "$1" == "repo_update" ]]; then

    # Uses internal_plugins, internal_algs, external_repos, and test_repos variables
    . $GEOIPS_PACKAGES_DIR/geoips/setup/repo_clone_update_install.sh repo_update $2

elif [[ "$1" == "install" ]]; then
    pip install -e $GEOIPS_PACKAGES_DIR/recenter_tc

    # Uses internal_plugins, internal_algs, and external_repos variables
    . $GEOIPS_PACKAGES_DIR/geoips/setup/repo_clone_update_install.sh install_plugins

else
    echo "UNRECOGNIZED COMMAND $1"
    exit 1
fi

