# Class Libraries 

**About this document**

This document describes the design and organization of **nanoFramework** Class Libraries, offers some explanation on the choices that were made and how to add a new Class Library. The examples bellow are related with ChibiOS (which is the currently reference implementation for **nanoFramework**).


## Libraries


Follow the list of the existing libraries, respective Nuget package and CMake enable option:

| Class Library | Nuget package name | CMake option |
| --- | --- | --- |
| Base Class Library (also know as mscorlib) | nanoFramework.CoreLibrary | (always included) |
| Windows.Device.Gpio | nanoFramework.Windows.Devices.Gpio | -DAPI_Windows.Devices.Gpio=ON |
| Windows.Device.Spi | nanoFramework.Windows.Devices.Spi | -DAPI_Windows.Devices.Spi=ON |


## Distribution strategy

To ease the burden of distributing and updating the class libraries we've choose to use Nuget to handle all this. It has the added benefit of dealing with the dependency management, version and such.

So, for each class library, there is a Nuget package that includes the assembly and documentation files. The Nuget package takes care of making sure that the required dependency(ies) and correct version(s) are added to a managed (C#) project, making a developer's life much easier.


## How to add a new class library

Follows the procedure to add a new class library to a **nanoFramework** target image. 

The example is for adding Windows.Devices.Gpio library.


1. In VS2017 start a new project for a **nanoFramework** C# Class library. Source code [here](https://github.com/nanoframework/lib-Windows.Devices.Gpio)

2. Implement all the required methods, enums, properties in that project. It's recommended that you add XML comments there (and enable the automated documentation generation in the project properties).

3. Add the Nuget packaging project to distribute the managed assembly and documentation. We have a second Nuget package that includes all the build artifacts, generated stubs, dump files and such. This is to be used in automated testing and distribution of followup projects or build steps. 

4. Upon a successfully build of the managed project the skeleton with the stubs should be available in the respective folder. Because **nanoFramework** aims to be target independent the native implementation of a class library will live 'inside' each target RTOS folder.
The next step would be to copy the stubs to a folder with the assembly name inside the nanoCLR folder. For our example: [Windows.Devices.Gpio](https://github.com/nanoframework/nf-interpreter/tree/develop/targets/CMSIS-OS/ChibiOS/nanoCLR/Windows.Devices.Gpio).

5. Add the CMake as a module to the modules folder [here](https://github.com/nanoframework/nf-interpreter/tree/develop/CMake/Modules). The name of the module should follow the assembly name (Find**Windows.Devices.Gpio**.cmake). Mind the CMake rules for the naming: start with _Find_ followed by the module name and _cmake_ extension. The CMake for the Windows.Devices.Gpio module is [here](https://github.com/nanoframework/nf-interpreter/blob/develop/CMake/Modules/FindWindows.Devices.Gpio.cmake).

6. In the CMake [NF_API_Namespaces.cmake](https://github.com/nanoframework/nf-interpreter/blob/develop/CMake/Modules/NF_API_Namespaces.cmake) add an option for the API. The option name must follow the pattern API_**namespace**. The option for Windows.Devices.Gpio is API_Windows.Devices.Gpio.

7. In the CMake [NF_API_Namespaces.cmake](https://github.com/nanoframework/nf-interpreter/blob/develop/CMake/Modules/NF_API_Namespaces.cmake) find the macro `ParseApiOptions` and add a block for the API. Just copy/paste an existing one and replace the namespace with the one that you are adding.

8. Update the template file for the CMake variants [here](https://github.com/nanoframework/nf-interpreter/blob/develop/cmake-variants.TEMPLATE.json) to include the respective option. For the Windows.Devices.Gpio example you would add to the _OPTION1..._ and _OPTION2..._ (under _linkage_) the following line: "API_Windows.Devices.Gpio" : "OFF"

9. If the API requires enabling hardware or SoC peripherals in the target HAL/PAL make the required changes to the appropriate files. 
For Windows.Devices.Gpio in ChibiOS there is nothing to enable because the GPIO subsystem is always enabled.
In contrast, for the Windows.Devices.Spi, the SPI subsystem has to be enabled at the _halconf.h_ file and also (at driver level) in _mcuconf.h_ the SPI peripherals have to be individually enabled (e.g. `#define STM32_SPI_USE_SPI1 TRUE`).

To ease the overall configuration of an API and related hardware (and when it makes sense) the API option (API_Windows.Devices.Gpio) can be _extended_ to automatically enable the HAL subsystem. This happens with the Windows.Devices.Spi API. The CMake option is mirrored in the general [CMakeLists.txt](https://github.com/nanoframework/nf-interpreter/blob/develop/CMakeLists.txt) in order to be used in CMakes and headers. This mirror property is `HAL_USE_SPI_OPTION`. It's being defined here and not in the individual _halconf.h_ files as usual. To make this work the CMake property has to be added to the CMake template file of the platform [target_platform.h.in](https://github.com/nanoframework/nf-interpreter/blob/develop/targets/CMSIS-OS/ChibiOS/nanoCLR/target_platform.h.in).

10. When adding/enabling new APIs and depending on how the drivers and the library are coded, some static variables will be added to the BSS RAM area. Because of that extra space that is taken by those variables the Managed Heap size may have to be adjusted to make room for those. To do this find the `__clr_managed_heap_size__` in the general CMakeLists.txt of that target and decrease the value there as required.

11. Some APIs depend of others. This happens for example with Windows.Devices.Gpio that requires nanoFramework.Runtime.Events in order to generate the interrupts for the changed pin values. To make this happen the option to include the required API(s) has to be enabled in the main [CMakeLists.txt](https://github.com/nanoframework/nf-interpreter/blob/develop/CMakeLists.txt) inside the if clause of the dependent API. Just like if the option was enabled at the CMake command line. Check this by searching for `API_nanoFramework.Runtime.Events` inside the `if(API_Windows.Devices.Gpio)`.

## How to include a class library in the build

To include a class library in the build for a target image you have to add to the CMake an option for the API. For the Windows.Devices.Gpio example the option would be `-DAPI_Windows.Devices.Gpio=ON`.
You can also add this to your own cmake-variants.json file.
To exclude a class library just set the option to OFF or simply don't include it in the command.
