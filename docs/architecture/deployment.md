# Application deployment

**About this document**

This document describes how a managed **nanoFramework** application is deployed to a target device.


## Deployment preparation

The pre-requisites for deploying a managed **nanoFramework** application to a target device are very simple: a collection with the PE files for the target application and the referenced assemblies needs to be compiled. This collection of PE files is a blob with the binary contents of those files.


## Deployment

The deployment stage consists on erasing the required deployment blocks on the device (FLASH sectors) and programming them with the blob containing the binary versions of the PE files.

**nanoFramework** follows a simplified and high level approach to this. It's up to the programming application to manage the device memory, meaning that it will tell the device exactly where and what is going into the memory. 
Also there is no "reuse" of what might be already deployed on the device. All the PE files are always deployed. This has the advantage of not requiring the extra steps of reading back what's in the device, checking the exact versions and deciding if a certain PE file will fit on a flash block. The downside is that sometimes this causes unnecessary flash erase and write cycles. Considering that a typical modern SoC flash endurance limit is in the range of 100k to 1M cycles this is neglectable and acceptable for a device used for development purposes.
