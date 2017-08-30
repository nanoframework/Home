# CMake file for building mbed OS from sources

**About this document**

This document describes the purpose and workflow for the CMake configuration files to build mbed OS from the repository sources.
Building mbed OS from sources might be needed when debugging a **nanoFramework** feature that interacts with it.


# Purpose

The purpose of the configuration files collections is to create a CMake package for mbed and build it.

# Reasoning

The sources from mbed can be downloaded from their GitHub repository or, if already available in the build machine, can be copied to the build folder.
When invoking CMake these options is passed specifying ```RTOS=mbedRTOS``` and ```mbed_SOURCE=path-to-the-local-repository-folder```.
Building mbed OS requires a bunch of source files and passing a number of compiler definitions. These are either preset according to the target and series or are read from the _targets.json_ file in the targets folder.

# Workflow

Because CMake has no native capability to parse json files we are relying on a third party library to do that.
We are not parsing the complete _targets.json_ file because of it's size and the time it takes to parse it which would negatively impact on the build speed. Instead the _targets.json_ file is searched for the mbed target specified in ```mbed_TARGETRTOS=target-name```. After finding the target and following an educated guess on the total size that a target definition takes on the file, that section of the json file is parsed. The down side is that most of the times we runover into the next target definition. The CMake code takes care of that by processing only the items that belong to the target collection.

After succesfully parsing the target details CMake stores the relevant portions for later use. Please check the code at [FindmbedOS.cmake](../../CMake/Modules/FindmbedOS.cmake) for details.
(NOTE: the current code has been validated for STM targets only)

Because of it broad targeting mbed source is comprised of several interface files and common structures and types. This makes it somewhat difficult to gather all the required files for a specific target. The folder structure is such that there are folders for each support vendor. Inside of these are the series of the MCUs. For some series there are in turn specific folders for targets.

The _FindmbedOS.cmake_ includes the specifics for the target series and the respective GCC options.
The file naming logic is:
- mbed_**STM**_sources.cmake: common source files for the vendor (with the vendor name in bold)
- mbed_**STM32F0**_sources.cmake: common source files for the series (with the series name in bold)
- mbed_**STM32F0**_GCC_options.cmake: GCC options for the series (with the series name in bold)

When adding a new vendor/series/target follow these general guidelines:
1. Check if vendor file exists. If not, create it and add the source files at the vendor base folder.
2. Check if the series file exists. If not, create it, add the source files at the series base folder and include the vendor source code above.
3. Check if the target startup file and the linker file (and possibly other specific files for the target) are listed in the series file. If not, add them.
