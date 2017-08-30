# Date and Time

**About this document**

This document describes how **nanoFramework** handles Date & Time and the available option regarding this matter.


## UTC and local time

Time (and date) is fundamental for the inner works of **nanoFramework**. But an application running on top of it can make use of it, or not, thus making relevant the discussion and evaluation of the related features and associated code.
Because **nanoFramework** runs on constrained resources platforms inclusion of features that increase both RAM and FLASH usage has to be considered and evaluated.

[`DateTime`](https://msdn.microsoft.com/en-us/library/system.datetime(v=vs.110).aspx) supports the use of Local and UTC times by its [`DateTime.Kind`](https://msdn.microsoft.com/en-us/library/system.datetime.kind(v=vs.110).aspx) property. Supporting this requires adding several _blocks_ such as: an API for setting the platform timezone, handling the huge number of available timezones, managing the daylight savings changes, manage conversion to/from the different kinds, etc.

Considering all the above, **nanoFramework** addresses this matter providing the _absolute minimal viable_ options.
There is support for `DateTime` (obviously) but all DateTime are considered UTC. There is no support for `DateTime.Kind.Local`, setting timezone or converting to/from the different kinds.
If an application requires this, it has to implement it at its own level.


## Time source

The _time base_ source is, by default, the `SysTick` available in the CMSIS RTOS API.
This is the _source_ of the time when a `DateTime` object is instantiated.

Because almost all hardware platforms capable of running **nanoFramework** include an hardware [RTC](https://en.wikipedia.org/wiki/Real-time_clock) this peripheral can be used as the _source_ for time objects.
Note that for all other internals of **nanoFramework** the CMSIS RTOS API `SysTick` keeps being used as the time base.

This option is exposed to the board designer by the `NF_FEATURE_RTC` configuration option. Setting it to `ON` when calling CMake brings in the RTC subsystem and all the calls to `DateTime` make use of the time base provided by this peripheral.  


## RTC and hardware

Leveraging the RTC hardware peripheral allows several interesting/valuable features:
- more accurate timekeeping (when compared with a regular timer);
- possibility for timekeeping in sleep/deep sleep modes;
- setting alarms to wake-up the system at a future time;
