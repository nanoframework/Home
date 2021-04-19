# .NET **nanoFramework** GitHub organization

Our GitHub organization holds the various repositories for firmware, class libraries, documentation and tools.
Follows a list and description of the repositories under .NET **nanoFramework** organization.

## Repositories

### Samples and documentation

- [Samples](https://github.com/nanoframework/Samples) - this repo contains sample applications illustrating .NET **nanoFramework** APIs and common use cases.
- [nanoframework.github.io](https://github.com/nanoframework/nanoframework.github.io) - this repo contains the sources and configuration files to generate the .NET **nanoFramework** documentation web site. Any static content, such as articles, guides, how-to's and such is to be checked-in here.

### Targets, interpreter, native C

- [nf-interpreter](https://github.com/nanoframework/nf-interpreter) - this repo contains the .NET **nanoFramework** CLR, interpreter, target boards configuration and the build system. This is where everything required to build an image to be flashed into a device lives.
- [nf-Community-Targets](https://github.com/nanoframework/nf-Community-Targets) - this repo contains target boards that are contributed by community members. You might find here _inspiration_ for your next board.
- [nf-Community-Contributions](https://github.com/nanoframework/nf-Community-Contributions) - this repo contains contributions from community members. Drivers, extensions, utilities, feature demos...

### Traditional System libraries

- [CoreLibrary](https://github.com/nanoframework/CoreLibrary) - this repo contains the Base Class Library (Core library - mscorlib) that is used in developing C# applications.
- [nanoFramework.System.Net](https://github.com/nanoframework/nanoFramework.System.Net) - this repo contains the nanoFramework.System.Net library that is used in developing C# applications with networking capabilities.
- [nanoFramework.System.Net.Http](https://github.com/nanoframework/nanoFramework.System.Net.Http) - this repo contains nanoFramework System.Net.Http class library.
- [System.Net](https://github.com/nanoframework/System.Net) - this repo contains the System.Net library that is the foundation for networking in .NET **nanoFramework**.
- [System.IO.FileSystem](https://github.com/nanoframework/System.IO.FileSystem) - this repo contains System.IO.Stream and other related classes.
- [nanoFramework.System.Text](https://github.com/nanoframework/nanoFramework.System.Text) - this repo contains nanoFramework System.Text Class Library offering advance Text manipulation.
- [nanoFramework.System.Text.RegularExpressions](https://github.com/nanoframework/nanoFramework.System.Text.RegularExpressions) - this repo contains nanoFramework System.Text.RegularExpressions Class Library.
- [nanoFramework.System.Math](https://github.com/nanoframework/nanoFramework.System.Math) - this repo contains nanoFramework System.Math Class Library.
- [nanoFramework.System.Collections](https://github.com/nanoframework/nanoFramework.System.Collections) - this repo contains nanoFramework System.Collections Class Library.
- [nanoFramework.System.Threading](https://github.com/nanoframework/nanoFramework.System.Threading) - this repo contains nanoFramework System.Threading class library.
- [nanoFramework.ResourceManager](https://github.com/nanoframework/nanoFramework.ResourceManager) - this repo contains what's needed to add resources in any .NET nanoFramework project. It's important to use this specific package to add resource support.

### System.Device and Windows.Devices Libraries

Note: work to migrate `Windows.*` namespaces to `System.*` is in process, see [this issue](https://github.com/nanoframework/Home/issues/620).

- [System.Devices.Dac](https://github.com/nanoframework/System.Devices.Dac) - this repo contains the nanoFramework.System.Devices.Dac library that is used in developing C# applications that require DAC (Digital Analog Converter) capabilities.
- [Windows.Devices.Adc](https://github.com/nanoframework/Windows.Devices.Adc) - this repo contains the Windows.Devices.Adc library that is used in developing C# applications.
- [System.Device.Gpio](https://github.com/nanoframework/System.Device.Gpio) - this repo contains the System.Device.Gpio library that is used in developing C# applications, this replaces Windows.Devices.Gpio.
- Deprecated: [Windows.Devices.Gpio](https://github.com/nanoframework/Windows.Devices.Gpio) - this repo contains the Windows.Devices.Gpio library that is used in developing C# applications.
- [System.Device.I2c](https://github.com/nanoframework/System.Device.I2c) - this repo contains the Windows.Devices.I2c library that is used in developing C# applications, this replaces Windows.Devices.I2c.
- Deprecated: [Windows.Devices.I2c](https://github.com/nanoframework/Windows.Devices.I2c) - this repo contains the Windows.Devices.I2c library that is used in developing C# applications.
- [Windows.Devices.Pwm](https://github.com/nanoframework/Windows.Devices.Pwm) - this repo contains the Windows.Devices.Pwm library that is used in developing C# applications.
- [Windows.Devices.SerialCommunication](https://github.com/nanoframework/Windows.Devices.SerialCommunication) - this repo contains the Windows.Devices.SerialCommunication library that is used in developing C# applications.
- [Windows.Devices.Spi](https://github.com/nanoframework/Windows.Devices.Spi) - this repo contains the Windows.Devices.Spi library that is used in developing C# applications.
- [Windows.Devices.WiFi](https://github.com/nanoframework/Windows.Devices.WiFi) - this repo contains the Windows.Devices.WiFi library that is used in developing C# applications.
- [Windows.Networking.Sockets](https://github.com/nanoframework/Windows.Networking.Sockets) - this repo contains the Windows.Networking.Sockets library that is used in developing C# applications that require networking capabilities.
- [Windows.Storage](https://github.com/nanoframework/Windows.Storage) - this repo contains the Windows.Storage library that is used in developing C# applications.
- [Windows.Storage.Streams](https://github.com/nanoframework/Windows.Storage.Streams) - this repo contains the Windows.Storage.Streams library that is used in developing C# applications.
- [nanoFramework.Devices.Can](https://github.com/nanoframework/nanoFramework.Devices.Can) - this repo contains nanoFramework.Devices.Can Class Library.
- [nanoFramework.Devices.OneWire](https://github.com/nanoframework/nanoFramework.Devices.OneWire) - this repo contains nanoFramework 1-Wire Class Library

### Additional nanoFramework libraries

- [nanoFramework.Json](https://github.com/nanoframework/nanoFramework.Json)  - this repo contains a Json Serializer and Deserializer Library for nanoFramework, replaces Json.NetMF.
- Deprecated: [Json.NetMF](https://github.com/nanoframework/Json.NetMF) - this repo contains a Json Serializer and Deserializer Library for nanoFramework and .NET Micro Framework.
- [nanoFramework.TestFramework](https://github.com/nanoframework/nanoFramework.TestFramework) - this repo contains nanoFramework Unit Test platform. It brings an integrated experience for unit testing nanoFramework including on a device fully integrated with Visual Studio 2019.
- [nanoFramework.Graphics](https://github.com/nanoframework/nanoFramework.Graphics) - this repo contains nanoFramework.Graphics class library to allow using graphics on screens.
- [nanoFramework.Networking.Sntp](https://github.com/nanoframework/nanoFramework.Networking.Sntp) - this repo contains the nanoFramework.Networking.Sntp library that is used in developing C# applications.
- [nanoFramework.WebServer](https://github.com/nanoframework/nanoFramework.WebServer) - this repo contains Web server for nanoFramework packed with features: REST api using attributes, multithread requests, parameters in query URL, static files serving.
- [nanoFramework.Logging](https://github.com/nanoframework/nanoFramework.Logging) - this repo contains a logging library for .NET nanoFramework compatible with Microsoft.Extensions.Logging. It does include Debug, Serial and Stream logging.
- [amqpnetlite](https://github.com/nanoframework/amqpnetlite) - this repo contains a forked from Azure/amqpnetlite repo and modifications to support nanoFramework offering an AMQP 1.0 .NET Library support.
- [paho.mqtt.m2mqtt](https://github.com/nanoframework/paho.mqtt.m2mqtt) - this repo contains a forked from eclipse/paho.mqtt.m2mqtt repo and modifications to support nanoFramework offering a MQTT Class Library support.

### Hardware specific libraries

- [nanoFramework.Hardware.Esp32](https://github.com/nanoframework/nanoFramework.Hardware.Esp32) - this repo contains the nanoFramework.Hardware.Esp32 library that is used in developing C# applications for ESP32.
- [nanoFramework.Hardware.Esp32.Rmt](https://github.com/nanoframework/nanoFramework.Hardware.Esp32.Rmt) - this repo contains the nanoFramework class library for the RMT (remote control) peripheral for the ESP32 target.
- [nanoFramework.Hardware.TI](https://github.com/nanoframework/nanoFramework.Hardware.TI) - this repo contains nanoFramework TI SimpleLink Hardware Class Library.
- [nanoFramework.TI.EasyLink](https://github.com/nanoframework/nanoFramework.TI.EasyLink) - this repo contains nanoFramework TI EasyLink Hardware Class Library.
- [nanoFramework.Hardware.Stm32](https://github.com/nanoframework/nanoFramework.Hardware.Stm32) - this repo contains nanoFramework STM32 Hardware Class Library.
- [nanoFramework.Runtime.Events](https://github.com/nanoframework/nanoFramework.Runtime.Events) - this repo contains the nanoFramework.Runtime.Events library that is used in developing C# applications.
- [nanoFramework.Runtime.Native](https://github.com/nanoframework/nanoFramework.Runtime.Native) - this repo contains the nanoFramework.Runtime.Native library that is used in developing C# applications.
- [nanoFramework.M5Stack](https://github.com/nanoframework/nanoFramework.M5Stack) - this repo contains support for the M5Stack hardware especially native elements for the screen.

### Tools

- [nf-Visual-Studio-extension](https://github.com/nanoframework/nf-Visual-Studio-extension) - this repo contains the Visual Studio extension and all the associated tools required to compile and build a .NET **nanoFramework** managed application ready to deploy to a target device.
- [nf-debugger](https://github.com/nanoframework/nf-debugger) - this repo contains the debugger library (in several technologies) allowing reuse of the low lower library by third party applications.
- [nf-tools](https://github.com/nanoframework/nf-tools) - this repo contains various tools that are required in .NET **nanoFramework** development, usage or repository management.
- [metadata-processor](https://github.com/nanoframework/metadata-processor) - this repo contains the Meta Data Processor that is used when building C# nanoFramework applications. It's main function is to parse the outputs from Roslyn and build proprietary PE files that will be loaded into the nanoFramework target devices.
- [nanoFirmwareFlasher](https://github.com/nanoframework/nanoFirmwareFlasher) - this repo contains the nanoFramework Firmware Flasher that is used to update the firmware on nanoFramework target devices. Along with other flash utilities that are useful in production and on the daily use.
- [hex2dfu](https://github.com/nanoframework/hex2dfu) - this repo contains the hex2dfu utility that is used to pack binary files in DFU files required to update some STM32 chips.
- [nFBot](https://github.com/nanoframework/nFBot) - this repo contains our lovely and chatty bot for issues, PR on all nanoFramework repos and posting on our Discord server.
- [Home](https://github.com/nanoframework/Home) - The landing page for nanoFramework repositories.

### RTOS clone repositories

- [ChibiOS](https://github.com/nanoframework/ChibiOS) - this repo contains a mirror of the official ChibiOS SVN repository. It's used as the default source for building .NET **nanoFramework** images.
- [ChibiOS-Contrib](https://github.com/nanoframework/ChibiOS-Contrib) - this repo contains a forked from ChibiOS/ChibiOS-Contrib. Community contributed code (ports, drivers, etc).
- [mbedtls](https://github.com/nanoframework/mbedtls) - this repo contains a mirror of the official mbedtls repository. It's used as the default source for building .NET **nanoFramework** images implementing TLS for networking.
- [TI_XDCTools](https://github.com/nanoframework/TI_XDCTools) - this repo contains Texas Instruments XDCTools (this is NOT an official repository of the tools).
- [STM32CubeL4](https://github.com/nanoframework/STM32CubeL4) - this repo contains a forked from STMicroelectronics/STM32CubeL4. STM32Cube MCU Full Package for the STM32L4 series - (HAL + LL Drivers, CMSIS Core, CMSIS Device, MW libraries plus a set of Projects running on all boards provided by ST (Nucleo, Evaluation and Discovery Kits)).
- [STM32CubeH7](https://github.com/nanoframework/STM32CubeH7) - this repo contains a forked from STMicroelectronics/STM32CubeH7. STM32Cube MCU Full Package for the STM32H7 series - (HAL + LL Drivers, CMSIS Core, CMSIS Device, MW libraries plus a set of Projects running on all boards provided by ST (Nucleo, Evaluation and Discovery Kits)).
- [STM32CubeF4](https://github.com/nanoframework/STM32CubeF4) - this repo contains a forked from STMicroelectronics/STM32CubeF4. STM32Cube MCU Full Package for the STM32F4 series - (HAL + LL Drivers, CMSIS Core, CMSIS Device, MW libraries plus a set of Projects running on all boards provided by ST (Nucleo, Evaluation and Discovery Kits)).
- [STM32CubeF7](https://github.com/nanoframework/STM32CubeF7) - this repo contains a forked from STMicroelectronics/STM32CubeF7. STM32Cube MCU Full Package for the STM32F7 series - (HAL + LL Drivers, CMSIS Core, CMSIS Device, MW libraries plus a set of Projects running on all boards provided by ST (Nucleo, Evaluation and Discovery Kits)).
- [STM32CubeF0](https://github.com/nanoframework/STM32CubeF0) - this repo contains a forked from STMicroelectronics/STM32CubeF0. STM32Cube MCU Full Package for the STM32F0 series - (HAL + LL Drivers, CMSIS Core, CMSIS Device, MW libraries plus a set of Projects running on all boards provided by ST (Nucleo, Evaluation and Discovery Kits)).
- [STM32CubeL0](https://github.com/nanoframework/STM32CubeL0) - this repo contains a forked from STMicroelectronics/STM32CubeL0. STM32Cube MCU Full Package for the STM32L0 series - (HAL + LL Drivers, CMSIS Core, CMSIS Device, MW libraries plus a set of Projects running on all boards provided by ST (Nucleo, Evaluation and Discovery Kits)).
- [TI_SysConfig](https://github.com/nanoframework/TI_SysConfig) - this repo contains Texas Instruments SysConfig tool (this is NOT an official repository of the tool).
- [SimpleLink_CC13x2_26x2_SDK](https://github.com/nanoframework/SimpleLink_CC13x2_26x2_SDK) - this repo contains Texas Instruments SimpleLink™ CC13x2 and CC26x2 (this is NOT the official repository).
- [SimpleLink_CC32xx_SDK](https://github.com/nanoframework/SimpleLink_CC32xx_SDK). - this repo contains source files for TI SimpleLink CC32xx SDK (this is NOT the official repository).
