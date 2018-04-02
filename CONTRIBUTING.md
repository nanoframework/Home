# Contributing to **nanoFramework**

The **nanoFramework** team maintains several guidelines for contributing to the **nanoFramework** repos, which are provided below. Many of these are straightforward, while others may seem subjective. A **nanoFramework** team member will be happy to explain why a guideline is defined as it is.

## Contribution Guidelines

- [General Contribution Guidance](#general-contribution-guidance) describes general contribution guidance, including more subjective stylistic guidelines.
- [Contribution Bar](#contribution-bar) describes the bar that the team uses to accept changes.
- [Contribution Workflow](docs/contributing/contributing-workflow.md) describes the workflow that the team uses for considering and accepting changes.
- [Copyright Notice](#copyright-notice) describes file header copyright notice format.

## General Contribution Guidance

There are several issues to keep in mind when making a change.

### Typos

Typos are embarrassing! We will accept most PRs that fix typos. In order to make it easier to review your PR, please focus on a given component with your fixes or on one type of typo across the entire repository. If it's going to take >30 mins to review your PR, then we will probably ask you to split it into smaller chunks.

### Commit Messages

Please format commit messages as follows (based on this [excellent post](http://tbaggery.com/2008/04/19/a-note-about-git-commit-messages.html)):

```
Summarize change in 50 characters or less

Provide more detail after the first line. Leave one blank line below the
summary and wrap all lines at 72 characters or less.

If the change fixes an issue, leave another blank line after the final
paragraph and indicate which issue is fixed in the specific format
below.

Fix #42
```

Also do your best to factor commits appropriately, i.e not too large with unrelated
things in the same commit, and not too small with the same small change applied N
times in N different commits. If there was some accidental reformatting or whitespace
changes during the course of your commits, please rebase them away before submitting
the PR.

### DOs and DON'Ts

* **DO** follow our C/C++ [coding style](docs/contributing/cxx-coding-style.md)
* **DO** follow our C# [coding style](docs/contributing/cs-coding-style.md)
* **DO** give priority to the current style of the project or file you're changing even if it diverges from the general guidelines.
* **DO** include tests when adding new features. When fixing bugs, start with
  adding a test that highlights how the current behavior is broken.
* **DO** keep the discussions focused. When a new or related topic comes up
  it's often better to create new issue than to side track the discussion.
* **DO** blog and tweet (or whatever) about your contributions, frequently!

* **DON'T** send PRs for style changes. 
* **DON'T** surprise us with big pull requests. Instead, open an issue and start
  a discussion so we can agree on a direction before you invest a large amount
  of time.
* **DON'T** commit code that you didn't write. If you find code that you think is a good fit to add to **nanoFramework**, open an issue and start a discussion before proceeding.
* **DON'T** submit PRs that alter licensing related files or headers. If you believe there's a problem with them, open an issue and we'll be happy to discuss it.
* **DON'T** add API additions without opening an issue and discussing with us first. See [API Review Process](docs/contributing/api-review-process.md).

### Contribution "Bar"

Project maintainers will merge changes that align with [project priorities](docs/contributing/project-priorities.md) and/or improve the product significantly for a broad set of apps. Proposals must also satisfy the published [guidelines for **nanoFramework**](#contribution-guidelines).

Maintainers will not merge changes that have narrowly-defined benefits, due to compatibility risks. Changes to the codebase must first be reviewed and tested to ensure they are correct and fit for purpose and will not inadvertently break applications. We may revert changes if they are found to introduce undesired states at a later date.

### Contributing Ports

We encourage adding support for other platforms and/or microcontroller units including vendors and families. We currently have ports for a number of STM32 based mcu's in progress and have a lot of momentum behind them. 

Ports have a weaker contribution bar, since they do not contribute to compatibility risk with existing products. For ports, we are primarily looking for functionally correct implementations.

### Copyright Notice

The following copyright notice header is used for all new files of original works:
```
//
// Copyright (c) 2017 The nanoFramework project contributors
// See LICENSE file in the project root for full license information.
//
```

For a file that is either a modification of an existing .NET Micro Framework file
or was created by copying portions of one or more .NET Micro Framework files,
the original notice has to be retained in the following format:
```
//
// Copyright (c) 2017 The nanoFramework project contributors
// Portions << original copyright >>
// See LICENSE file in the project root for full license information.
//
```
There are several copyright notices in .NET Micro Framework code base,
so for example `<< original copyright >>` may take the form:
```
Copyright (c) Microsoft Corporation.  All rights reserved.
```
> Note the extra space before `All`

or
```
Copyright (c) Microsoft Open Technologies, Inc. All rights reserved.
```

### Copying Files from Other Projects

**nanoFramework** uses some files from other projects, typically where a binary distribution does not exist or would be inconvenient.

The following rules must be followed for PRs that include files from another project:

- The license of the file is [permissive](https://en.wikipedia.org/wiki/Permissive_free_software_licence).
- The license of the file is left intact.
- The contribution is correctly attributed in the [3rd party notices](../../THIRD-PARTY-NOTICES) file in the repository, as needed.

<!--See [IdnMapping.cs](../../.cs) for an example of a file copied from another project and attributed in the [**nanoFramework** 3rd party notices](../../THIRD-PARTY-NOTICES) file. -->

### Porting Files from Other Projects

There are many good algorithms implemented in other languages that would benefit the **nanoFramework** project. The rules for porting a Java file to C# , for example, are the same as would be used for copying the same file, as described above.

[Clean-room](https://en.wikipedia.org/wiki/Clean_room_design) implementations of existing algorithms that are not permissively licensed will generally not be accepted. If you want to create or nominate such an implementation, please create an issue to discuss the idea.

### Contributor License Agreement

You must sign the [nanoFramework Contribution License Agreement](docs/contributing/cla.md) (CLA) before your PR can merged. This is a one-time requirement for projects maintained under the nanoFramework organization. You can read more about Contribution License Agreements (CLA) on [Wikipedia](https://en.wikipedia.org/wiki/Contributor_License_Agreement).
