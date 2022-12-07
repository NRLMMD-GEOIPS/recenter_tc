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


## NRLMMD-GEOIPS/recenter_tc#3: 2022-12-07, add mac install instructions
### Documentation
* **New mac-specific system requirements**
    * xcode command line tools
    * Updated `llvm`, `clang`, and `libomp`
* **Additional environment variables for install on mac**
    * LIBRARY_PATH
    * PATH


# v1.5.1: 2022-07-13, update test repo outputs

### Major New Functionality
* **compare_outputs_recenter_tc.py**
    * Add module to handle \*\_FIX fdeck files text comparisons (mimic compare\_outputs\_metoctiff.py).
    * fdeck standard filename contains "." so text filename check fails (since splitext[-1] is not "")

### Test Repo Updates
* **Update Output Directory Structure**
    * abi.tc.Visible.imagery\_clean
    * ahi.tc.IR-BD.imagery\_clean
    * amsr2.tc.color37.imagery\_clean
    * amsr2.tc.windspeed.imagery\_clean
    * amsub\_hdf.tc.157V.imagery\_clean
    * amsub\_mirs.tc.89V.imagery\_clean
    * ascat\_uhr.tc.nrcs.imagery\_clean
    * ascat\_uhr.tc.windbarbs.imagery\_clean
    * gmi.tc.89pct.imagery\_clean
    * hy2b.tc.windspeed.imagery\_clean
    * imerg.tc.Rain.imagery\_clean
    * metopc\_knmi\_125.tc.windbarbs.imagery\_clean
    * modis.tc.Infrared.imagery\_clean
    * oscat.tc.windspeed.imagery\_clean
    * saphir.tc.183-3H.imagery\_clean
    * sar.tc.nrcs.imagery\_clean
    * smap.tc.windspeed.imagery\_clean
    * smos.tc.windspeed.imagery\_clean
    * ssmis.tc.color89.imagery\_clean
    * ssmi.tc.37pct.imagery\_clean
    * viirs.tc.Infrared-Gray.imagery\_clean
* **Update test script names**
    * abi.tc.Visible.imagery\_clean.sh
    * ahi.tc.IR-BD.imagery\_clean.sh
    * amsr2.tc.color37.imagery\_clean.sh
    * amsr2.tc.windspeed.imagery\_clean.sh
    * amsub\_hdf.tc.157V.imagery\_clean.sh
    * amsub\_mirs.tc.89V.imagery\_clean.sh
    * ascat\_uhr.tc.nrcs.imagery\_clean.sh
    * ascat\_uhr.tc.windbarbs.imagery\_clean.sh
    * gmi.tc.89pct.imagery\_clean.sh
    * hy2b.tc.windspeed.imagery\_clean.sh
    * imerg.tc.Rain.imagery\_clean.sh
    * metopc\_knmi\_125.tc.windbarbs.imagery\_clean.sh
    * modis.tc.Infrared.imagery\_clean.sh
    * oscat.tc.windspeed.imagery\_clean.sh
    * saphir.tc.183-3H.imagery\_clean.sh
    * sar.tc.nrcs.imagery\_clean.sh
    * smap.tc.windspeed.imagery\_clean.sh
    * smos.tc.windspeed.imagery\_clean.sh
    * ssmis.tc.color89.imagery\_clean.sh
    * ssmi.tc.37pct.imagery\_clean.sh
    * viirs.tc.Infrared-Gray.imagery\_clean.sh
* **Update test_all.sh for new script names**

### Bug fixes
* **recenter_tc**
    * Update recenter\_with\_archer function to append "run\_archer" filenames to "out\_fnames" for return.
        * Previously typo appended empty list to output filename list.


# v1.5.0: 2022-06-09, geoips2->geoips, GEOIPS\_REPO\_URL, consolidate test outputs, remove old style test scripts

### Test Repo Updates
* **bdeck path update: geoips/tests/sectors/tc_bdecks**
    * Update ALL test scripts to new bdeck sector path
    * Update ALL YAML metadata outputs to new bdeck sector path
