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

"""Test all Recenter TC Output Checker plugins."""
import pytest
import numpy as np
from os import environ

from geoips.interfaces import output_checkers
from geoips.commandline import log_setup


log_setup.setup_logging()


class TestRecenterTCOutputCheckers:
    """TestRecenterTCOutputChecker class, defining methods as well."""

    savedir = str(environ["GEOIPS_PACKAGES_DIR"]) + "/test_data/test_fdecks/pytest/"
    comp_path = savedir + "compare_fdeck._FIX"
    match_path = savedir + "matched_fdeck._FIX"
    close_path = savedir + "close_mismatch_fdeck._FIX"
    bad_path = savedir + "bad_mismatch_fdeck._FIX"
    available_output_checkers = {
        "fdeck": True,
    }

    def clear_fdecks(self):
        """Clear output fdecks so they can be written again."""
        open(self.match_path, "w").close()
        open(self.close_path, "w").close()
        open(self.bad_path, "w").close()

    def yield_fdecks(self):
        """Return a series of varied fdeck files."""
        self.clear_fdecks()
        with open(self.comp_path, mode="r") as comp_fdeck:
            match = open(self.match_path, "w")
            close_mismatch = open(self.close_path, "w")
            bad_mismatch = open(self.bad_path, "w")
            for line in comp_fdeck.readlines():
                for version in range(3):
                    rand = np.random.rand()
                    if version == 0:  # matched
                        match.write(line)
                    elif version == 1:  # Close but mismatched
                        if rand > 0.05:
                            close_mismatch.write(line)
                    else:  # Mismatched -- not close
                        if rand > 0.25:
                            bad_mismatch.write(line)
            match.close()
            close_mismatch.close()
            bad_mismatch.close()
        return self.comp_path, [self.match_path, self.close_path, self.bad_path]

    def yield_plugin_products(self, plugin):
        """Return the appropriate compare/output paths for the corresponding plugin."""
        if plugin.name == "fdeck":
            return self.yield_fdecks()

    def fdeck_comparisons(self, plugin, compare_path, output_paths):
        """Test the comparison of two Fdecks with the Fdeck Output Checker."""
        for path_idx in range(len(output_paths)):
            plugin.module.outputs_match(
                plugin,
                output_paths[path_idx],
                compare_path,
            )

    def compare_plugin(self, plugin):
        """Test the comparision of two products with the appropriate Output Checker."""
        compare_paths, output_paths = self.yield_plugin_products(plugin)
        if plugin.name == "fdeck":
            self.fdeck_comparisons(plugin, compare_paths, output_paths)

    @pytest.mark.parametrize("checker_name", available_output_checkers)
    def test_plugins(self, checker_name):
        """Test all output_checkers that are ready for testing."""
        output_checker = self.available_output_checkers[checker_name]
        if not output_checker or checker_name not in self.available_output_checkers:
            pytest.mark.xfail(checker_name + " is not ready to be tested yet.")
        plugin = output_checkers.get_plugin(checker_name)
        self.compare_plugin(plugin)
