# Procedure for creating a new repository

**About this document**

This document describes the recipe to create a new GitHub repository. It's meant for class libraries.

## Introduction

The strict following of this procedure is required in order to maintain consistency and coherence throughout the repositories, along with taking advantage of the build tools, testing and publishing automation.
If in doubt please ask one of the senior team members.

## Creating the repository in GitHub

1. This is basically clicking the create new repository button in GitHub. 

    Note: The class libraries repositories are following the pattern "lib-namespace" most of the remaining repositories "nf-some-relevant-name-here". This makes it easier to spot what is what.

2. As we are following the [GitFlow branching model](http://nvie.com/posts/a-successful-git-branching-model/) two branches must be created: `master` and `develop`.

3. Make sure to create an empty readme.md to make it easier to fork and clone the new repo.

## Adjust the repository settings (part 1)

1. Go to the repository settings and move into _Options_.

2. In the _Features_ section disable Wikis, Issues and Projects.

3. On the _Merge Button_ section disable Allow merge commits. We prefer to have tidy merges on PRs without having to bother contributors to squash commits.

4. Move into _Branches_ and set `develop` as the default branch.

## Setup the CLA

1. Open a browser window in Private Mode (so you can sign-in as `nfbot` and not loose you personal GitHub session).

2. Navigate to the [CLA Assistant](https://cla-assistant.io/).

3. Sign-in with GitHub `nfbot` account.

4. Click the "Configure CLA" button at the top left.

5. Select the newly created repo on the "Choose a repository" drop-down.

6. Select the "nanoFramework-CLA.md" in the next drop-down.

7. Click the "Link" button and agree with the next step.

8. On the list of the CLAs, find the new one and click on the ellipsis to the right and then 'Edit'. Add 
    `nfbot,*[bot]` into the field "Provide user names, who doesn't need to sign the CLA".

## Setup AppVeyor

1. Still on that Private browser window, navigate to [AppVeyor](https://ci.appveyor.com/projects).

2. Click "New Project" and select the newly created repo.

3. After the new project corresponding to the the new repo shows, go to "Settings".

4. Check that the default branch showing is "develop".

5. Check the "Save build cache in Pull Requests" option almost at the bottom.

6. Click "Save".

7. Move into "Environment" and create the following environment variables, filling in the value with the appropriate:
    - "MyGetToken": value with the token from MyGet feed.
    - "APPVEYOR_DISCORD_WEBHOOK_URL": value with URL of Discord GitHub pulse channel.
    - "NuGetToken": value with the token from NuGet organization.

8. Click "Save".

9. Move into "Badges" and copy the markdown code for master and develop branches. This will be required to add the correct build badges in the repo readme in a moment. Make sure to include in the URL the branch names on _all_ branches.

## Prepare the initial commit

1. Fork the repo into your preferred GutHub account and clone it locally.

2. The best option is to copy/past from an existing repo, so you're more efficient doing just that. Mind the name changes tough! Grab the following files:
    - .github\PULL_REQUEST_TEMPLATE.md _(no changes required)_
    - .gitignore _(no changes required)_
    - .github_changelog_generator
    - appveyor-discord.ps1 _(no changes required)_
    - appveyor.yml
    - CODE_OF_CONDUCT.md _(no changes required)_
    - commit-assemblyinfo-changes.ps1
    - CONTRIBUTING.md _(no changes required)_
    - generate-change-log.ps1
    - GitVersion.yml _(no changes required)_
    - install-vsix-appveyor.ps1 _(no changes required)_
    - LICENSE _(no changes required)_
    - README.md
    - template.vssettings _(no changes required)_
    - update-dependencies.ps1 _(this is only required if this class library is a dependency of others)_

3. Open "appveyor.yml"
    1. Rename the class library name occurrences with the new name.
    2. Rename the deploy "release description" with the new name.
    3. If this class library is a dependency of others, the section `on_success:` that installs NuKeeper and launches the update-dependecies PowerShell is required, otherwise it shouldn't exist.

4. Open ".github_changelog_generator" and set the _project_ to the repo name.

5. Open "GitVersion.yml" and set the _next_ version to the appropriate one. Make sure to follow our version number guidelines. In doubt please ask one of the senior team members.

6. Open "README.md"
    1. Rename the class library name occurrences with  the new name.
    2. Rename the package name for the Nuget badges.
    3. Replace the build status badges with the ones that you've copied from AppVeyor. Make sure that you past the correct ones. Don't misplace the develop in the the master!

7. Create a "source" folder that will hold the code files and VS Solutions and projects.

8. Create a "**Nuget.**class-lib-name" folder inside source.

9. Create a "**Nuget.**class-lib-name.DELIVERABLES" folder inside source.

10. Create a "class-lib-name" folder inside source.

11. Add the VS solutions for the class library and for the Nuget packages. Again it's better to follow an existing one and ask in doubt.
    1. Make sure you are following the naming pattern.
    2. Do not add a `.nuget` solution folder
    3. Make sure you copy the `key.snk` from the initial repo (or from the CorLib repo). DO NOT create a new one.

12. Open "commit-assemblyinfo-changes.ps"
    1. Rename the class library name occurrences with the new name.
    2. Adjust the RegEx in `$assemblyFiles` to the file name of this new project that can be found in the stubs folder after running the build. You have to return here after the

13. Open "update-dependencies.ps"
    1. Rename the class library name occurrences with the new name.
    2. Adjust the `$librariesToUpdate` array with the repo names of the class libraries that depend on this new one.

## Adjust the repository settings (part 2)

1. Go to the repository settings in GitHub and move into _Branches_.

2. Go to the rule for "develop" branch and change the following:
      - Enable "Require pull request reviews before merging"
      - Enable "Require status checks to pass before merging" with the options:
        - "Require branches to be up to date before merging"
        - "Status checks: continuous-integration/appveyor/pr" (for develop branch)
        - "Status checks: continuous-integration/appveyor/branch" (for master branch)
        - "Status checks: license/cla" (for develop branch)

## Update the dependency upwards

As a minimum the new class library depends on mscorlib. If that's the only dependency, edit the [`update-dependencies.ps1`](https://github.com/nanoframework/lib-CoreLibrary/blob/develop/update-dependencies.ps1) file there and add this new repo to the collection of the repositories there.
Now, if it depends on others, you have to figure out which one of those is _at the end_ of the dependency chain and add this new repo to _that_ `update-dependencies.ps1` file. For example, `Windows.Devices.Gpio` depends on `CoreLibrary` and `Runtime.Events` (which, in turn, depends on `CoreLibrary`). Updating it's dependencies has to the triggered at `Runtime.Events` not on `CoreLibrary`.

## Add the class library to the documentation project

If this class library has documentation that has to be published as part of nanoFramework documentation (which is most likely) it needs to be referenced in the documenation project.
Edit the documentation repo [AppVeyor yaml](https://github.com/nanoframework/nanoframework.github.io/blob/pages-source/appveyor.yml) and include the git clone operation for this new repo.
