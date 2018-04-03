# USB configuration of Virtual COM port (CDC)

**About this document**

This document describes the available settings/options to configure the USB Virtual COM port provided by ChibiOS HAL.
All these settings/options are exposed in the _usbcfg.c_ file, located in the _common_ folder of the reference boards that expose an USB device connector.


## USB Vendor

```#define USB_STRING_VENDOR  L"STMicroelectronics"```

In this setting it's defined the string that will show as the Vendor name for the USB device (showing in Windows Device manager, for example).
Adjust the string to whatever is to show there. Mind the L prefix, **DO NOT** remove it.


## USB Device description

```#define USB_STRING_DEVICE_DESCRIPTION  L"nanoFramework Virtual COM Port"```

In this setting it's defined the string that will show as the device description for the USB device (showing in Windows Device manager, for example).
Adjust the string to whatever is to show there. Mind the L prefix, **DO NOT** remove it.


## USB serial number

```#define USB_STRING_SERIAL_NUMBER      L"NANO_xxxxxxxxxxxx"```

In this setting it's defined the string that will show as the serial number of the USB device (showing in Windows Device manager, for example).
This serial number will be part of the instance path of the device that helps the OS to identify and address the USB device like in \\USB\\VID_0483&PID_5740\\NANO_3267335D3333.
Adjust the string to whatever is to show there. Mind the L prefix, **DO NOT** remove it.

_Note 1: nanoFramework ANT tool uses this serial number as a helper to identify nanoFramework devices relying that this string starts with_ **NANO_**_ (that is upper case NANO followed by an underscore)._

_Note 2: For STMicroelectronics reference boards the serial number is completed with the silicon unique ID available on their STM32 parts. Check the series manual for details._


## USB Vendor ID

```idVendor``` in the ```vcom_device_descriptor_data``` structure.
In this setting it's defined the [USB Vendor ID](http://www.usb.org/developers/vendor/) of the USB device. Hexadecimal 0x0483 in the reference boards (that's STMicroelectronics USB Vendor ID).

_Note: You are not allowed to use the USB Vendor from a third party without their express consent. If you want to use your own Vendor ID you have to apply for one with the USB organization._


## USB Product ID

```idProduct``` in the ```vcom_device_descriptor_data``` structure.
In this setting it's defined the [USB Product ID](http://www.usb.org/developers/usbfaq#12) of the USB device. Hexadecimal 0x5740 in the reference boards (that's STM USB product ID used in the Discovery and Nucleo boards).

_Note: You are not allowed to use the USB Vendor ID + Product from a third party without their express consent. If you want to use your own Vendor ID + Product ID you have to apply for one with the USB organization._
