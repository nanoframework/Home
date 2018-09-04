# Contribution Workflow

You can contribute to **nanoFramework** with issues and PRs. Simply filing issues for problems you encounter is a great way to contribute. Contributing implementations is greatly appreciated.


### Table of contents

- [Getting Started](#getting-started)
- [Making a change](#making-a-change)
- [Typos](#typos)
- [Coding Style Changes](#coding-style-changes)
- [Commit Messages](#commit-messages)
- [Contributor License Agreement](#contributor-license-agreement)
- [PR Feedback](#pr-feedback)
- [Working on an open issue](#working-on-an-open-issue)
- [Suggested Workflow](#suggested-workflow)
- [General git resources](#general-git-resources)


## Getting Started

If you are looking at getting your feet wet with some simple (but still beneficial) changes, check out [_up-for-grabs_](https://github.com/nanoframework/Home/issues?q=is%3Aissue+is%3Aopen+label%3Aup-for-grabs) issues on the [**nanoFramework** Home](https://github.com/nanoframework/Home) repo.

For new ideas, please always start with an issue before starting development of an implementation. See [project priorities](project-priorities.md) to understand the team's approach to engagement on general improvements to the product.

You do not need to file an issue for trivial changes (e.g. typo fixes). Just create a PR for those changes.


## Making a change

Make a quality change. Consider and document (preferably with tests) as many usage scenarios as you can to ensure that your change will work correctly in the miriad of ways it might get used.

There are several issues to keep in mind when making a change.


## Typos

Typos are embarrassing! We will accept most PRs that fix typos. In order to make it easier to review your PR, please focus on a given component with your fixes or on one type of typo across the entire repository. If it's going to take >30 mins to review your PR, then we will probably ask you to chunk it up.


## Coding Style Changes

We would like to have **nanoFramework** in full conformance with the style guidelines described here [C/C++ Coding Style](cxx-coding-style.md) and here [C# Coding Style](cs-coding-style.md). We plan to do that with tooling, in a holistic way. In the meantime, please:

* **DO NOT** send PRs for style changes.
* **DO** give priority to the current style of the project or file you're changing even if it diverges from the general guidelines.


## Commit Messages

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

Also do your best to factor commits appropriately, i.e. not too large with unrelated
things in the same commit, and not too small with the same small change applied N
times in N different commits. If there was some accidental reformatting or whitespace
changes during the course of your commits, please rebase them away before submitting
the PR.


### Signing off your commit messages

We recommend (although is not mandatory) that you include a `Signed-off-by` line in the commit message:

```
Signed-off-by: Joe Smith <joe.smith@email.com>
```

The project requires that the name used is your real name. Neither anonymous contributions nor those utilizing pseudonyms will be accepted.


## Contributor License Agreement

### Why a CLA?

The Contributor License Agreement helps ensure everyone that **nanoFramework** is here to stay.
Specifically, our Contributor License Agreements (CLAs) grant the contributor and **nanoFramework** joint copyright interest in contributed code. Further, it provides assurance from the contributor that contributions are original work that does not violate any third-party license agreement. The agreement between contributors and project is explicit, so developers and users can be confident in the legal status of the source code and their right to use it.

### Our CLA's

All contributions to **nanoFramework** (no matter if that's code, bug fixes, configuration changes, documentation, or anything elase) requires that the contributor(s) complete and sign a Contributor License Agreement. You can read it [here](cla.md).


**nanoFramework** team and community members will provide feedback on your change. Community feedback is highly valued. You will often see the absence of team feedback if the community has already provided good review feedback. 


## PR Feedback

**nanoFramework** team and community members will provide feedback on your change. Community feedback is highly valued. You will often see the absence of team feedback if the community has already provided good review feedback. 

One or more **nanoFramework** team members will review every PR prior to merge. They will often reply with "LGTM, modulo comments". That means that the PR will be merged once the feedback is resolved. "LGTM" == "looks good to me".

There are lots of thoughts and [approaches](https://github.com/antlr/antlr4-cpp/blob/master/CONTRIBUTING.md#emoji) for how to efficiently discuss changes. It is best to be clear and explicit with your feedback. Please be patient with people who might not understand the finer details about your approach to feedback.
Also don't think that comments and requests for changes means that your contribution is not appreciated and people can be stalling or discouraging you. You may have done a wonderfull job on the task at hand but, as it's still part of a very large sofware project, there could be implications on aspects that you might not be aware of, or that it's impacting or causing side effects on other parts. Keep an open mind and positive attitude! :wink:

**nanoFramework** project uses many labels for categorizing issues and pull requests. Check [here](labels.md) the full list.


## Working on an open issue

When you want to work on an open issue (including _up-for-grabs_) we recommend the following.

- Issues labeled with [_investigating_](labels.md#investigating): if the current status doesn't seem updated or clear, add a comment asking for clarification before start any work on it.
- Issues labeled with [_under-review_](labels.md#under-review): if the current status doesn't seem updated or clear, add a comment asking for a clarification before start any work on it.
- Issues labeled with [_up-for-grabs_](labels.md#up-for-grabs): add a comment stating your interest and the issue will be assigned to you and the label switched to _in progress_.


## Suggested Workflow

We use and recommend the following workflow:

1. Create an issue for your work. 
    - You can skip this step for trivial changes.
    - Reuse an existing issue on the topic, if there is one.
    - Get agreement from the team and the community that your proposed change is a good one.
    - If your change adds a new API, follow the [API Review Process](api-review-process.md). 
    - Clearly state that you are going to take on implementing it, if that's the case. You can request that the issue be assigned to you. Note: The issue filer and the implementer don't have to be the same person.

2. Create a personal fork of the repository on GitHub (if you already have one you can jump straight to step 5 bellow).
    
      Forking the repository is a simple click on the "Fork" button (at the top right corner) on the repositories page in GitHub.

3. Clone that new fork to your local system.
      
    This operation depends heavily on what local client you are going to use in order to manage your local clone. There are a number of clients, from Git command line to more sophisticated and GUI clients.
    
    - GitHub has it's own [desktop client](https://desktop.github.com/).
    - There is an extension for [Visual Studio](https://marketplace.visualstudio.com/items?itemName=GitHub.GitHubExtensionforVisualStudio).
    - Visual Studio Code has it's owned Git client baked in. 
    -  There is also the popular [Tower](https://www.git-tower.com/) and many others.
    
    If you are using a GUI client don't bother with the the git command lines shown bellow.

    Cloning locally is a simple click on the green "Clone or Download" button (at the top right corner) that shows on your personal fork in GitHub.

    You can also perform this operation localy. Directly from your Git client or from the git command line:

    `git clone https://github.com/<your-github-id-here>/<nf-repo-name-here>.git`

4. Configure a remote upstream to the master repository.

    `git remote add upstream https://github.com/nanoframework/<nf-repo-name-here>.git`

5. Make sure that your develop branch is in sync with the master  **develop** branch.

    `git checkout develop`
    
    `git pull upstream develop`

6. Create a branch off of **develop** branch.
    
    `git checkout -b <branch-name-here> develop`
  
    We suggest that you name the branch so that it clearly communicates your intentions, such as *issue-123* or *githubhandle-issue*.
    Don't use a branch name starting with _develop_ because that may be mistaken with the _develop_ branches on the master repository.
    
    Branches are useful since they isolate your changes from incoming changes from upstream. They also enable you to create multiple PRs from the same fork.

7. Work your way through the changes and commit them using your Git client or the command line as you prefer.
      - Please follow our [Commit Messages](contributing-workflow.md#commit-messages) guidance.
      - Include `Signed-off-by` line, e.g. `git commit -s`

8. Add new tests corresponding to your change, if applicable.

9. Build the repository with your changes.
      - Make sure that the builds are clean.
      - Make sure that the tests are all passing, including any new tests that you've added.

10. Push your changes to your fork on GitHub (if you haven't already).

    `git push origin <branch-name-here>`

11. Create a pull request (PR) against the upstream repository's **develop** branch.
      
    Creating a PR is a simple click on the "Pull Request" button that shows on your personal fork in GitHub.

    There is a template for the PR message. We ask you to follow it. It has the required topics and placeholders for what is required to make it clear. Also acts as a check list for you as the submitter.

    When starting a PR GitHub will show you if you repo is up to date with the master one and if a merge is OK. If there are differences showing you have to go back to you local clone and merge those into your local clone. After doing that it's advisable to re-run the build and tests because there could have been changed brought in that affected your code.
    After the above succeeds you have to push the changes up to origin repeating step 10 above.

Note 1: It is OK for your PR to include a large number of commits. If that's the case, once your change is accepted, you can be asked to squash your commits into one or some appropriately small number of commits before your PR is merged.

Note 2: It is OK to create your PR as "[WIP]" on the upstream repo before the implementation is done. This can be useful if you'd like to start the feedback process concurrent with your implementation. State that this is the case in the initial PR comment.

Note 3: If you are working on a feature that has high impact or it's something experimental, your original PR can have it's target branch moved into a new develop branch in the master repo, something like *develop-shiny-awesome-feature*.


## General git resources

If you are coming from another version control system *git* can feel daunting, awkward, confusing and may cause you frustration. :warning: Be warned about that! :warning: :stuck_out_tongue_winking_eye:

We suggest that you go through some basic tutorial and give it a try on a test repo that you setup for yourself.

Here are a few resources that we've compiled to get you up to speed. No claims that these are, by any stretch, the only or the better ones! You can find a bunch of these out there!

- [GitHub trial site](http://try.github.io/). Gives you a nice tour of git. Get your feet wet without even installing software!

- [GitHub help page](http://help.github.com/) Deals with basic usage, concepts and terms of git and github. Good to get a first idea.

- [Git Reference](http://git.github.io/git-reference/). Nice and concise reference of the essential functions of git. Takes about 30min to read through, you'll come out smarter at the end.

- The git [community book](https://git-scm.com/book/en/v2). This book is meant to help you learn how to use Git as quickly and easily as possible.

- [Escape a git mess step-by-step](http://justinhileman.info/article/git-pretty/git-pretty.png). Humorous and handy workflow to help you when you get stuck with git and your blood pressure starts to rise.
