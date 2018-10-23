# Tweaking cmake-variants.TEMPLATE.json

### Table of contents ##

- [What is it](#what-is-it)
- [How to use it](#how-to-use-it)
- [Brief description](#brief-description)
- [Content explained](#content-explained)
- [Working example](#working-example)
- [Templates](#templates)

**About this document**

This document describes how to use and modify the **cmake-variants.TEMPLATE.json** file to suit your needs.

_Note : the current revision of the document only focuses on using ChibiOS RTOS. Other RTOSes will follow in a future revision._

## What is it

cmake-variants.TEMPLATE.json is a template containing a minimal set of configuration examples needed to build nanoFramework for you board.

Its content describes what kind of build you will get, which toolchain(s) you will use, which type of MCU is on the board, and some other options that will be described later in this document.

## How to use it

First, you have to either rename the file or copy the contents to **cmake-variants.json**. Then, you will have to modify the content to match your environment.


## Brief description

There are two sets of parameters that need to be present in this file :
- the build type : 'debug' or 'release', for example
- the board's environment : MCU, toolchain, RTOS

You should not have to modify the *BuildType* section unless you have good reasons to do so. However, the *Linkage* section is the one you will have to take care of.

For each *board* you want to build, you will have to create a dedicated section in the *Linkage* area, precisely describing the MCU, the toolchain, the build type and the RTOS you will use.

## Content explained
The following explains each line of the *linkage* section. Text highlighted in **bold** is an information that you will have to provide.

**_Note : Mind the forward slash ('/') in paths strings !_**

- "**OPTION1_NAME_HERE**"
	- Replace this text with a distinctive option name. e.g. *"STM32F429_Disco"*
- "short": "**<summary-here>**"
	- Replace the *<summary-here>* text with one word describing shortly your board. e.g. "F429Disco"
- "long": "**<description-here>**"
	- This is a more complete description of the configuration
- "BUILD_VERSION" : "**<version-number-for-the-build-format-is-N.N.N.N>**"
- "TOOLCHAIN_PREFIX" : "**<path-to-gcc-toolchain-mind-the-forward-slash>**"
	- This is the path to your gcc toolchain compiler. Use forward slashes and do not provide executable name here
- "TOOL_HEX2DFU_PREFIX" : "**<path-to-hex2dfu-utility-mind-the-forward-slash>**"
	- This is the path to the HEX2DFU utility. Use forward slashes and do not provide executable name here.
- "ESP32_IDF_PATH" : "**<path-to-esp-idf-mind-the-forward-slash>**"
	- This the path to the ESP32 IDF utility. Use forward slashes and do not provide executable name here.
- "TARGET_SERIES" : "**STM32F7xx**"
	- For STM32 MCUs represents the target series (STM32F4XX, STM32L4XX, and so on)
	- For ESP32 matches the series name: "ESP32"
- "USE_RNG" : "**ON**"
	- Option to enable the use of the hardware true random generator unit, if present. Default is ON as the majority of the targets have this feature.
- "DP_FLOATINGPOINT" : "**OFF**"
	- Enables support for double-precision floating point. The default is single-precision. Set to ON to enable double precision floating point.
- "SUPPORT_ANY_BASE_CONVERSION" : "**OFF**"
	- Defines which bases are supported when performing string to value conversions. When ON support for any base is enabled. When OFF (the default) the image will be compiled with support for base 10 and base 16 only.
- "RTOS" : "**<one-of-valid-rtos-options>**"
	- Defines the RTOS that will be used to build nanoFramework. It can be CHIBIOS or FREERTOS. Currently ChibiOS is supported for all STM32 targets and FreeRTOS is supported for ESP32 targets.
- "CHIBIOS_SOURCE" : "**<path-to-chibios-source-mind-the-forward-slash>**"
	- Path to an optional local installation of ChibiOS source files. If no path is given, then CMake will download the sources from the projects ChibiOS repository when needed
- "CHIBIOS_BOARD" : "**<valid-chibios-board-name-from-boards-collection>**"
	- Name of your board, chosen from the available boards collection that can be found in the \os\hal\boards folder of the ChibiOS installation (or distant repository)
- "SWO_OUTPUT" : "**OFF**"
	- Allows specifying whether to include, or not, support for Cortex-M Single Wire Output (SWO). Default is OFF. Check the documentation [here](arm-swo.md) for more details on how to use SWO.
- "NF_BUILD_RTM" : "**OFF**"
	- Sets if the build is of **R**eady **T**o **M**arket type. Meaning that all debug helpers and code blocks will be removed from compilation and the build will be compiled and linked with all possible code reducing options enabled.
- "NF_WP_TRACE_ERRORS" : "**OFF**"
	- Enable error tracing in Wire Protocol.
- "NF_WP_TRACE_HEADERS" :  "**OFF**"
	- Enable packet headers tracing in Wire Protocol.
- "NF_WP_TRACE_STATE" :  "**OFF**"
	- Enable state tracing in Wire Protocol.
- "NF_WP_TRACE_NODATA" :  "**OFF**"
	- Enable tracing of empty or incomplete packets in Wire Protocol.
- "NF_WP_TRACE_ALL" :  "**OFF**"
	- Enable all tracing options for Wire Protocol.
- "NF_WP_IMPLEMENTS_CRC32" :  "**OFF**"
	- Enable CRC32 calculations for Wire Protocol. See details [here](../architecture/wire-protocol.md#crc32-validatons).
- "NF_FEATURE_DEBUGGER" : "**OFF**"
	- Defines is support for debuggin managed applications is enabled. Default is OFF.
- "NF_FEATURE_RTC" : "**OFF**"
	- Allows you to specify whether to use the real time clock unit of the hardware for date & time functions. Depends on target availability. Default is OFF.
- "NF_FEATURE_USE_APPDOMAINS" : "**OFF**"
	- Allows you to specify whether to include, or not, support for Application Domains. Default is OFF. More information about this is available in the documentation [here](https://msdn.microsoft.com/en-us/library/cxk374d9(v=vs.90).aspx). ***Note that the complete removal of support for this feature is being considered (see issue [here](https://github.com/nanoframework/nf-interpreter/issues/303)).***
- "NF_FEATURE_WATCHDOG" : "**ON**"
    - Allows you to define it the hardware watchdog should be disabled.
	This setting can only be set to OFF for STM32 targets. ESP32 build enables this by default so there is no way to disable it.
	Default is ON, so the hardware watchdog will be enabled by default.
- "NF_FEATURE_HAS_CONFIG_BLOCK" : "**OFF**"
    - Allows the developer to set if the targets platform has configuration block.
    	This requires the the block storage definition and the linker files add support for that.
    	Default is OFF meaning that that the target DOES NOT have configuration block.
- "NF_PLATFORM_NO_CLR_TRACE" : "**OFF**"
	- Allows you to define if trace messages and checks are added to CLR or not.
	These checks are usually valuable when debugging issues within the CLR.
	Can and should be removed for RTM build flavours.
	Default is OFF meaning that all the standard trace and checks are added to the CLR.
- "NF_CLR_NO_IL_INLINE" : "**OFF**"
	- Allows you to define if CLR will use IL inlining.
	Default is OFF meaning that CLR will inline IL.
- "NF_INTEROP_ASSEMBLIES" : [ "Assembly1-Namespace", "Assembly2-Namespace" ]
	- Lists the name of the Interop assembly(ies) to be added to the build. Leave empty or don't add it if no Interop assembly is to be added.
- "API_System.Net" : "**OFF**"
	- Allows you to specify whether System.Net support is available to your application. Default is OFF.
- "API_Windows.Devices.Adc" : "**OFF**"
	- Allows you to specify whether ADC functions are available to your application. Default is OFF.
- "API_Windows.Devices.Gpio" : "**OFF**"
	- Allows you to specify whether GPIO functions are available to your application. Default is OFF.
- "API_Windows.Devices.I2c" : "**OFF**"
	- Allows you to specify whether I2C functions are available to your application. Default is OFF.
- "API_Windows.Devices.Pwm" : "**OFF**"
	- Allows you to specify whether PWM functions are available to your application. Default is OFF.
- "API_Windows.Devices.SerialCommunication" : "**OFF**"
	- Allows you to specify whether Serial Communication functions are available to your application. Default is OFF.
- "API_Windows.Devices.Spi" : "**OFF**"
	- Allows you to specify whether SPI functions are available to your application. Default is OFF.
- "API_Windows.Networking.Sockets" : "**OFF**"
	- Allows you to specify whether Networking Sockets functions are available to your application. Default is OFF.
- "API_Hardware.Esp32" : "**OFF**"
	- Allows you to specify whether Hardware.Esp32 functions are available to your application. Default is OFF. 
	Note that this API is exclusive of ESP32 targets and can't be used with any other.
- "API_Hardware.Stm32" : "**OFF**"
	- Allows you to specify whether Hardware.Stm32 functions are available to your application. Default is OFF.
	Note that this API is exclusive of STM32 targets and can't be used with any other.


## Working example
The following linkage section is a real example used to build nanoFramework for the MBN Quail board. It is using the minimal mandatory information :

```
"MBNQUAIL":
	{
		"oneWordSummary$": "QUAIL",
        "description$": "MBN Quail",
        "settings":
		{
            "TOOLCHAIN_PREFIX" : "C:/Program Files (x86)/GNU Tools ARM Embedded/5.4 2016q3",
            "TARGET_CHIP" : "STM32F427VIT",
			"TARGET_SERIES" : "STM32F4xx",
            "RTOS" : "CHIBIOS", 
            "CHIBIOS_SOURCE" : "C:/dev/ChibiOS_16.1.7",
            "CHIBIOS_BOARD" : "MBN_QUAIL"
			"NF_FEATURE_DEBUGGER" : "TRUE",
            "NF_FEATURE_RTC" : "ON",
			"NF_FEATURE_USE_APPDOMAINS" : "OFF",
			"NF_FEATURE_USE_NETWORKING" : "OFF",			
            "API_Windows.Devices.Gpio" : "ON"
        },
        "buildType": "Debug"
      },
```

## Templates 

To make your life easier, we provide templates with pre-configured cmake-variants.json for the various reference targets. Just grab them from our Gist.

-[ST_STM32F4_DISCOVERY](https://gist.github.com/nfbot/d4dbea239069146fe30d0869463507a8)

-[ST_STM32F429I_DISCOVERY](https://gist.github.com/nfbot/a5e04d750ff67d7b377f6aea74514208)

-[ST_NUCLEO_F091RC](https://gist.github.com/nfbot/cf7f6cfeb6f776ba068985bc44c005f0)

-[ST_NUCLEO144_F746ZG](https://gist.github.com/nfbot/6de229c9e6e64d5c48b729e077af7153)

-[ST_STM32F769I_DISCOVERY](https://gist.github.com/nfbot/efd47b5cfffdc7e54e388c37f1cb7a9c)

-[MBN_QUAIL](https://gist.github.com/nfbot/06723075c41d4e8f66ba511a4ce46e3f)

-[NETDUINO3_WIFI](https://gist.github.com/nfbot/dae2411ba9d2251c45d302ea1cac135a)

-[ESP32](https://gist.github.com/nfbot/627051a2f9f459d3c8f17752ca4985be)
