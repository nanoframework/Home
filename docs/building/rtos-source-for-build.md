## Building **nanoFramework** with local RTOS source vs RTOS source from repository


When building **nanoFramework** for a CMSIS target (currently only ChibiOS is supported) the developer has two options: either using a local path for the RTOS source code or downloading it from the official repository.
This document aims to give you an brief overview of the differences between these two so you can choose the option that best fits your use scenario.




### Source from official repository

When running CMake, if the parameter `-DCHIBIOS_SOURCE` is not not specified CMake will connect to **nanoFrameworks** [ChibiOS mirror](https://github.com/nanoframework/ChibiOS) on GitHub and will clone the source from there. The time for this operation to complete will mostly depend on the speed of your internet connection. Note that you have the option to specify the `-CHIBIOS_VERSION` (e.g. `17.6.2`) if you would like to target a specific release else the latest code from the 'stable_17.6.x' branch will be checked out instead.

ChibiOS will be cached within the build directory so the full download won't happen again unless the build directory is cleared. A check for any changes in the repo is made whenever a build is run. If there are any, the changes will be downloaded and merged.

This option is good for automated builds or when you don't have (or don't want) the repo cloned to your local storage device.

Another advantage is that you don't have to manage the updates to the local clone yourself.

An obvious disadvantage is that if the build folder is cleaned (required when switching between target boards) the 'cached' repo will be gone and a full download will occur when the project is next built.




### Source from local clone

When running CMake, if the parameter `-DCHIBIOS_SOURCE="....."` is specified a local clone located at the designated path will be used when the build occurs. When using this option the `-CHIBIOS_VERSION` is not taken into account.
The only time penalty is the one necessary for CMake to copy the contents of the local ChibiOs repo to the build cache folder. This is a one time operation and it won't happen again unless the build folder is cleaned up.

This option is good when you have a local clone of the repo and you don't want to increase the build time with checks on the repo and downloading it or wish to target a different branch (such as `master`).

The downside is that you have to manage the update process for the ChibiOs repo yourself.

Another important aspect to consider is the branch **to _manually_ checkout**. Not doing this is synonym of using the 'master' branch that contains the development files and is not a stable version, which is probably not what you want to use.

Also here, if the build folder is cleaned the 'cached' repo will be gone.
