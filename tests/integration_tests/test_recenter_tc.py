# # # This source code is subject to the license referenced at
# # # https://github.com/NRLMMD-GEOIPS.

"""Pytest file for calling integration bash scripts."""

import os
import pytest

# Only use base_setup, because full_setup requires ALL test data repositories.
from tests.integration_tests.test_integration import base_setup  # noqa: F401

from tests.integration_tests.test_integration import (
    run_script_with_bash,
    setup_environment as setup_geoips_environment,
)

# Single base test to ensure plugin repo works at all.
base_integ_test_calls = [
    "$repopath/tests/scripts/gmi.tc.89pct.imagery_clean.sh",
]

# Exhaustive test of all remaining functionality in this repo (excluding base test).
full_integ_test_calls = [
    "$geoips_repopath/tests/utils/check_code.sh all $repopath",
    "$geoips_repopath/docs/build_docs.sh $repopath $pkgname html_only",
    "$repopath/tests/scripts/abi.tc.Visible.imagery_clean.sh",
    "$repopath/tests/scripts/ahi.tc.IR-BD.imagery_clean.sh",
    "$repopath/tests/scripts/amsr2.tc.color37.imagery_clean.sh",
    "$repopath/tests/scripts/amsr2.tc.windspeed.imagery_clean.sh",
    "$repopath/tests/scripts/amsua_mhs_mirs.tc.89V.imagery_clean.sh",
    "$repopath/tests/scripts/ascat_uhr.tc.nrcs.imagery_clean.sh",
    "$repopath/tests/scripts/ascat_uhr.tc.windbarbs.imagery_clean.sh",
    "$repopath/tests/scripts/imerg.tc.Rain.imagery_clean.sh",
    "$repopath/tests/scripts/metopc_knmi_125.tc.windbarbs.imagery_clean.sh",
    "$repopath/tests/scripts/modis.tc.Infrared.imagery_clean.sh",
    "$repopath/tests/scripts/oscat.tc.windspeed.imagery_clean.sh",
    "$repopath/tests/scripts/saphir.tc.183-3H.imagery_clean.sh",
    "$repopath/tests/scripts/sar.tc.nrcs.imagery_clean.sh",
    "$repopath/tests/scripts/smap.tc.windspeed.imagery_clean.sh",
    "$repopath/tests/scripts/smos.tc.windspeed.imagery_clean.sh",
    "$repopath/tests/scripts/viirs.tc.Infrared-Gray.imagery_clean.sh",
]
# Test scripts that require test datasets with limited availability.
limited_data_integ_test_calls = [
    "$repopath/tests/scripts/amsub_hdf.tc.157V.imagery_clean.sh",
    "$repopath/tests/scripts/hy2b.tc.windspeed.imagery_clean.sh",
    "$repopath/tests/scripts/ssmis.tc.color91.imagery_clean.sh",
    "$repopath/tests/scripts/ssmi.tc.37pct.imagery_clean.sh",
]


def setup_environment():
    """
    Set up necessary environment variables for integration tests.

    Configures paths and package names for the GeoIPS core and its plugins by
    setting environment variables required for the integration tests. Assumes
    that 'GEOIPS_PACKAGES_DIR' is already set in the environment.

    Notes
    -----
    The following environment variables are set:
    - geoips_repopath
    - geoips_pkgname
    - repopath
    - pkgname
    """
    # Setup base geoips environment
    setup_geoips_environment()
    # Setup current repo's environment
    os.environ["repopath"] = os.path.join(os.path.dirname(__file__), "..", "..")
    os.environ["pkgname"] = "recenter_tc"


@pytest.mark.base
@pytest.mark.integration
@pytest.mark.parametrize("script", base_integ_test_calls)
def test_integ_base_test_script(base_setup: None, script: str):  # noqa: F811
    """
    Run integration test scripts by executing specified shell commands.

    Parameters
    ----------
    script : str
        Shell command to execute as part of the integration test. The command may
        contain environment variables which will be expanded before execution.

    Raises
    ------
    subprocess.CalledProcessError
        If the shell command returns a non-zero exit status.
    """
    setup_environment()
    run_script_with_bash(script)


@pytest.mark.full
@pytest.mark.integration
@pytest.mark.parametrize("script", full_integ_test_calls)
def test_integ_full_test_script(base_setup: None, script: str):  # noqa: F811
    """
    Run integration test scripts by executing specified shell commands.

    Parameters
    ----------
    script : str
        Shell command to execute as part of the integration test. The command may
        contain environment variables which will be expanded before execution.

    Raises
    ------
    subprocess.CalledProcessError
        If the shell command returns a non-zero exit status.
    """
    setup_environment()
    run_script_with_bash(script)


# These are required to test the full functionality of this repo, but have limited
# test dataset availability, so mark them as optional.
@pytest.mark.optional
@pytest.mark.integration
@pytest.mark.parametrize("script", limited_data_integ_test_calls)
def test_integ_limited_data_script(base_setup: None, script: str):  # noqa: F811
    """
    Run integration test scripts by executing specified shell commands.

    Parameters
    ----------
    script : str
        Shell command to execute as part of the integration test. The command may
        contain environment variables which will be expanded before execution.

    Raises
    ------
    subprocess.CalledProcessError
        If the shell command returns a non-zero exit status.
    """
    setup_environment()
    run_script_with_bash(script)
