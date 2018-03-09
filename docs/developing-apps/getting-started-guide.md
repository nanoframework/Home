# Getting Started Guide


**nanoFramework** enables the writing of managed code applications for embedded devices. Doesn’t matter if you are a seasoned .NET developer or if you’ve just arrived here and want to give it a try.

This getting started guide will walk you through the setup of your development machine to get you coding a nice “Hello World” in no time!
We presume you already have the hardware. 


## The hardware

In this guide we’ll be using a ST Microelectronics [STM32F746 NUCLEO](http://www.st.com/content/st_com/en/products/evaluation-tools/product-evaluation-tools/mcu-eval-tools/stm32-mcu-eval-tools/stm32-mcu-nucleo/nucleo-f746zg.html) board. This is a rather common and inexpensive board that packs a Cortex M7 with 1MB flash, 320 kB of RAM and includes an ethernet connector.


## Installing Visual Studio 2017

The first part is to get Visual Studio 2017 and the **nanoFramework** extension installed.

1.	Download Visual Studio 2017. If you already have it installed, you can skip this step. If you don’t, please download the free [Visual Studio Community 2017](https://www.visualstudio.com/downloads) edition. Either way, make sure you've selected the .NET desktop workload.

2.	Launch Visual Studio 2017 (we’ll just refer to it as VS from now on) and install the **nanoFramework** extension. You can do this by going into Tools > Extensions and Updates. Make sure you’ve switched the left-hand tree view to the Online branch and enter “nanoFramework” in the search box.

3.	Now open the Device Explorer window. You can do this by going into View > Other Windows > Device Explorer.


## Uploading the firmware to the board

The second part is to load the **nanoFramework** image in the board flash. Actually there are two images, one for nanoBooter and another one for nanoCLR.

1. Download the STM32 ST-LINK Utility from ST web site [here](http://www.st.com/content/st_com/en/products/development-tools/software-development-tools/stm32-software-development-tools/stm32-programmers/stsw-link004.html) and install it in your development machine.

2. Download a ZIP file with the firmware for the board from our web site [here](https://github.com/nanoframework/nf-interpreter#firmware-for-reference-boards) by clicking on the appropriate badge. This will take you to our JFrog Bintray repository that holds the packages with pre-build images for several target boards. After downloading it, unzip the package contents. 

3. Connect the STM32F746 NUCLEO board to your PC using an USB cable. In fact, you'll be needing two USB cables with a micro USB connector. One to connect to the ST-Link debugger, that doubles as power supply to the board. And a second one to connect the USB client of the board. 

4. Launch the ST-LINK Utility that you've just installed and connect to the STM32F746 NUCLEO board.

5. Perform a "full chip erase" to clear the flash.

6. Load the nanoBooter.hex file from the package and hit the "Program and verify" button. Make sure you tick the "Reset after programming" check box and hit "Start". After the upload completes, the MCU is reset and the nanoBooter image runs. You can check the success of the operation watching for a slow blink pattern on the LED. Congratulations, you now have a board running nanoFramework's booter!

7. Next, load the nanoCLR.hex file from the extracted package folder and hit again the "Program and verify" button. Make sure you tick the "Reset after programming" check box and hit "Start". After the upload completes, the MCU is reset and the nanoCLR image will run. This time and if all goes as expected, there will be no LED blinking. You can check if the board is properly running **nanoFramework** by looking into the Device Explorer window in VS.


## Coding an 'Hello World' application

Now you have everything that you need to start coding your first application. Let's go for a good old 'Hello World' in micro-controller mode, which is blinking a LED, shall we?

1. Go back to VS and click File > New > Project. Make sure you have selected 'Framework 4.6 or above' and choose nanoFramework, on the left hand side tree view. Choose the 'Blank Application' template and a location of your choosing were the project files will be saved. Name your project and hit OK. The program file will be automatically opened for you.

2. We'll code a very simple application that enters an infinite loop and turns on and off an LED. We'll skip the details because that's not the aim of this guide. Let's just grab the code from the **nanoFramework** samples repo [here](https://github.com/nanoframework/Samples/tree/master/Blinky). Make sure that the correct GPIO pin is being used. That's the line below the comment mentioning the STM32F746 NUCLEO board.

3. Because GPIO is being used we need to pull that class library and a reference to it in our project. The class libraries are distributed through NuGet. To add this class, right click on 'References' in the Solution Explorer and click 'Manage NuGet Packages'. On the search box type 'nanoFramework'. Make sure you have the preview checkbox ticked. Find the Windows.Devices.Gpio package and click "Install". After the license confirmation box, the package will be downloaded and a reference to it will be added. You'll notice that you no longer have the unknown references hints in VS.

4. Click "Build Solution" from the Build menu. A success message shows in the Build window.

5. We are almost there. Go into the Device Explorer window and click on the **nanoFramework** device showing there. Make sure the connection is OK by hitting the "Ping" button. On success, a message shows on the output window.

6. Let's deploy the application to the board. In order to do that, right click on the Project name and choose "Deploy". You'll see the feedback of the several operations that are running on the background in the Output Window. After a successful deployment, your 'Hello World' blinky application will start running and, _voilá_, the LED starts blinking!


## Wrapping up

Congratulations! That's your first **nanoFramework** C# application executing right there on the target board. How awesome is that?!

And this is it for the getting started guide. 
You've went through the steps required to install Visual Studio, the **nanoFramework** extension and the ST-LINK Utility.
You've also learned how to upload **nanoFramework** firmware images into a target board.
And last, but not the least: how to code a simple 'Hello World' C# application and deploy it to a target board.

Check out other guides and tutorials. You may also want to join our Slack workspace, where you'll find a supportive community to discuss your ideas and help you in case you get stuck on something.
