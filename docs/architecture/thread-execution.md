# Thread execution

**About this document**

This document describes how thread execution works with the **nanoFramework** CLR.


## Introduction to Threads

Oversimplifying it a **nanoFramework** thread is (in terms of execution) basically a stream of IL instructions that are translated by the interpreter making things happen.
This execution occurs in a cooperative fashion, meaning that a thread is allowed to run for a certain amount of time, after that it stops and the execution is passed to the next thread that meets the required conditions to run.


## Thread execution

The **nanoFramework** CLR and interpreter run on a RTOS thread. When the RTOS works in a [cooperative](https://en.wikipedia.org/wiki/Computer_multitasking#Cooperative_multitasking) fashion (opposed to a [preemptive](https://en.wikipedia.org/wiki/Computer_multitasking#Preemptive_multitasking) fashion) the thread is expected to relinquish control to the RTOS so that context switching can occur and the next RTOS thread is given the opportunity to run.
This context switching in **nanoFramework** is expected to occur after each time slot that a **nanoFramework** thread is allowed to run.
It's up to the target board developer to provide the correct way to relinquish the control of the threads execution according to the RTOS running beneath.
This may not be required by all RTOS's. For example when by default the RTOS works in a preemptive fashion, the thread execution occurs in a round robin fashion among the various RTOS threads. 

_execution control relinquish_ is declared as `NANOCLR_RELINQUISHEXECUTIONCONTROL` in [nanoHAL_v2.h](../../src/HAL/Include/nanoHAL_v2.h). The actual implementation has to be provided at the target board level in the `targetHAL.h` header file.
For the current version of **nanoFramework** - which is using ChibiOS (a CMSIS compliant RTOS) - a simple call to `osDelay(1)` is sufficient and allows the kernel to run all the other threads with the same (or higher) priority.
