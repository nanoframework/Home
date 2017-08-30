# Using Ninja to build **nanoFramework**


## Inside VS Code using CMake Tools

To setup the CMake tools to build using Ninja you have to follow the following steps:

1. Download and place the Ninja executable on a folder.

2. Edit the `settings.json` file that VS Code places inside the .vscode folder

3. Find a line for `"cmake.generator"`. If you don't have one just add it like this: `"cmake.generator": "Ninja",` 

4. Find a line for `"cmake.configureSettings"`. This is were the full path to the Nina executable should be set. Mind the forward slashes. 
If you don't have one just add a block like this: `"cmake.configureSettings": { "CMAKE_MAKE_PROGRAM": "E:/ninja/ninja.exe" },`

And that is it! Hit F7 or click the build configuration options for CMake Tools at the bottom toolbar.


## Performance comparison

A simple test to compare the performance of NMake and Ninja was carried. It's a complete build (nanoBooter and nanoCLR) for a STM32F429I_DISCOVERY target with debugger and GPIO enabled.

| Build tool | Time to complete build |
| --- |  --- |
| NMake | 3m 17sec |
| Ninja | 1m 19sec |
