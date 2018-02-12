# Thread execution

**About this document**

This document describes how thread execution works with the **nanoFramework** CLR.


## Native interrupt handlers

The functions implementing interrupt handlers for native code need to be _wrapped_ by the macros `NATIVE_INTERRUPT_START` and `NATIVE_INTERRUPT_END` that take care of setting/resetting the appropriate `System_State` flags. 
