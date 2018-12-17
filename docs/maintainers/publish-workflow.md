# Merge Workflow and Strategy

**About this document**

This document describes the workflow and strategy adopted by **nanoFramework** to handle the merging, branching and release publishing.

## Pull Requests

Pull requests with contributions are **always** merged into _develop_ branch. 
On each pull request build the respective NuGet packages are published to nanoFramework [MyGet feed](https://www.myget.org/feed/Packages/nanoframework-dev) (if this is a component that uses this distribution channel). By sourcing this NuGet feed someone testing that pull request can reference it straight away without any further hassle.
There is nothing else to be done as the package identifier and the version are automatically incremented based upon the GitVersion configuration.

## Development

Once pull requests have been merged into _develop_ a new release is automatically generated and published to nanoFramework [MyGet feed](https://www.myget.org/feed/Packages/nanoframework-dev) (if this is a component that uses this distribution channel). 
There is nothing else to be done as the package identifier and the version are automatically incremented based upon the GitVersion configuration.

## Release Candidates

The process is kicked off by opening up a pull request from _develop_ to a new branch named _release-vN.N.N_ (note the branch name starting with _release_, this is mandatory for the configuration and scripts to properly recognize this as such).

If this release contains a breaking change then increase the MAJOR version by one and reset the MINOR back to zero and keep the PATCH at zero. Otherwise just bump the MINOR version by one and keep the PATCH at zero.

At this stage the contributor proposing a new release must perform a few administrative tasks. It's the responsibility of the release approver to verify that these tasks have been performed correctly.

Edit the source/version.json and bump the `version` field to the appropriate number matching the release at hand.

If the process for merging individual pull requests was followed perfectly there is not much else to do except verify that all pull requests have assigned a milestone and an appropriate label.
The label classifies the type of change and it's mandatory because the release notes are automatically generated from this information.
For the purposes of the automated release notes generation, only the pull requests have to follow this strict label mapping, not the issues. This is because the issue management is centralized in the Home repo (not per repository).
The pull requests that address an issue already link to that issue thus making easy to trace the changes and the reasoning about those, ultimately self-documenting the changes.

If there are any problems with the generated release notes document, resolve those in GitHub by assigning the appropriate labels to the pull requests and then re-run the build for the merge commit in Azure DevOps.

## Production

The process is kicked off by opening up a pull request from a _release-vN.N.N_ branch to _master_.

In the Home repository, edit the vNext milestone and change it to the version number of this release.

Once the pull request has been approved use the _merge commit_ option (**not the squash and merge**). This will trigger a new CI build after which a new draft release with be generated along with the release notes. If the validation of these has already been done in the _release-vN.N.N_ step above there should be no need for further corrections.

Pressing the publish release button will stamp the repository with a git tag with the release version, overriding any automatic versioning strategies and trigger a new build which will be automatically published to NuGet (if this is a component that uses this distribution channel).

After the build for the tag release is completed edit the source/version.json file and bump the `version` field to the vNext version, including the preview tag. Then start a new PR from the _release-vN.N.N_ into the develop branch. This makes any changes in that have been made branch should be deleted.

After the CI completes _squash and merge_ (**really really squash and merge**) the PR. The _release-vN.N.N_ branch can now be safely be deleted.

To complete this step create a new vNext milestone in the Home repo.
