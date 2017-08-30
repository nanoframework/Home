# CMake file for ST Cube repository folder

**About this document**

This document describes the purpose and workflow for the CMake configuration file on the *stcube-repository* folder.


<a name="Purpose"></a>
# Purpose

The purpose of this configuration file is to download the appropriate ST Cube package from ST's web site and unzip it to the appropriate location.


<a name="Reasoning"></a>
# Reasoning

Each ST Cube package file has several hundred MB which can take a bit longer to download, therefore contributing to make the build process slower. 
The *stcube-repository* folder is meant to hold the packages as a cache in order to speed up the build process.
The ZIP file with the packages are downloaded from ST's web site and stored in this folder.
After the download the file is unzipped to the respective series directory (with follows the series name). The documentation, utilities, example projects and other non code files are deleted in order to save disk space.
If the destination folder doesn't exist, CMake will try to find the ZIP file for the package. If the file exists it will be unzipped, if not it will be downloaded.     


<a name="workflow"></a>
# Workflow

The configuration file relies on the STM32_SERIES variable to determine what is the SMT32 series along with the PACKAGE_VERSION variable that holds the package version that the build is expected to use.
The PACKAGE_VERSION is checked for the correct format which follows the standard format _MAJOR.MINOR.PATCH_.
The distribution of ST Cube packages has a particularity: when a package is a patch (meaning that the rightmost number is not zero) it only holds the patched files. This means that the original package is required too. 
For example, if the target version is 1.13.2 (witch is a patch for v1.13.0) we need two files: the original one (v1.13.0) and the patch (v1.13.2). The destination directory has to be cleaned up before unzipping the first one and then the second one is unzip overwriting the patched files.

The file naming of the ST Cube packages distribution files follows the following format: *stm32cube_fw_f0_v160.zip*.
Note the series name and the version. All in small case and the version number without dots.
After unzipping the destination directory name will be STM32Cube_FW_F0_V1.6.0.
Note that the version number now has the dots and that the name is all in upper case, except for the 'Cube' name.

The base URL for downloading the package files from ST's web is "http://www.st.com/resource/en/firmware2". To have the complete URL for downloading a file just add the package file name to the base URL.

To ease the management and search of the 'cache' and destination directories, the destination directory for the build (were the ST Cube package code is actually placed) is named just *stcube* (dropping the _repository).
