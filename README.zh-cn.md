[![#yourfirstpr](https://img.shields.io/badge/first--timers--only-friendly-blue.svg)](https://github.com/nanoframework/Home/blob/master/CONTRIBUTING.md) 
[![Average time to resolve an issue](http://isitmaintained.com/badge/resolution/nanoframework/home.svg)](http://isitmaintained.com/project/nanoframework/home "Average time to resolve an issue") [![Percentage of issues still open](http://isitmaintained.com/badge/open/nanoframework/home.svg)](http://isitmaintained.com/project/nanoframework/home "Percentage of issues still open") [![](https://badgen.net/opencollective/backers/nanoframework?label=Open%20Collective%20backers)](https://opencollective.com/nanoframework) [![Discord](https://img.shields.io/discord/478725473862549535.svg?logo=discord&logoColor=white&label=Discord&color=7289DA)](https://discord.gg/gCyBu8T)

![nanoFramework logo](resources/logo/nanoFramework-repo-logo.png)

-----
文档语言: [English](README.md) | [简体中文](README.zh-cn.md)

# .NET **nanoFramework** 首页

[<img align="right" width="100px" src="https://dotnetfoundation.org/img/logo_big.svg" />](https://dotnetfoundation.org/)

本库是开发者了解 .NET **nanoFramework** 的起点，也可以贡献或提问。它包含了 .NET **nanoFramework** 所使用到的各个GitHub库链接。

.NET **nanoFramework** 的目标是在受限嵌入式设备上使用托管代码编写应用。开发者可以利用熟悉的IDE(Visual Studio)和 .NET(C#)知识快速编写应用程序，而无需担心微控制器的低级硬件复杂性。

它是 [.NET Foundation](https://www.dotnetfoundation.org/) 的一部分。

作为一名开发者，你可以选择以下一种（或两种）角色：

- 开发者：如果你的目标是为微控制器开发C#应用。
- 贡献者：如果你有兴趣通过编码（原生，托管，C/C++，CMake）积极贡献，包括编写文档或者参与整个项目组织。

# 赞助 .NET **nanoFramework**

大多数核心团队成员和贡献者都是嵌入式系统爱好者，热衷于编码和喜欢挑战的人。.NET **nanoFramework** 工作都是他们在工作之余完成。一些核心成员恰好工作于那些大力赞助 .NET **nanoFramework** 并为其提供工作时间的公司。如果你想把 .NET **nanoFramework** 用于正式工作并支持它，请捐赠。这样可以支付基础设施成本，并为项目投入更多的时间。除了货币捐助，还有其它几种捐助方式，请参考 [这里](http://docs.nanoframework.net/content/contributing/index.html).

我们如何使用捐赠：

- 支付基础设施成本。
- 宣传推广项目。
- 支持在项目中投入大量时间的维护人员和贡献者。
- 支持 .NET **nanoFramework** 所依赖的项目。
- 制作产品文档、教程以及其它内容，以支持使用 .NET **nanoFramework** 的其他开发人员。
- 组织活动演示 .NET **nanoFramework**

## 赞助商

赞助商将在我们的Github自述文件和主页上获得他们的徽标和链接。

<a href="https://opencollective.com/nanoframework#support"><img src="https://opencollective.com/nanoframework/tiers/sponsor.svg?avatarHeight=80"></a>

## 支持者

支持者是那些用金钱帮助支持 .NET **nanoFramework** 的人。每一点点的帮助，我们都很感激所有的贡献，即使是最小的贡献。

<a href="https://opencollective.com/nanoframework#support"><img src="https://opencollective.com/nanoframework/tiers/backer.svg?avatarHeight=80"></a>

## 其他支持者和赞助商

还有其他人和组织一直以多种方式为.NET **NanoFramework**做出贡献：赞助对缺失或需要改进的功能进行编码、支付费用、对功能进行编码或……我们要感谢这些赞助商。

<table>
 <tr>
  <td><a href="http://www.eclo.solutions"><img src="http://www.eclo.solutions/images/eclo-solutions-logo-tall.svg" height="100" width="151"/></a></td>
  <td><a href="https://www.orgpal.com"><img src="https://www.orgpal.com/orgpallogo.png" height="100" width="228"/></a></td>
  <td><a href="http://www.chibios.org"><img src="https://upload.wikimedia.org/wikipedia/commons/c/cd/ChibiOS_Embeddedware_Official_Logo.jpg" height="100" width="100" alt="ChibiOS RTOS"/></a></td>
 </tr>
</table>

## 评估板固件

以下每个ZIP文件包括了nanoBooter和nanoCLR镜像（HEX，BIN，DFU）。可以使用相应烧写工具把它们写入目标板卡中。

**稳定** 版是RTM最小大小编译。它包含了最后稳定版本，关闭调试功能，仅有最少或没有错误信息。
**预览** 版是目标板持续编译。它包含所有功能和错误修正的最后版本，也包括调试信息和详细错误信息。

| 目标 | 稳定 | 预览 |
|:-|---|---|
| ESP32_WROOM_32 | [ ![Download](https://api.bintray.com/packages/nfbot/nanoframework-images/ESP32_WROOM_32/images/download.svg) ](https://bintray.com/nfbot/nanoframework-images/ESP32_WROOM_32/_latestVersion) | [![Latest Version @ Cloudsmith](https://api-prd.cloudsmith.io/v1/badges/version/net-nanoframework/nanoframework-images-dev/raw/ESP32_WROOM_32.zip/latest/x/?render=true&badge_token=gAAAAABgWxsQ0EOQ1_NxwC74J7T4CPbdGB3unrMqV-ALAnO7NmQeLcrlPWAehyXUQ3_4EsiE30fOp-boZmAADZwTcQBKv8-gJTmJhUP0DeZJCMsdWf4lBP4%3D)](https://cloudsmith.io/~net-nanoframework/repos/nanoframework-images-dev/packages/detail/raw/ESP32_WROOM_32.zip/latest/) |
| ESP_WROVER_KIT | [ ![Download](https://api.bintray.com/packages/nfbot/nanoframework-images/ESP_WROVER_KIT/images/download.svg) ](https://bintray.com/nfbot/nanoframework-images/ESP_WROVER_KIT/_latestVersion) | [![Latest Version @ Cloudsmith](https://api-prd.cloudsmith.io/v1/badges/version/net-nanoframework/nanoframework-images-dev/raw/ESP_WROVER_KIT.zip/latest/x/?render=true&badge_token=gAAAAABgWxs0sy_Z0SJKVtabJLFxB-wercZM99WqrRSZZVSfcOeW2EjIhyu3MPq36A2-St-aqhmoVxICvlJM0Fg2JXx46vLcuM1vpL2AnKbEaPbpFd2tY64%3D)](https://cloudsmith.io/~net-nanoframework/repos/nanoframework-images-dev/packages/detail/raw/ESP_WROVER_KIT.zip/latest/) |
| ESP32_PICO | [ ![Download](https://api.bintray.com/packages/nfbot/nanoframework-images/ESP32_PICO/images/download.svg) ](https://bintray.com/nfbot/nanoframework-images/ESP32_PICO/_latestVersion) | [![Latest Version @ Cloudsmith](https://api-prd.cloudsmith.io/v1/badges/version/net-nanoframework/nanoframework-images-dev/raw/ESP32_PICO.zip/latest/x/?render=true&badge_token=gAAAAABgWxtNdQxouHYolWQFagVq8taYLJzrxmbrP-_3yisFna9pGplAkfsCxyc-JhjD9c6KvIPjPKRId6E6-X9RswLd9vKx3pf4dX1TIcPF26YJG9uCTc4%3D)](https://cloudsmith.io/~net-nanoframework/repos/nanoframework-images-dev/packages/detail/raw/ESP32_PICO.zip/latest/) |
| ST_STM32F429I_DISCOVERY | [ ![Download](https://api.bintray.com/packages/nfbot/nanoframework-images/ST_STM32F429I_DISCOVERY/images/download.svg) ](https://bintray.com/nfbot/nanoframework-images/ST_STM32F429I_DISCOVERY/_latestVersion) | [![Latest Version @ Cloudsmith](https://api-prd.cloudsmith.io/v1/badges/version/net-nanoframework/nanoframework-images-dev/raw/ST_STM32F429I_DISCOVERY.zip/latest/x/?render=true&badge_token=gAAAAABgWxtgAxHQjTJGznPOINUoT_Ej3tdlloXGP3tyipuu1bigH-NFmKsDiJqOFZhkYzo0HuekIdfn_af2KBfO-IrHuHd-9FrqP7nFVvuIpriyBU29jKM%3D)](https://cloudsmith.io/~net-nanoframework/repos/nanoframework-images-dev/packages/detail/raw/ST_STM32F429I_DISCOVERY.zip/latest/) |
| ST_NUCLEO64_F091RC | [ ![Download](https://api.bintray.com/packages/nfbot/nanoframework-images/ST_NUCLEO64_F091RC/images/download.svg) ](https://bintray.com/nfbot/nanoframework-images/ST_NUCLEO64_F091RC/_latestVersion) | [![Latest Version @ Cloudsmith](https://api-prd.cloudsmith.io/v1/badges/version/net-nanoframework/nanoframework-images-dev/raw/ST_NUCLEO64_F091RC.zip/latest/x/?render=true&badge_token=gAAAAABgWxuEsfOKMwTQ4p8tNlgFltGI-TQyh6hS-c4m2fn3cOiiCoH2Zs_A9blCjwIA_ldqDk7OdlvCONxjn7si9t-xqPyHyAT8j-1cnAuwtKpY9iV1-_o%3D)](https://cloudsmith.io/~net-nanoframework/repos/nanoframework-images-dev/packages/detail/raw/ST_NUCLEO64_F091RC.zip/latest/) |
| ST_STM32F769I_DISCOVERY | [ ![Download](https://api.bintray.com/packages/nfbot/nanoframework-images/ST_STM32F769I_DISCOVERY/images/download.svg) ](https://bintray.com/nfbot/nanoframework-images/ST_STM32F769I_DISCOVERY/_latestVersion) | [![Latest Version @ Cloudsmith](https://api-prd.cloudsmith.io/v1/badges/version/net-nanoframework/nanoframework-images-dev/raw/ST_STM32F769I_DISCOVERY.zip/latest/x/?render=true&badge_token=gAAAAABgWxuSyThy9rWl2BFzOgy1r4LRv1KYZe_vU3VicNMvPjsbwg3ps-x_V1aC8yiSoIXwIP8aPw3Ph6-wCpJZqUJduVtpp2s_UR6P2ccwtoOMJGjlvJ8%3D)](https://cloudsmith.io/~net-nanoframework/repos/nanoframework-images-dev/packages/detail/raw/ST_STM32F769I_DISCOVERY.zip/latest/) |
| ORGPAL_PALTHREE | [ ![Download](https://api.bintray.com/packages/nfbot/nanoframework-images/ORGPAL_PALTHREE/images/download.svg) ](https://bintray.com/nfbot/nanoframework-images/ORGPAL_PALTHREE/_latestVersion) | [![Latest Version @ Cloudsmith](https://api-prd.cloudsmith.io/v1/badges/version/net-nanoframework/nanoframework-images-dev/raw/ORGPAL_PALTHREE.zip/latest/x/?render=true&badge_token=gAAAAABgWxuvhPup6KikfsjlSNopnl1YJj6kwaw3ZKb4ePHYbU-kp3YcyQ5fggVV_eyGSa9Gh53-TIJ5RIbFMV8gvKnvDCTczJW8CpelDLyMgP373Ey10hw%3D)](https://cloudsmith.io/~net-nanoframework/repos/nanoframework-images-dev/packages/detail/raw/ORGPAL_PALTHREE.zip/latest/) |
| NETDUINO3_WIFI | [ ![Download](https://api.bintray.com/packages/nfbot/nanoframework-images/NETDUINO3_WIFI/images/download.svg) ](https://bintray.com/nfbot/nanoframework-images/NETDUINO3_WIFI/_latestVersion) | [![Latest Version @ Cloudsmith](https://api-prd.cloudsmith.io/v1/badges/version/net-nanoframework/nanoframework-images-dev/raw/NETDUINO3_WIFI.zip/latest/x/?render=true&badge_token=gAAAAABgWxvAxFISErASMvjPfBiilCIOBObv-i9TAxVYbL0_kXOsLOGv_5CFTD9sQ_NHjSB4TNhTB4AnA0aed7VG-Vu9koWwHxMQs-1Bo_LlB9tufBhubGE%3D)](https://cloudsmith.io/~net-nanoframework/repos/nanoframework-images-dev/packages/detail/raw/NETDUINO3_WIFI.zip/latest/) |
| TI_CC1352R1_LAUNCHXL_868 | [ ![Download](https://api.bintray.com/packages/nfbot/nanoframework-images/TI_CC1352R1_LAUNCHXL_868/images/download.svg) ](https://bintray.com/nfbot/nanoframework-images/TI_CC1352R1_LAUNCHXL_868/_latestVersion) | [![Latest Version @ Cloudsmith](https://api-prd.cloudsmith.io/v1/badges/version/net-nanoframework/nanoframework-images-dev/raw/TI_CC1352R1_LAUNCHXL_868.zip/latest/x/?render=true&badge_token=gAAAAABgWxvs4c8caJtRfrxQMUln4iKcBPy3j_L6K3BNZRBKFt5YjIhU9qSFzoPqyM0s4RGTFrUUTg1VN6YID7MkrGf3PeZT_2dW9mR5VdFkIGnrnVW9vtA%3D)](https://cloudsmith.io/~net-nanoframework/repos/nanoframework-images-dev/packages/detail/raw/TI_CC1352R1_LAUNCHXL_868.zip/latest/) |
| TI_CC1352R1_LAUNCHXL_915 | [ ![Download](https://api.bintray.com/packages/nfbot/nanoframework-images/TI_CC1352R1_LAUNCHXL_915/images/download.svg) ](https://bintray.com/nfbot/nanoframework-images/TI_CC1352R1_LAUNCHXL_915/_latestVersion) | [![Latest Version @ Cloudsmith](https://api-prd.cloudsmith.io/v1/badges/version/net-nanoframework/nanoframework-images-dev/raw/TI_CC1352R1_LAUNCHXL_915.zip/latest/x/?render=true&badge_token=gAAAAABgWxv9FGSgTGts-1jHwH4R9rCD74Ry-HDqgamGyMxcIFB4w0ByEzLiVXRFvTwpromS_Zi2uMRnXHLPP4XEO9lJmGJbHEDrexyss9tSU9jHx_C2ybc%3D)](https://cloudsmith.io/~net-nanoframework/repos/nanoframework-images-dev/packages/detail/raw/TI_CC1352R1_LAUNCHXL_915.zip/latest/) |
| TI_CC3220SF_LAUNCHXL | [ ![Download](https://api.bintray.com/packages/nfbot/nanoframework-images/TI_CC3220SF_LAUNCHXL/images/download.svg) ](https://bintray.com/nfbot/nanoframework-images/TI_CC3220SF_LAUNCHXL/_latestVersion) | [ ![Download](https://api.bintray.com/packages/nfbot/nanoframework-images-dev/TI_CC3220SF_LAUNCHXL/images/download.svg) ](https://bintray.com/nfbot/nanoframework-images-dev/TI_CC3220SF_LAUNCHXL/_latestVersion) |
| NXP_MIMXRT1060_EVK | [ ![Download](https://api.bintray.com/packages/nfbot/nanoframework-images/NXP_MIMXRT1060_EVK/images/download.svg) ](https://bintray.com/nfbot/nanoframework-images/NXP_MIMXRT1060_EVK/_latestVersion) | [![Latest Version @ Cloudsmith](https://api-prd.cloudsmith.io/v1/badges/version/net-nanoframework/nanoframework-images-dev/raw/NXP_MIMXRT1060_EVK.zip/latest/x/?render=true&badge_token=gAAAAABgWxwUlaLK-cw0e71em0ksycYwgy8Xxc44JLI3_ZwxxrszUOEzLud2mKaWr6GUuPjaw84h9BoKzf_1ksd5eZ1n1IpeYOmpGmMWbEYrYrQCAeZNFCw%3D)](https://cloudsmith.io/~net-nanoframework/repos/nanoframework-images-dev/packages/detail/raw/NXP_MIMXRT1060_EVK.zip/latest/) |


以上固件支持以下类库和功能：


<details>
  <summary>点击展开</summary>

  | Target                  | Gpio               | Spi                | I2c                | Pwm                | Adc                | Dac                | Serial             | OneWire            | Events             | SWO                | Networking         | Large Heap         | UI         |
  |:-:                      |:-:                 |:-:                 |:-:                 |:-:                 |:-:                 |:-:                 |:-:                 |:-:                 |:-:                 |:-:                 |:-:                 |:-:                 |:-:                 |
  | ESP32_WROOM_32          | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: |                    | :heavy_check_mark: | :heavy_check_mark: |                    |
  | ESP_WROVER_KIT          | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: |                    | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: |
  | ESP32_PICO          | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: |                    | :heavy_check_mark: | :heavy_check_mark: |                    |
  | ST_STM32F429I_DISCOVERY | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: |                    | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: |                    | :heavy_check_mark: |                    |
  | ST_NUCLEO64_F091RC      | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: |                    |                    | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: |                    |                    |                    |
  | ST_STM32F769I_DISCOVERY | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: |
  | ORGPAL_PALTHREE | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: |                    |
  | MBN_QUAIL               | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: |                    |                    | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: |                    |                    |                    |                    |
  | NETDUINO3_WIFI          | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: |                    | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: |                    |                    |                    |                    |
  | TI_CC1352R1_LAUNCHXL    | :heavy_check_mark: |  |  |  |  |                    |                    |                    |  |                    |  |                    |                    |
  | TI_CC3220SF_LAUNCHXL    | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: |                    |                    |                    | :heavy_check_mark: |                    | :heavy_check_mark: |                    |                    |
  | NXP_MIMXRT1060_EVK           | :heavy_check_mark: |  |  |  |  |  | :heavy_check_mark:  |                    | :heavy_check_mark: |                    | :heavy_check_mark: | :heavy_check_mark: |                    |
</details>

## 社区目标板固件

除了上面的固件映像，您还可以为社区提供的目标板找到其他几个映像。在 [社区目标库](https://github.com/nanoframework/nf-Community-Targets) 上检查可用的链接并下载。

## 项目库

我们的GitHub团队拥有用于固件、类库、文档和工具的各种项目库。
你可以在 [这里](docs/organization/README.md) 得到一个列表和描述。

## 如何参与、贡献和提供反馈

贡献的一些最好方法是尝试去整理问题解决问题，并参与到设计讨论中。
如果你有好的创意，或者希望表达清楚某个问题，最好不要打开问题，而是在我们的 [Discord](https://discord.gg/gCyBu8T) 频道中讨论。
请选择最适合您所面临的问题的解决方案。

如果你发现一个bug，或者不能使用 Discord，请打开问题 [Issues](https://github.com/nanoframework/Home/issues)。
我们希望你只有在你有一个真实确定的问题是才打开一个问题，而不是为了请求支持或开展讨论。使用 [Discord](https://discord.gg/gCyBu8T) 会得到更好的支持反馈。

这个列表可以找到需要解决的若干问题， [up-for-grabs issues](https://github.com/nanoframework/Home/issues?q=is%3Aissue+is%3Aopen+label%3Aup-for-grabs) ，这是一个不错的切入点。

有关更多详细信息，请参阅我们的一些指南：

- [贡献指南](https://github.com/nanoframework/.github/blob/master/CONTRIBUTING.md)
- [贡献流程](https://docs.nanoframework.net/content/contributing/contributing-workflow.html)

## 许可证

.NET **nanoFramework** 库、固件映像、工具和示例根据 [MIT license](LICENSE.md) 获得许可。

## 文档

### [文档](https://docs.nanoframework.net)

无论您是新手还是老手，项目文档都是查找有关.NET **nanoFramework**信息的好地方。它按以下类别组织：

- [API手册](http://docs.nanoframework.net/api) 各种类库的文档。
- [开发C#应用](https://docs.nanoframework.net/content/getting-started-guides/getting-started-managed.html#coding-a-hello-world-application) 使用 .NET **nanoFramework**.
- [编译镜像](https://docs.nanoframework.net/content/building/index.html) 加载到目标板上。
- [.NET **nanoFramework**架构](https://docs.nanoframework.net/content/architecture/index.html) 不同的部分是如何组合在一起的。
- [贡献.NET **nanoFramework**](https://docs.nanoframework.net/content/contributing/index.html) 包括如何为项目做出贡献的概述。

### [博客](https://www.nanoframework.net/blog)

有一个博客，我们尝试发布关于开发状态的详细更新，关于某个特定功能的技术文章，或者设计选项。

### [YouTube 频道](https://www.youtube.com/c/nanoFramework)

我们还有一个YouTube频道，里面有视频教程，还有关于我们正在试验的功能演示和新想法构思。

## 行为准则

该项目通过了《贡献者公约》界定的行为守则，以澄清我们社区的预期行为。
有关详细信息，请参阅 [.NET Foundation 行为准则](https://dotnetfoundation.org/行为准则)。
