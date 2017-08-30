# CMake _toolchain file_ for STM32 with GNU ARM Embedded Toolchain

**About this document**

This document describes the CMake module that is loaded as a _toolchain file_ to support STM32 devices using the GNU ARM Embedded Toolchain.


# Purpose

The purpose of this CMake module is to configure CMake for cross-compiling an ARM Cortex image in the platform that is running (Windows, MAC or Linux) using the GNU ARM Embedded Toolchain.
In the process the parameters that were passed to CMake when invoking it are also validated.
The toolchain CMake module is located in the CMake directory, not in the Modules directory because CMake understands it as a _toolchain file_ not a module (despite being technically of the same kind).


# Workflow

Follows a brief description on the validations that are performed:
- Toolchain location
- Target chip. The support for STM32 devices is added for each series (F0, F4, etc). The target chip is validated against a list of the series that are supported.

The next part of the file takes care of configuring the GCC toolchain location, setup the working directories, C, C++ and assembly compilers, flags for the various build flavors (debug/release) and the targets that will eventually result from running the build.

An important part is the inclusion of a CMake module that is specific to the STM32 series of the target chip. This helps on keeping things separated and more manageable. The general aspects, configurations and definitions are kept in this toolchain file and the particulars of the target series remain in the series CMake module. The naming of the series module follows the structure "STM32**NN**_GCC_options.cmake" on which the **NN** are replaced with the series designation in upper case.
The series CMake module has to be placed in the CMake\Modules directory otherwise CMake won't be able to find it.
