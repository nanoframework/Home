# ADC configuration

**About this document**

This document describes how to configure the ADC and respective GPIO pins for a STM32 target board based in ChibiOS HAL/PAL.


## Assumptions and design

The STM32 parts can have up to 19 multiplexed channels (being 16 from external sources). Those can be grouped for special conversion scenarios that we are not going to use.
Each ADC channel can be exposed in one or more GPIO pins. Despite this providing more flexibility to a system designer it poses an additional complication at the time of configuring the ADC. 
Considering that the heavy-lifting on the ADC configuration and initial setup is performed by ChibiOS, we've tried to make the remaining configuration as simple as possible, which is pretty much mapping the GPIO pins.

For the remaining of this document we'll be using ST STM32F769I_DISCOVERY reference target and will configure the ADC to use the ADC channels exposed through the CN14 connector. From the schematics of the board (mb1225 F769I-DISCO schematic.pdf downloadable from ST web site) one can see that the following channels exposed:

| pad | GPIO pin | ADC channel |
|:-:|:-:|:-:|
| A0 | PA6 | ADC1_IN6 |
| A1 | PA4 | ADC1_IN4 |
| A2 | PC2 | ADC1_IN12 |
| A3 | PF10 | ADC1_IN8 |
| A4 | PF8 | ADC3_IN6 |
| A5 | PB8 | ADC3_IN7 |

To fully take advantage of the ADC hardware we are going to enable the internal ADC sources. These ones have to be mapped to ADC1.

| pad | GPIO pin | ADC channel |
|:-:|:-:|:-:|
| N.A. | N.A. | ADC1_TEMP_SENSOR |
| N.A. | N.A. | ADC1_VREFINT |
| N.A. | N.A. | ADC1_VBAT |


## Configurations

The configurations are all concentrated in the `target_windows_devices_adc_config.cpp` file in the reference target folder.
This source file is added to the CMake target only if the `API_Windows.Devices.Adc` option is set to ON. See the target CMakeList.txt.

There is a global `NF_PAL_ADC_PORT_PIN_CHANNEL` array for the ADC controller. On each entry there are the configurations for the ADC block, the GPIO port and pin along with the ADC internal channel reference. 
Note that for the internal sources channels the GPIO port and pin are to be set to `NULL` and those are only available on ADC1.
All the naming come from existing ChibiOS defines.

The configuration array will look like:
```
const NF_PAL_ADC_PORT_PIN_CHANNEL AdcPortPinConfig[] = {
    
    // ADC1
    {1, GPIOA, 6, ADC_CHANNEL_IN6},
    {1, GPIOA, 4, ADC_CHANNEL_IN4},
    {1, GPIOC, 2, ADC_CHANNEL_IN12},
    {1, GPIOF, 10, ADC_CHANNEL_IN8},

    // ADC3
    {3, GPIOF, 8, ADC_CHANNEL_IN6},
    {3, GPIOB, 8, ADC_CHANNEL_IN7},

    // these are the internal sources, available only at ADC1
    {1, NULL, NULL, ADC_CHANNEL_SENSOR},
    {1, NULL, NULL, ADC_CHANNEL_VREFINT},
    {1, NULL, NULL, ADC_CHANNEL_VBAT},
};
```
There is also a variable with the channel count, like this:
`const int AdcChannelCount = ARRAYSIZE(AdcPortPinConfig);`

To complete the configuration one has to enable ADC1 and ADC3 for ChibiOS HAL. Remember those were the ADC blocks used in the configuration above. This is done by editing the `mcuconf.h` file inside the target nanoCLR folder. Search for `STM32_ADC_USE_ADC1` and `STM32_ADC_USE_ADC3` and set those to `TRUE`.
