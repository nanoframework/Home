
## Building **nanoFramework** with local RTOS source vs RTOS source from repository


When building **nanoFramework** for a CMSIS target (currently only ChibiOS is supported) the developer has two options: either using a local path for the RTOS source code or downloading it from the official repository.
This document aims to give you an brief overview of the differences between these two so you can choose the option that best fits your use scenario.




### Source from official repository

When running CMake if the parameter `-DCHIBIOS_SOURCE` is not not specified what happens is that Cake will connect to [ChibiOS repo](https://github.com/nanoframework/ChibiOS) on GitHub and will download it from there. The time for this operation to complete will depend mostly on the speed of the Internet connection. Note that you can specify `-CHIBIOS_VERSION` too otherwise the latest code from the 'stable_17.6.x' branch will be checked out instead.

ChibiOS will be cached in the build directory so the full download won't happen again unless the build directory is cleared. A check for any changes in the repo is made whenever a build is run. If there are any, the changes will be downloaded and merged.

This option is good for automated builds or when you don't have (or don't want) the repo cloned to your local disk.

Another advantage is that you don't have to manage the updates on the local clone.

An obvious disadvantage is that if the build folder is cleaned the 'cached' repo will be gone.




### Source from local clone

When running CMake, if the parameter `-DCHIBIOS_SOURCE="....."` is specified a local clone located at the designated path will be used in the build. When using this option the `-CHIBIOS_VERSION` is not taken into account.
The only time penalty is the one necessary for CMake to copy the contents of the repo to the build cache folder. This is a one time operation and it won't happen again unless the build folder is cleaned up.

This option is good when you have a local clone of the repo and you don't want to increase the build time with checks on the repo and downloading it.

The downside is that you have to manage the updates from the repo yourself.

Another important aspect to consider is that you **have to _manually_ checkout** the branch that you want to use in the build. This is because CMake can't checkout branches for you.
Not doing this is synonym of using the 'master' branch that contains the development files and not a stable version, which is probably what you want to use.

Also here, if the build folder is cleaned the 'cached' repo will be gone.
