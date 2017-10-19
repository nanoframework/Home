# Licensing options when using ChibiOS as the RTOS


**About this document**

This document provides a general overview on the licensing options available when using [ChibiOS](http://chibios.org) as **nanoFramework** RTOS component.
We've been in touch with the ChibiOS sales team to clarify this as much as possible.

For details and to discuss your particular situation we strongly recommend getting in touch with the ChibiOS sales [here](http://chibios.org/dokuwiki/doku.php?id=chibios:licensing:quote).


## What exactly is being used from ChibiOS in **nanoFramework**?

**nanoFramework** is built against _unmodified_ ChibiOS sources. It's using:
* The [HAL](http://chibios.org/dokuwiki/doku.php?id=chibios:product:hal:start), which is released under Apache License 2.0 meaning that it's 100% free also for commercial use.
* The [RT](http://chibios.org/dokuwiki/doku.php?id=chibios:product:rt:start), which is released under GPL3. See bellow about the licensing options according to your use. 


## Can I use ChibiOS freely for my hobby or personal development at home?

Yes, using ChibiOS in FOSS project is perfectly fine.


## Can I use ChibiOS freely if I'm developing a commercial product?

Here there are several options:
* Yes, if you are OK with [GPL3](https://www.gnu.org/licenses/gpl.html) licensing terms. Basically you have to open your source code.
* Yes, if you are OK with ChibiOS publicizing your use of it _and_ you have to clearly mention that your product is using ChibiOS.


## Can I use ChibiOS 'components licensing'?

'Components Licensing' is when you buy only parts of ChibiOS, for example the RT kernel with the CM4 port. It can be an option, but you have to discuss it with the ChibiOS sales team.


## What is 'runtime license'?

The 'runtime license' is a way to use ChibiOS or parts of it into SW products that are sold to 3rd parties. It can be an option, but you have to discuss it with the ChibiOS sales team.


## What about managed apps (C#) running on **nanoFramework**?

These are applications that are _loaded into_ and _executed by_ the image build with ChibiOS code. Their source code isn't compiled or  built along with the ChibiOS code. Even if it was it would still be _your_ code and _another_ component in the build. The **nanoFramework** image after the build completes it's a finished, closed product by itself. For discussion sake imagine that you won't ever load a managed app on that image. **nanoFramework** would still be a perfectly working software, just not doing much.
To wrap this up: this means that ChibiOS licensing doesn't have any effect on managed apps and also that it's use is not affected by licensing terms of managed apps.