* **Update existing clean outputs for new output directory structure**
	* amsr2\_color37
	* amsub\_hdf\_157V
	* amsub\_mirs\_89V
	* gmi\_89pct
	* hy2b\_windspeed
	* sar\_nrcs
	* smap\_windspeed
	* smos\_windspeed
	* viirs\_Infrared-Gray
* **Adding clean output imagery for new test cases**
    * abi\_Visible
    * ahi\_IR-BD
    * amsr2\_windspeed
    * ascat\_uhr\_nrcs
    * ascat\_uhr\_windbarbs
    * imerg\_Rain
    * metopc\_knmi\_125\_windbarbs
    * modis\_Infrared
    * oscat\_windspeed
    * ssmi\_37pct
    * ssmis\_color89
* **Currently non-functional test scripts, with no associated outputs**
	* atms
    * saphir
* **Remove old test outputs and test scripts**
    * abi
    * ahi
    * amsr2
    * amsr2\_winds
    * amsub\_hdf
    * amsub\_mirs
    * ascat\_uhr
    * gmi
    * hy2b
    * imerg
    * metopc\_knmi\_125
    * modis
    * oscat
    * sar
    * smap
    * smos
    * ssmi
    * ssmis
    * viirs
* **YAML outputs**
    * Update from gdeck to bdeck parser
    * Update source\_filename to $GEOIPS bdeck file
    * Update source\_sector\_file to $GEOIPS bdeck file
    * Subset of data types impacted
        * AMSR2
        * AMSU-B HDF
        * AMSU-B MIRS
        * GMI
        * SAR
        * SMAP (both overpasses)
        * SMOS
        * VIIRS
* **Image center**
    * GMI center very slightly changed from bdeck update (17.67% to 17.66% coverage)
* **Replace annotated with clean imagery**
    * AMSR2 color37
    * AMSU-B HDF 157V
    * AMSU-B MIRS 89V
    * GMI 89pct
    * SAR nrcs
    * SMOS windspeed
    * VIIRS Infrared-Gray
    * SMAP and HY2 were already clean imagery
* **Removed unused test outputs**
    * AMSR2 (only color37 tested)
        * 37H
        * 37V
        * 37pct
        * 89H
        * 89V
        * 89pct
        * color89
    * AMSU-B HDF (only 157V tested)
        * 183-3H
    * AMSU-B MIRS (only 89V tested)
        * 183-1H
        * 190V
    * GMI (only 89pct tested)
        * 37H
        * 37pct
        * 89H-Legacy
        * color37
        * color89
    * SAR (only nrcs tested)
        * windspeed
    * VIIRS (only Infrared-Gray tested)
        * Visible

### Refactor
* **File modifications**
    * Update all instances of 'geoips2' with 'geoips'
    * Update all instances of 'GEOIPS2' with 'GEOIPS'

### Documentation Updates
* **README.md**
    * Update GEOIPS\_REPO\_URL to NRL MMD GitHub

### 1.5.0post1 Post Release Patch (2022-06-10)

#### Documentation Updates
* Add system requirements section, noting system requirements beyond what is listed in installation steps directly
    * Fortran compiler supported by f2py, for akima86 build
    * git > 2.19.1, for git -C
    * test data repos in $GEOIPS_BASEDIR/test_data in order for tests to pass.


# v1.4.8: 2022-05-15, update GMI test scripts to new style direct call, setup\_recenter\_tc.sh -> setup.sh

### Major New Functionality
* **GMI test script**
    * Remove "old" style GMI test scripts
    * Add direct GMI test script testing only 89pct recenter_tc functionality (full functionality with YAML config)
    * Update test_all.sh to remove old style and add new direct test script calls.

### Improvements
* **Installation**
    * Update "setup_recenter_tc.sh install_recenter_tc" -> "setup.sh install"
        * For brevity and consistency


# v1.4.7: 2022-05-06, update archer_fix filename for required ATCF filename formatting

