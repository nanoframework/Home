# Licensing options when using ChibiOS as the RTOS


**About this document**

This document provides a general overview of the licensing options available when using [ChibiOS](http://chibios.org) as the **nanoFramework** RTOS component.
The nanoFramework team have been in contact with the ChibiOS sales team to ensure accuracy of the following information at time of print (October 2017).

For details or to discuss your particular situation, we strongly recommend getting in touch with the ChibiOS [sales team](http://chibios.org/dokuwiki/doku.php?id=chibios:licensing:quote).


## What exactly is being used from ChibiOS in **nanoFramework firmware**?

**nanoFramework** is built against _unmodified_ ChibiOS sources via a mirror. It's using:
* The [HAL](http://chibios.org/dokuwiki/doku.php?id=chibios:product:hal:start), which is released under Apache License 2.0 meaning that it's 100% free to use or distribute without royalties for any purpose.
* The [RT](http://chibios.org/dokuwiki/doku.php?id=chibios:product:rt:start), is released under GPL3. See below for the licensing options which maybe different depending on your particular use. 


## Can I use ChibiOS freely for my hobby or personal development at home?

Yes, using ChibiOS in a Free and Open Source Software project or for personal use is perfectly fine.


## Can I use ChibiOS freely if I'm developing a commercial product?

Yes but please be aware of the following options:
* if you modify the [firmware](nanoframework/nf-interpreter) in any way and you are okay with [GPL3](https://www.gnu.org/licenses/gpl.html) licensing terms. Basically the firmware **MUST** keep your firmware open source.
* if you modify the [firmware](nanoframework/nf-interpreter) in any way and are okay with ChibiOS publicizing your use of it _and_ you clearly mention that your product is using ChibiOS.


## Can I use ChibiOS 'components licensing'?

'Components Licensing' is when you buy only parts of ChibiOS, for example the RT kernel with the CM4 port. This option **MUST** be discussed it with the ChibiOS sales team.


## What is a 'runtime license'?

The 'runtime license' is an option for the use of parts of ChibiOS in software products that are sold to 3rd parties. This option **MUST** be discussed with the ChibiOS sales team.


## What about managed apps (C#) running on **nanoFramework**?

Applications (the C# code) that are _loaded_ into and _executed by_ the [nanoframwork firmware](nanoframework/nf-interpreter) firmware image are not compiled or built by it due to the fact that it is interpreted on the fly from memory. As such, it can be deemed as a seperate component and _your_ C# managed code from a licensing perspective can be deemed seperate from the firmware. For discussion sake imagine that you won't ever load a managed app on the firmqare image. **nanoFramework** would still be perfectly working software, just not doing much.
As such this means that ChibiOS licensing doesn't apply to C# managed apps and it's use is not affected by the ChibiOS licensing terms.
