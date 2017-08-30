# GCC linker script for ChibiOS boards

**About this document**

This document describes the GCC linker script for **nanoFramework** boards using ChibiOS HAL/PAL and some explanations on how to customize and adapt it to a new target board.


## Linker script file naming

To make it very clear on what file belongs to what image, the linker script files names carry a suffix of '_booter' for the nanoBooter and '_CLR' for the nanoCLR.

These linker scripts are used by the linker at the link stage and are added to the build on the CMakeLists.txt global to a target board.

When adding a new target board make sure that you set each linker script file to the appropriate target (in CMake, that is).

It's also recommended that each linker script file is located in the respective nanoBooter or nanoCLR folder (these being inside a target board folder, that is).


## Configurations for nanoBooter link script

The nanoBooter image is located at the default boot address of the target Soc/MCU.

It's recommended that that the region length is set to match the FLASH space reserved for the nanoBooter. This adds an extra check because when the build and link occurs, if the image is too large to fit that space an error is generated and corrective actions can be taken.

To illustrate this we are going to look into the linker script for the ST_NUCLEO_F091RC board. This is file [STM32F091xC_booter.ld](../../targets/CMSIS-OS/ChibiOS/ST_NUCLEO_F091RC/nanoBooter/STM32F091xC_booter.ld).


The only configuration here is the length of the `flash` region that should be set to the FLASH space reserved for the nanoBooter. In the example it can be seen that the nanoBooter image will start at address 0x08000000, with a maximum size of 16K.


## Configurations for nanoCLR link script

The nanoCLR image is located at the designated address of the available FLASH space, typically right after the space reserved for the nanoBooter.

It's recommended that that the region length is set to match the FLASH space reserved for the nanoCLR. This adds an extra check because when the build and link occurs, if the image is too large to fit that space an error is generated and corrective actions can be taken.

To illustrate this we are going to look into the linker script for the ST_NUCLEO_F091RC board. This is file [STM32F091xC_CLR.ld](../../targets/CMSIS-OS/ChibiOS/ST_NUCLEO_F091RC/nanoCLR/STM32F091xC_CLR.ld).


The `flash` region configuration depends on two factors: the space reserved for nanoBooter image and the space reserved for application deployment.
In the example it can be seen that nanoCLR image will start at address 0x08004000 and has a maximum size of 256k - 16k - 100k. That's the size reserved for nanoBooter and the size reserved for the application deployment.

On this particular example (because this SoC requires that the vector table is copied to RAM) the `ram0` region needs to be tweaked so it starts after the space reserved for the vector table. The end result is `ram0` starting at 0x200000C0 with a length of 32k - 0xC0.


### Tips

- When designing the address map make sure that the address region boundaries **match the FLASH memory blocks**. This is very important in order to be able to perform image updates. This is valid for nanoBooter, nanoCLR and application deployment.

- The link script accepts several number format. Use the one that is convenient for what you are specifying. 
Follow some examples. For an absolute address (such as the start of a FLASH block) use the hexadecimal notation like in 0x08000000. When specifying the size of a region use the _k_ and _M_ suffixes, like 16k for a block with 16k Bytes (4096 bytes), or 1M. This makes it much easier to copy/paste from the device data sheet.

- It's OK to use mathematical expressions. For example, when setting the available space for the nanoCLR image don't bother with doing the math, just put there 1M - 16k.