### Improvements
* Update archer_fix filename for required ATCF filename formatting
    * Add kwarg for "use_storm_subdirs" default False
    * Add single basin letter to archer_fix filename (must end in, ie, 02W_FIX)
    * Add \_FIX to the end of filename, default to None for extension (so it ends in, ie, 02W\_FIX)
    * Add function to get the single basin letter


# v1.4.6: 2022-04-18, add archer\_fix and archer\_image output capabilities

### Major New Functionality
* Adding archer\_fix and archer\_image filename\_formats.
* Add recenter\_tc/filenames/base\_paths.py
    * include fields specifying filename\_format modules and base paths for ARCHER output
        * ARCHER_IMAGE_PATH
        * ARCHER_IMAGE_FILENAME_FORMAT
        * ARCHER_FIX_PATH
        * ARCHER_FIX_FILENAME_FORMAT
* Output archer\_fix and archer\_image filenames within recenter\_tc module, using above environment variables
    for PATHs and FILENAME_FORMAT modules
* Update all ARCHER based functions called from recenter\_tc to return out\_fnames list as well as area\_defs
    (so we can track as additional output products from top level procflow)
    * Updated adjuster\_type to list\_xarray\_list\_variables\_to\_area\_def\_out\_fnames so we are backwards
        compatible with potential area_def_adjusters that do NOT return a list of out_fnames.


# v1.4.5: 2022-03-18, compare\_paths->compare\_path

### Refactor
* Replace compare\_paths with compare\_path in test scripts
    * amsr2.sh
    * amsub\_hdf.sh
    * amsub\_mirs.sh
    * hy2.sh
    * sar.sh
    * smap.sh
    * smos.sh
    * viirs.sh


# v1.4.4: 2022-03-06, test image updates: informative colorbar labels, correct AHI Visible scaling

### Test Repo Updates
* Informative colorbar label for VIIRS and ABI Visible products, images unchanged
    * Include channel and wavelength.
* Corrected AHI Visible image scaling, updated colorbar label


# v1.4.3: 2022-02-17, correct ambiguity test outputs, jpss-1 to noaa-20

### Test Repo Updates
* Updating ASCAT UHR ambiguities plot so it actually includes ambiguities.
* Update test outputs for jpss-1 to noaa-20


# v1.4.2: 2022-02-05, update test outputs for Natural Earth Vector v5.0.0 shapefiles

### Test Repo Updates
    * Updated recenter_tc test outputs for latest natural earth data.
        * Updated natural earth data shapefiles to v5.0.0, used for cartopy plotting
        * AMSR2/SSMI/SSMIS TC2020IO01: A new political boundary on the left side of imagery
        * ASCAT UHR NRCS/ METOP-C windspeed TC2021WP02: A new political boundary on the left side of imagery


# v1.4.1: 2022-01-21, recenter_tc viirs output config test scripts

### Major New Functionality
    * Add explicit command line single source based test script
        * VIIRS Infrared-Gray

### Improvements
    * Update test_all.sh to use new explicit test script
        * Remove old-style VIIRS test module


# v1.4.0: 2022-01-12, add direct test scripts, update for explicit metadata output requests

### Major New Functionality
    * Add hy2 explicit single source test script
        * metadata default output
        * clean windspeed product
        * akima recentering
    * Update hy2 metadata YAML to use $GEOIPS bdeck rather than test_data_hy2
        * For simplicity and completeness, keep as many deck files as output products in $GEOIPS as possible.

### Refactor
    * Convert SAR, SMOS test scripts to direct calls
        * Removed old-style and added new to test_all.sh
        * Remove old-style scripts/data_types/smos
        * Added direct single_source command line call to scripts/smos.sh
    * Update all test scripts to include explicit request for default metadata YAML outputs
        * amsr2
        * amsub_hdf
        * amsub_mirs
        * sar
        * smap
        * smos


# v1.3.2: 2021-12-21, bug fix: tc\_clean fname for hy2 product

### Bug fixes
    * Use hy2 "clean" fname for test output, since producing "clean" imagery


# v1.3.1: 2021-12-07, hscat outputs, remove duplicates before akima, updated amsub/amsr2/smap test scripts

