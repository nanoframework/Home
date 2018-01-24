# Community targets build and publishing

**About this document**

This document describes the recipe to setup the build and publish of new Community targets.


## Introduction

The build of Community targets is handled on an unconventional approach. The reason for this is that using the traditional "build matrix" provided byt AppVeyor leads to several problems. 
The obvious ones are: lLaunching a build will get a job for each target in the build matrix. The latter is even more dumb when the changes concern only one (or some) of the targets thus wasting computing resources and taking ages as the number of targets increases.
To overcome the above the AppVeyor yaml was changed so it now relies on a PowerShell script that launches the build only for the selected targets. Or for all of then, if requested. There is no build matrix anymore, the target names and the build options are stored in a collection.
The _request_ to trigger the build for a specific target is made in the commit message by adding a _token_ (or more than one) with the board name(s), or `#ALL#`. The _token_ is the board name enclosed in '#', e.g. #I2M_OXYGEN_NF#.


## Build

Update the [appveyor.yml](https://github.com/nanoframework/nf-Community-Targets/blob/master/Cappveyor.yml) in the Community repository as follows:

1. Edit the PowerShell script [get-target-to-build.ps1](https://github.com/nanoframework/nf-Community-Targets/blob/master/get-target-to-build.ps1) and add to the collection of community targets the triplet: target name, build options and the requirement to generate (or not) _DFU_ files.


## Publish

Community target images are distributed trough **nanoFramework** JFrog Bintray [repository](https://bintray.com/nfbot/nanoframework-images-community-targets).

1. Sing-in with **nanoFramework** Bintray account.
2. Go to nanoframework-images-community-targets repository [here](https://bintray.com/nfbot/nanoframework-images-community-targets)

3. Add a new package inside that repository. 
   - The package name must be **exactly** the same as the target name otherwise the AppVeyor publish will fail.
   - The remaining details are to be copied from one of the other existing targets. Mind the description field to update the target name and possibly the manufacturer.

4. Go to the package main page of the recently created package and grab the markdown from the "Latest Version Badge" link there and past it in the Community targets list in the readme.
