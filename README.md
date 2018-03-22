[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0) [![#yourfirstpr](https://img.shields.io/badge/first--timers--only-friendly-blue.svg)](https://github.com/nanoframework/Home/blob/master/CONTRIBUTING.md) 
[![Average time to resolve an issue](http://isitmaintained.com/badge/resolution/nanoframework/home.svg)](http://isitmaintained.com/project/nanoframework/home "Average time to resolve an issue") [![Percentage of issues still open](http://isitmaintained.com/badge/open/nanoframework/home.svg)](http://isitmaintained.com/project/nanoframework/home "Percentage of issues still open")  


![nanoFramework logo](resources/logo/nanoFramework-repo-logo.png)

-----

# **nanoFramework** Home

This _Home_ repository is the starting point for developers that want to learn about **nanoFramework**, contribute to it or opening issues.
It contains links to the various GitHub repositories used by **nanoFramework**.

**nanoFramework** goal is to be a platform that enables the writing of managed code applications for constrained embedded devices. 
Developers can harness the familiar IDE Visual Studio and their .NET (C#) knowledge to quickly write applications without having to worry about the low level hardware intricacies of a micro-controller.

Being a developer you'll probably will fit in one (or maybe both :wink:) of the following _profiles_:
- Developer: if your goal is to develop C# applications for micro-controllers.
- Contributor: if you are interested in actively contributing by coding (native, managed, C, C++, CMake), writing documentation or participating in the overall project organization.


## Firmware for reference boards


Each of the following ZIP files contains the image files for nanoBooter and nanoCLR in various formats (HEX, BIN and DFU). They should be flashed in the target boards using an appropriate software utility.

The **stable** versions are RTM builds with the smallest possible size. They include the latest stable version. The debugging feature is disabled and only minimal (or none) error messages.

The **preview** versions are continuous builds of the reference targets. They include the latest version of all features and bug corrections. They also have the debugging feature enabled along with detailed error messages.


| Target | Stable | Preview |
|:-|---|---|
| ST_STM32F4_DISCOVERY | []() |  [![Download](https://api.bintray.com/packages/nfbot/nanoframework-images-dev/ST_STM32F4_DISCOVERY/images/download.svg)](https://bintray.com/nfbot/nanoframework-images-dev/ST_STM32F4_DISCOVERY/_latestVersion) |
| ST_STM32F429I_DISCOVERY | []() | [ ![Download](https://api.bintray.com/packages/nfbot/nanoframework-images-dev/ST_STM32F429I_DISCOVERY/images/download.svg) ](https://bintray.com/nfbot/nanoframework-images-dev/ST_STM32F429I_DISCOVERY/_latestVersion) |
| ST_NUCLEO64_F091RC | []() | [ ![Download](https://api.bintray.com/packages/nfbot/nanoframework-images-dev/ST_NUCLEO64_F091RC/images/download.svg) ](https://bintray.com/nfbot/nanoframework-images-dev/ST_NUCLEO64_F091RC/_latestVersion) |
| ST_NUCLEO144_F746ZG | []() | [ ![Download](https://api.bintray.com/packages/nfbot/nanoframework-images-dev/ST_NUCLEO144_F746ZG/images/download.svg) ](https://bintray.com/nfbot/nanoframework-images-dev/ST_NUCLEO144_F746ZG/_latestVersion) |
| ST_STM32F769I_DISCOVERY | []() | [ ![Download](https://api.bintray.com/packages/nfbot/nanoframework-images-dev/ST_STM32F769I_DISCOVERY/images/download.svg) ](https://bintray.com/nfbot/nanoframework-images-dev/ST_STM32F769I_DISCOVERY/_latestVersion) |
| MBN_QUAIL | []() | [ ![Download](https://api.bintray.com/packages/nfbot/nanoframework-images-dev/MBN_QUAIL/images/download.svg) ](https://bintray.com/nfbot/nanoframework-images-dev/MBN_QUAIL/_latestVersion) |
| NETDUINO3_WIFI | []() | [ ![Download](https://api.bintray.com/packages/nfbot/nanoframework-images-dev/NETDUINO3_WIFI/images/download.svg) ](https://bintray.com/nfbot/nanoframework-images-dev/NETDUINO3_WIFI/_latestVersion) |
| ESP32_DEVKITC | []() | [ ![Download](https://api.bintray.com/packages/nfbot/nanoframework-images-dev/ESP32_DEVKITC/images/download.svg) ](https://bintray.com/nfbot/nanoframework-images-dev/ESP32_DEVKITC/_latestVersion) |


The above firmware builds include support for the class libraries and features marked bellow.


| Target | Gpio | Spi | I2c | Pwm | Adc | Serial | Events | SWO | Networking |
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| ST_STM32F4_DISCOVERY | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark:  | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | |
| ST_STM32F429I_DISCOVERY | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | |
| ST_NUCLEO64_F091RC | | | | :heavy_check_mark: | | | | :heavy_check_mark: | |
| ST_NUCLEO144_F746ZG | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | |
| ST_STM32F769I_DISCOVERY | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | |
| MBN_QUAIL | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | | :heavy_check_mark: | :heavy_check_mark: | | | |
| NETDUINO3_WIFI | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | | :heavy_check_mark: | :heavy_check_mark: | | | |
| ESP32_DEVKITC | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | | :heavy_check_mark: | | | |


## Repositories

- [nf-interpreter](https://github.com/nanoframework/nf-interpreter) - this repo contains the **nanoFramework** CLR, interpreter, target boards configuration and the build system. This is where everything required to build an image to be flashed into a device lives.

- [nf-Community-Targets](https://github.com/nanoframework/nf-Community-Targets) - this repo contains target boards that are contributed by community members. You might find here _inspiration_ for your next board.

- [lib-CoreLibrary](https://github.com/nanoframework/lib-CoreLibrary) - this repo contains the Base Class Library (Core library - mscorlib) that is used in developing C# applications.

- [lib-nanoFramework.Runtime.Events](https://github.com/nanoframework/lib-nanoFramework.Runtime.Events) - this repo contains the nanoFramework.Runtime.Events library that is used in developing C# applications.

- [lib-nanoFramework.Runtime.Native](https://github.com/nanoframework/lib-nanoFramework.Runtime.Native) - this repo contains the nanoFramework.Runtime.Native library that is used in developing C# applications.

- [lib-Windows.Devices.Adc](https://github.com/nanoframework/lib-Windows.Devices.Adc) - this repo contains the Windows.Devices.Adc library that is used in developing C# applications.

- [lib-Windows.Devices.Gpio](https://github.com/nanoframework/lib-Windows.Devices.Gpio) - this repo contains the Windows.Devices.Gpio library that is used in developing C# applications.

- [lib-Windows.Devices.I2c](https://github.com/nanoframework/lib-Windows.Devices.I2c) - this repo contains the Windows.Devices.I2c library that is used in developing C# applications.

- [lib-Windows.Devices.Pwm](https://github.com/nanoframework/lib-Windows.Devices.Pwm) - this repo contains the Windows.Devices.Pwm library that is used in developing C# applications.

- [lib-Windows.Devices.SerialCommunication](https://github.com/nanoframework/lib-Windows.Devices.SerialCommunication) - this repo contains the Windows.Devices.SerialCommunication library that is used in developing C# applications.

- [lib-Windows.Devices.Spi](https://github.com/nanoframework/lib-Windows.Devices.Spi) - this repo contains the Windows.Devices.Spi library that is used in developing C# applications.

- [lib-Windows.Networking.Sockets](https://github.com/nanoframework/lib-Windows.Networking.Sockets) - this repo contains the Windows.Networking.Sockets library that is used in developing C# applications that require networking capabilities.

- [lib-Windows.Storage.Streams](https://github.com/nanoframework/lib-Windows.Storage.Streams) - this repo contains the Windows.Storage.Streams library that is used in developing C# applications.

- [nf-Visual-Studio-extension](https://github.com/nanoframework/nf-Visual-Studio-extension) - this repo contains the Visual Studio extension and all the associated tools required to compile and build a **nanoFramework** managed application ready to deploy to a target device.

- [nf-debugger](https://github.com/nanoframework/nf-debugger) - this repo contains the debugger library (in several technologies) allowing reuse of the low lower library by third party applications.

- [nf-ANT](https://github.com/nanoframework/nf-ANT) - this repo contains an UWP application that connects to a **nanoFramework** target and can provide basic information about it along with some basic management operations. The development of this tool has been put on a halt because its features and capabilities are now available in Visual Studio through the Device Manager window.

- [ChibiOS](https://github.com/nanoframework/ChibiOS) - this repo contains a mirror of the official ChibiOS SVN repository. It's used as the default source for building **nanoFramework** images.

- [nf-tools](https://github.com/nanoframework/nf-tools) - this repo contains various tools that are required in **nanoFramework** development, usage or repository management.

- [nanoframework.github.io ](https://github.com/nanoframework/nanoframework.github.io) - this repo contains the sources and configuration files to generate the **nanoFramework** documentation web site. Any static content, such as articles, guides, how-to's and such is to be checked-in here.


## How to Engage, Contribute and Provide Feedback

Some of the best ways to contribute are to try things out, file bugs, and join in design conversations. 
If you are having issues or need a clarification about something, instead of opening an issue the best way is to start a conversation in one of our [Slack](https://nanoframework.slack.com) channels.
Please select the one that's most appropriate to the matter you are facing.

If you've find a bug or can't use Slack, please open an issue at [Issues](https://github.com/nanoframework/Home/issues).
We ask you to open an issue only when you have a real and confirmed one. Don't open an issue for support requests or to start a discussion. For that you'll get a better (and quicker!) support/feedback in one of the [Slack](https://nanoframework.slack.com) channels. You can request an invitation for the Slack workspace in [this form](https://nanoframework.net/slack-invite-form/).

Looking for something to work on? Check the list of [up-for-grabs issues](https://github.com/nanoframework/Home/issues?q=is%3Aissue+is%3Aopen+label%3Aup-for-grabs) on the Home repo, that's a great place to start.

See some of our guides for more details:

* [Contributing Guide](CONTRIBUTING.md)
* [Developer Guide](docs/contributing/developer-guide.md)


## Documentation

### [Docs](docs/)

The project documentation is a great place to find information about **nanoFramework**, no matter if you are newcomer or a veteran. It's organized in the following categories:
- [API reference](http://docs.nanoframework.net/api) documentation for the various class libraries.
- [Developing C# applications](docs/developing-apps) using **nanoFramework**.
- [Building an image](docs/building) to load on a target board.
- [**nanoFramework** architecture](docs/architecture/) and how the different pieces fit together.
- [Contributing to **nanoFramework**](docs/contributing/) includes an overview on how you can contribute to the project. 


### [Blog](http://www.nanoframework.net/blog)

There is a blog where we try to post detailed updates about the development status, technical posts about a particular feature ou a design option.


## Who is behind this project?

There are a number of people behind this project. We are mostly embedded systems enthusiasts, passionate about coding and people that like challenges. 
All of us have our daily jobs and we work on this project in our free time.
That is to say that you can always expect an answer from us. Maybe not instantly but in a - hopefully - timely fashion :wink: !


## Code of Conduct
This project has adopted the code of conduct defined by the [Contributor Covenant](http://contributor-covenant.org/)
to clarify expected behavior in our community.
