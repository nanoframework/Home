# CMake _toolchain file_ for ChibiOS with GNU ARM Embedded Toolchain

**About this document**

This document describes the CMake module that is loaded as a _toolchain file_ to support mbed OS target using the GNU ARM Embedded Toolchain.


# Purpose

The purpose of this CMake module is to configure CMake for cross-compiling an ARM Cortex image in the platform that is running (Windows, MAC or Linux) using the GNU ARM Embedded Toolchain.
In the process the parameters that were passed to CMake when invoking it are also validated.
The toolchain CMake module is located in the CMake directory, not in the Modules directory because CMake understands it as a _toolchain file_ not a module (despite being technically of the same kind).


# Workflow

Follows a brief description on the validations that are performed:
- Toolchain location

The next part of the file takes care of configuring the GCC toolchain location, setup the working directories, C, C++ and assembly compilers, flags for the various build flavors (debug/release) and the targets that will eventually result from running the build.

The general aspects, configurations and definitions are kept in this toolchain file and the particulars of the target series remain in the series CMake module. 
