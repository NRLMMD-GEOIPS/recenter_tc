Pre Version 1.10.0a12 (2023-05-02)
**********************************

* Update command line argument in test scripts from
  adjust_area_def to sector_adjuster
* Update command line argument in test scripts from
  tc_template_yaml to tc_spec_template

Breaking Change
===============

Update command line argument from tc_template_yaml to tc_spec_template
----------------------------------------------------------------------

::

  modified: tests/scripts/ascat_uhr.tc.windbarbs.imagery_clean.sh
  modified: tests/scripts/metopc_knmi_125.tc.windbarbs.imagery_clean.sh

Update command line argument from adjust_area_def to sector_adjuster
--------------------------------------------------------------------

Standardize naming to use the interface names for the command line arguments.

::

  modified: tests/scripts/abi.tc.Visible.imagery_clean.sh
  modified: tests/scripts/ahi.tc.IR-BD.imagery_clean.sh
  modified: tests/scripts/amsr2.tc.color37.imagery_clean.sh
  modified: tests/scripts/amsr2.tc.windspeed.imagery_clean.sh
  modified: tests/scripts/amsub_hdf.tc.157V.imagery_clean.sh
  modified: tests/scripts/amsub_mirs.tc.89V.imagery_clean.sh
  modified: tests/scripts/ascat_uhr.tc.nrcs.imagery_clean.sh
  modified: tests/scripts/ascat_uhr.tc.windbarbs.imagery_clean.sh
  modified: tests/scripts/atms.tc.165H.imagery_clean.sh
  modified: tests/scripts/gmi.tc.89pct.imagery_clean.sh
  modified: tests/scripts/hy2b.tc.windspeed.imagery_clean.sh
  modified: tests/scripts/imerg.tc.Rain.imagery_clean.sh
  modified: tests/scripts/metopc_knmi_125.tc.windbarbs.imagery_clean.sh
  modified: tests/scripts/modis.tc.Infrared.imagery_clean.sh
  modified: tests/scripts/oscat.tc.windspeed.imagery_clean.sh
  modified: tests/scripts/saphir.tc.183-3H.imagery_clean.sh
  modified: tests/scripts/sar.tc.nrcs.imagery_clean.sh
  modified: tests/scripts/smap.tc.windspeed.imagery_clean.sh
  modified: tests/scripts/smos.tc.windspeed.imagery_clean.sh
  modified: tests/scripts/ssmi.tc.37pct.imagery_clean.sh
  modified: tests/scripts/ssmis.tc.color91.imagery_clean.sh
  modified: tests/scripts/viirs.tc.Infrared-Gray.imagery_clean.sh
