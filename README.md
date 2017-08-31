![nanoFramework logo](resources/logo/nanoFramework-repo-logo.png)

-----

This _Home_ repository is the starting point for developers that want to learn about **nanoFramework**, contribute to it or open issues.
It contains links to the various GitHub repositories used by **nanoFramework**.

The goal of **nanoFramework** is to be a platform that enables the writing of managed code applications for constrained embedded devices. 
Developers can harness the familiar Visual Studio IDE and their .NET (C#) knowledge to quickly write applications without having to worry about the low level hardware intricacies of a micro-controller.

Being a developer you'll probably will fit in one (or maybe both :wink:) of the following _profiles_:
- Developer: if your goal is to develop C# applications for micro-controllers.
- Contributor: if you are interested in actively contributing code (native, managed, C, C++, CMake), writing documentation or participating in the overall project organization.


# Repositories

- [nf-interpreter](https://github.com/nanoframework/nf-interpreter) - this repo contains the **nanoFramework** [CLR](https://en.wikipedia.org/wiki/Common_Language_Runtime), interpreter, target board configurations and the build system. This is where everything required to build an image for flashing to a device lives.

- [nf-class-libraries](https://github.com/nanoframework/nf-class-libraries) - this repo contains the various Class Libraries (Core library - mscorlib, Windows.Devices.Gpio, Windows.Devices.Spi, etc.) that are used in developing C# applications. Each of the Solutions include a Nuget package configuration that is used to build each of the packages for distribution.

- [nf-Visual-Studio-extension](https://github.com/nanoframework/nf-Visual-Studio-extension) - this repo contains the Visual Studio extension and all the associated tooling required to compile and build a **nanoFramework** managed application. It also handles the communication with the target device required to deploy the managed code.

- [nf-Community-Targets](https://github.com/nanoframework/nf-Community-Targets) - this repo contains target boards that are contributed by community members. Here you may find _inspiration_ for your next board. Contributions are most welcome! Check the repo for details on how you can contribute.

- [nf-debugger](https://github.com/nanoframework/nf-debugger) - this repo contains the debugger library (in several technologies) allowing reuse of the low level library by third party applications.

- [nf-ANT](https://github.com/nanoframework/nf-ANT) - this repo contains a UWP application that connects to a **nanoFramework** target and can provide basic information about it along with some basic management operations. The development of this tool has been frozen because its features and capabilities are now available in Visual Studio through the Device Manager window accesible after installing the [Visual Studio extension](https://github.com/nanoframework/nf-Visual-Studio-extension).

- [ChibiOS](https://github.com/nanoframework/ChibiOS) - this repo contains a mirror of the official ChibiOS SVN repository. It's used as the default source for building **nanoFramework** images.

- [nf-github-bot](https://github.com/nanoframework/nf-github-bot) - this repo contains the code for the **nanoFramework** bots which help with managing various aspects of communication and the pull requests workflow.


## Build status

| Component | Build Status |
|:-|---|
| nanoBooter | [![Build Status](https://travis-ci.org/nanoframework/nf-interpreter.svg?branch=master)](https://travis-ci.org/nanoframework/nf-interpreter) |
| nanoCLR | [![Build Status](https://travis-ci.org/nanoframework/nf-interpreter.svg?branch=master)](https://travis-ci.org/nanoframework/nf-interpreter) |
| Win32 test project | [![Build status](https://ci.appveyor.com/api/projects/status/94fldjinqji4w977?svg=true)](https://ci.appveyor.com/project/nfbot/nf-interpreter) |
| Class Libraries | [![Build status](https://ci.appveyor.com/api/projects/status/terbqvfdlw8po3cm?svg=true)](https://ci.appveyor.com/project/nfbot/nf-class-libraries) |
| Visual Studio extension | [![Build status](https://ci.appveyor.com/api/projects/status/9mtqen1wi0tv8x54?svg=true)](https://ci.appveyor.com/project/nfbot/nf-visual-studio-extension) |


## How to Engage, Contribute and Provide Feedback

Some of the best ways to contribute are to try things out, file bugs, and join in design conversations.


If you are having issues or need clarification on something, instead of opening an issue it is best to start a conversation on one of our Slack channels.
Please select the channel that's most appropriate to the context so subject matter experts are most likely to answer promptly.

You can join our lively Slack community by filling in this [invite form](https://nanoframework.wordpress.com/slack-invite-form/).


If you've found a bug or can't use Slack, please open an [Issue](https://github.com/nanoframework/Home/issues).
We ask you to open an issue only when you have a confirmed bug which is repeatable through a code example or manually defined steps. Don't open an issue for support requests or to start a discussion, you'll get better (and quicker!) support/feedback in one of the Slack channels.

Looking for something to work on? A great place to start is to check the list of up-for-grabs issues on any of the repositories.

See some of our guides for more details:

* [Contributing Guide](CONTRIBUTING.md)


## Documentation

### [Docs](docs/)

The project documentation is a great place to find information about **nanoFramework**, no matter if you are newcomer or a veteran. It's organized into the following categories:
- [Developing C# applications](docs/developing-apps) using **nanoFramework**.
- [Building an image](docs/building) to load on a target board.
- [**nanoFramework** architecture](docs/architecture/) and how the different pieces fit together.
- [Contributing to **nanoFramework**](docs/contributing/) includes an overview on how you can contribute to the project. 


### [Blog](https://nanoframework.wordpress.com)

The project has a blog where we try to post detailed updates about the development status, technical posts about particular features or design options taken and our reasoning behind them.


## Who is behind this project?

There are a number of people behind this project. We are mostly embedded systems enthusiasts, passionate about coding and people that like challenges. 
All of us have our daily jobs and we work on this project in our free time.
That is to say that you can always expect an answer from us. Maybe not instantly but - hopefully - in a timely fashion :wink: !


## Code of Conduct
This project has adopted the code of conduct defined by the [Contributor Covenant](http://contributor-covenant.org/)
to clarify expected behavior in our community.
