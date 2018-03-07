# Instructions for building **nanoFramework** images

## Table of contents ##

- [Prerequisites](#prerequisites)
- [Preparation](#preparation)
- [Build a **nanoFramework** image](#build-a-nanoframework-image)
- [**nanoFramework** build deliverables](#nanoframework-build-deliverables)

**About this document**

This document describes how to build the required images for **nanoFramework** to be flashed in a SoC or MCU.
The build is based on CMake tool to ease the development in all major platforms.

# Prerequisites

You'll need:
- [GNU ARM Embedded Toolchain](https://developer.arm.com/open-source/gnu-toolchain/gnu-rm/downloads)
- [CMake](https://cmake.org/) (Minimum required version is 3.7)
- A build system for CMake to generate the build files to. 
  + If you have Visual Studio (full version) you can use the included NMake.
  + A nice alternative is [Ninja](https://github.com/ninja-build/ninja). This is lightweight build system, designed for speed and it works on Windows and Linux machines. See [here](cmake/ninja-build.md) how to setup Ninja to build **nanoFramework**.

If you are using VS Code as your development platform we suggest that you use the CMake Tools extension. This will allow you to run the builds without leaving VS Code.
- [Visual Studio Code](http://code.visualstudio.com/)
- [CMake Extension](https://marketplace.visualstudio.com/items?itemName=twxs.cmake)
- [CMake Tools Extension](https://marketplace.visualstudio.com/items?itemName=vector-of-bool.cmake-tools)

In case you specify an RTOS and you want its source to be downloaded from the official repository, you'll need:
- For FreeRTOS a SVN client. [Tortoise SVN](https://tortoisesvn.net/downloads) seems to be a popular choice for Windows machines.
- For mbed and ChibiOS a Git client. [GitHub Desktop](https://desktop.github.com/) seems to be a popular choice for Windows machines.

# Preparation

It's ***highly*** recommended that run the build outside the source tree. This prevents you from cluttering the source tree with CMake artifacts, temporary files etc. 
In fact this is enforced and checked by the CMake script.

In case you need to clean up or start a fresh build all you have to do is simply delete the contents of the build directory.

As a suggestion we recommend that you create a directory named *build* in the repository root and run CMake from there.



# Build a **nanoFramework** image

The build script accepts the a number of parameters (some of them are mandatory). Please check the details about each parameter [here](cmake-tools-cmake-variants.md#content-explained).

_Note 1: The RTOS currently supported (except for ESP32 target) is ChibiOS. If no source path is specified the source files will be downloaded from nanoFramework  GitHub fork._
_Note 2: the very first build will take more or less time depending on the download speed of the Internet connection of the machine were the build is running. This is because the source code of the RTOS of your choice will be downloaded from its repository. On the subsequent builds this won't happen._

You can specify any generator that is supported in the platform where you are building.
For more information on this check CMake documentation [here](https://cmake.org/cmake/help/v3.7/manual/cmake-generators.7.html?highlight=generator).


## Building from the command prompt

If you are building from the command prompt, just go to your *build* directory and run CMake from there with the appropriate parameters. 
The following is a working example:

```
cmake \
-DTOOLCHAIN_PREFIX="E:/GNU_Tools_ARM_Embedded/5_4_2016q3" \
-DCHIBIOS_VERSION=17.6.0 \
-DCHIBIOS_BOARD=ST_NUCLEO_F091RC \
-DTARGET_SERIES=STM32F0xx \
-DNF_FEATURE_DEBUGGER=TRUE \
-DAPI_Windows.Devices.Gpio=ON \
-DNF_FEATURE_RTC=ON \
-G "NMake Makefiles" ../ 
```

This will call CMake (on your *build* directory that is assumed to be under the repository root) specifying the location of the toolchain install, specifying ChibiOS v17.6.0 as the RTOS version, that the target board is named ST_NUCLEO_F091RC, that STM32F0xx is the series name that it belongs to, debugger feature is to be included, Windows.Devices.Gpio API is to be included and that the build files suitable for NMake are to be generated.

Another example:

```
cmake \
-DTOOLCHAIN_PREFIX="E:/GNU_Tools_ARM_Embedded/5_4_2016q3" \
-DCHIBIOS_SOURCE=E:/GitHub/ChibiOS \
-DCHIBIOS_BOARD=ST_NUCLEO144_F746ZG \
-DTARGET_SERIES=STM32F7xx \
-DUSE_FPU=TRUE \
-DNF_FEATURE_DEBUGGER=TRUE \
-DAPI_Windows.Devices.Gpio=ON \
-DNF_FEATURE_RTC=ON \
-G "NMake Makefiles" ../ 
```

This will call CMake (on your *build* directory that is assumed to be under the repository root) specifying the location of the toolchain install, specifying that ChibiOS sources to be used are located in the designated path (mind the forward slash and no ending slash),  that the target board is named ST_NUCLEO144_F746ZG, that STM32F7xx is the series name that it belongs to, hardware floating point unit is to be used, debugger feature is to be included, Windows.Devices.Gpio API is to be included, RTC is used and that the build files suitable for NMake are to be generated.

After successful completion you'll have the build files ready to be used in the target build tool.


## Building from VS Code (using CMake Tools extension)

We've added the required files and configurations to help you launch your build from VS Code.
Follows a brief explanation on the files you might want to tweak.

- settings.json (inside .vscode folder) here you can change the generator that CMake uses to generate the build. The default is ```"cmake.generator": "NMake Makefiles"```.
- launch.json (inside .vscode folder) here you can set up your launch configurations, such as gdb path or openocd configuration.
- cmake-variants.json (at the repository root) here you can add several build flavors. You can even add variants to each one. Check the documentation extension [here](https://github.com/vector-of-bool/vscode-cmake-tools/blob/develop/docs/build_variants.md).

To launch the build in VS Code check the status bar at the bottom. Select the build flavor and then click the build button (or hit F7).


# **nanoFramework** build deliverables

After a successful build you can find the **nanoFramework** image files in the *build* directory. Those are:

- nanoBooter image:
  - nanoBooter.bin (raw binary format)
  - nanoBooter.hex (Intel hex format)
  - nanoBooter.s19 (Motorola S-record format, equivalent to srec)
  - nanoBooter.lst (source code listing intermixed with disassembly)
  - nanoBooter.map (image map) 

- nanoCLR image:
  - nanoCLR.bin (raw binary format)
  - nanoCLR.hex (Intel hex format)
  - nanoCLR.s19 (Motorola S-record format, equivalent to srec)
  - nanoCLR.lst (source code listing intermixed with disassembly)
  - nanoCLR.map (image map)
