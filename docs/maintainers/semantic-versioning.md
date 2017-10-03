# Semantic Versioning

**nanoFramework** versioning follows the [Semantic Versioning](http://semver.org/) guidelines.

Semantic versioning is all about releases and our continuous integration infrastructure uses [GitVersion](https://github.com/GitTools/GitVersion) to automatically version the releases as per the configuration of each repository.


**nanoFramework** follows the [GitFlow branching model](http://nvie.com/posts/a-successful-git-branching-model/) which allows more structured releases and versioning.


**nanoFramework** has three different workflows which control how the versioning.


## Development Builds

Builds from the *develop* branch have a suffix of alpha so that they are sorted higher than release builds which provides the team the ability to manually publish development builds to NuGet as pre-releases, if needed.

GitVersion is configured in [Continuous Deployment](http://gitversion.readthedocs.io/en/stable/reference/continuous-deployment/) mode which automatically increments the version per commit.


## Pull Request Builds

Builds from pull requests have a suffix of test$BuildNumber and are not automatically published to NuGet (if they are distributed by NuGet) but the packages - or artifacts - are available for download from AppVeyor which allows the team or anyone interested to test the unit of change without having to merge it into develop.


## Release Builds

Builds from the master branch do not have a suffix and GitVersion is configured in [Continuous Delivery](http://gitversion.readthedocs.io/en/stable/reference/continuous-delivery/) mode. If a commit is tagged, the version in the tag overrides the automatic versioning strategies.


# Versioning

**nanoFramework** follows the following version pattern: MAJOR.MINOR.PATCH[-PREVIEW\ALPHA\RC-BUILDNUMBER].

**Major** or **Breaking**:
* drop/adds support for a platform
* remove public API
* introduce incompatible API changes
* adopt a newer MAJOR version of an existing dependency
* disable a compatibility quirk off by default

**Minor**:
* add public API
* add new behavior
* add a new feature
* adopt a newer version of an existing dependency
* introduces a new dependency
* add functionality in a backwards-compatible manner
* any other change (not otherwise captured)

**Patch**:
* backwards-compatible bug fixes
* any other minor changes or improvements that are backwards-compatible
