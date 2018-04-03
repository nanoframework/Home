# External memory

**About this document**

This document describes how to use external memory for the managed heap using the ChibiOS FSMC driver from the **nanoFramework** overlay.
Please refer to the CLR managed heap [documentation](clr-managed-heap.md).


## Memory controller

Most STM32 devices include a FSMC (Flexible Static Memory Controller) that provides seamless interface with the most common memory types either synchronous or asynchronous.


## Assumptions and design

The initialization of the memory controller along with the memory configuration have to occur as early as possible after the boot. In the current **nanoFramework** design this is expected to occur right after the call to CMSIS `osKernelInitialize()` when all other initialization and configurations have already happen and interrupts are enabled. Because the memory space is to be used as the managed heap the timing is no more critical than that, so pretty much anywhere before the call to the CLR startup should be quite alright.


The function were the external memory configuration and initialization is to occur is `Target_ExternalMemoryInit()`. The `nanoHAL_v2.h` provides a _weak_ and empty implementation of this function. If a target is to use external memory it has to provide the _strong_ implementation of this function and call it before `ClrStartup()` is called.

Considering that the default placement of the CLR managed is in the SoC internal RAM, the linker file includes a rule to place this region (called `clr_managed_heap`) in one of its RAM regions.


# Example for STM32F429I-Discovery reference target

To provide a working example of this configuration we are taking the STM32F429I-Discovery reference target that is in the nf-interpreter repository [here](https://github.com/nanoframework/nf-interpreter/tree/develop/targets/CMSIS-OS/ChibiOS/ST_STM32F429I_DISCOVERY).
This targets board has a 64Mbit SDRAM (the chip is the IS42S16400J).


1. The _target_ implementation is provided in the `target_external_memory.c` file that is located in the target base folder. This location allows the function to be reused by nanoCLR and nanoBooter, if desired. Plus, it's included in the compile sequence at a time that the target CPU and other required definitions are already set.
In order to include this code file in the build it has to be included as source file the target definition. For our example this is in the arguments of `add_executable` for nanoCLR.

2. Next we have to set the `__crt_heap_size__` symbol to 0 so the managed heap is not placed in the SoC RAM. This is done by setting it to 0 in the target CMakelist.txt like this `--defsym=__crt_heap_size__=0x0`.