### Major New Functionality
    * hscat hy-2b recentered product outputs
        * windspeed

### Improvements
    * Added explicit test scripts for "finalized" config-based data types
        * amsr2 (color37)
        * amsub_hdf (157V)
        * amsub_mirs (89V)
        * smap (windspeed)
    * Remove old test scripts from test_all.sh, added new
    * Removed old style testing modules from tests/scripts/data_types


### Bug fixes
    * Remove duplicate storm positions prior to applying akima interpolation
        * positions must be monotonically increasing, so remove any duplicates
    * Updated amsr2_winds windspeed_image yaml metadata file
        * renamed original_source_filename to original_source_filenames
        * updated product_filename path to use preprocessed instead of GeoIPSfinal
        * added sector_type: tc


# v1.3.0: 2021-11-25, atcf -> tc, remove satops

### Breaking Interface Changes
    * recenter_tc area_def_adjuster: sector_type atcf -> tc

### Breaking Test Repo Updates
    * Updated all TC metadata YAML outputs
        * geoips_outdirs/satops/intermediate_files/GeoIPSfinal/tcwww -> geoips_outdirs/preprocessed/tcwww
        * add sector_type: tc


# v1.2.5: 2021-11-18, update README

### Improvements
    * Add geoips base_install_and_test.sh call to README


# v1.2.4: 2021-11-12, original_source_filename->original_source_filenames

### Breaking Test Repo Updates
    * Replaced original_source_filename attribute with list of original_source_filenames
        * Updated all metadata YAML outputs


# v1.2.2: 2021-10-25, finalized SAR/ASCAT NRCS products, updated test outputs from TC padding update.

### Breaking Test Repo Updates
    * Updated TC padding from 2.5x to 1.5x, slightly modifying some interpolated / center times
        * AMSR2
        * GMI
        * KNMI METOPC
        * OSCAT
        * SMAP
        * SMOS
        * SSMI/S
    * Updated SMAP 
        * tc_clean output
        * new test dataset
        * now produce both overpasses rather than one

### Improvements
    * Finalized NRCS products
        * SAR (10*log10(sigma)
        * ASCAT UHR (no longer named sigma0)


# v1.2.3: 2021-11-05, updated recentered filenames, updated test scripts to exit with valid return code

### Breaking Test Repo Updates
    * Added adjustment_id to each output filename, to quickly identify products that were successfully recentered
        * "ar<chan>" for ARCHER recentering
        * "akima" for akima interpolation only

### Improvements
    * Updated test scripts to exit with valid return code, to support updated test_all.sh script


# v1.2.2: 2021-10-25, finalized SAR/ASCAT NRCS products, updated test outputs from TC padding update.

### Breaking Test Repo Updates
    * Updated TC padding from 2.5x to 1.5x, slightly modifying some interpolated / center times
        * AMSR2
        * GMI
        * KNMI METOPC
        * OSCAT
        * SMAP
        * SMOS
        * SSMI/S
    * Updated SMAP 
        * tc_clean output
        * new test dataset
        * now produce both overpasses rather than one

### Improvements
    * Finalized NRCS products
        * SAR (10*log10(sigma)
        * ASCAT UHR (no longer named sigma0)


# v1.2.1: 2021-10-05, Test repo output updates, and code refactor/simplification

### Breaking Test Repo Updates
    * Updated cartopy to 0.20.0 and matplotlib to v3.4.3
        * test repo outputs incompatible with matplotlib < 3.4.0 and cartopy < 0.19.0
        * Older versions have figures that are very slightly shifted from later versions
        * Exclusively a qualitative difference, but it *does* cause the test comparisons to fail

### Refactor
    * Moved recenter_tc plugin to a separate installable repository

### Major New Functionality:
    * Added exhaustive "test_all.sh" script with successful 0 return.
        * Input data stored within standard test_data_<sensor> repos, test outputs stored within recenter_tc plugin repo

### Improvements
    * Standardized and formalized the README, setup script, and test script format for all plugin repos
    * Removed requirement to link test scripts from plugin repos into the main geoips test directory
