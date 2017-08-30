# C/C++ Coding Style

For C/C++ files (*.c, *.cpp and *.h), we use clang-format (version 3.6+) to ensure code styling. 

## Using Visual Studio Code

If you are using Visual Studio Code we suggest that you install the [Clang-Format extension](https://marketplace.visualstudio.com/items?itemName=xaver.clang-format).
To have this extension working you need to have the clang-format.exe installed in your system.

LLVM.org doesn't provide a separate installer for this tool so follows a quick and dirty way of getting it.
1. Install the Clang-Format extension.
2. Install the Visual Studio plugin (as described bellow) and **DON'T** close the install window before opening the install log.
3. After a succesfull install of the plugin, scroll down the install log until you find the path where it was installed.
4. Copy that path and edit your VS Code user settings.
5. Add to the end of the setting collection the following:
```
"clang-format.executable" : "C:/Users/nnnnnnnnn/AppData/Local/Microsoft/VisualStudio/14.0/Extensions/yyyyyy.zzzz/clang-format.exe"
```
You might have something different in your setup. 
Just remeber the following: add that setting, the path that you've copied before, change it to have forward slashes and add the **clang-format.exe** at the end.

After following the above steps suceesfully you can now right click on any C, C++ or H file and hit 'Format Document'. The VS Code extension will take care that the document is properly formated according to the coding style guidelines.

## Using Visual Studio

If you are using Visual Studio we suggest that you install the [clang-format plugin for Visual Studio](http://llvm.org/builds/).
