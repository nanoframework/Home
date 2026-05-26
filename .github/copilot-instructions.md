# GitHub Copilot Instructions

## Updating Native Assembly Declarations in nf-interpreter
When you are assigned to an issue titled **"Update {LibraryName} declaration"** in this repository, follow the steps below end-to-end. The issue body contains all the specific data you need: old and new values for native version and checksum, a link to the stubs build artifact, and a reference to the originating PR in the class library repository.

---
### 1. Understand the task
You are updating the native assembly declaration for a class library in [nanoframework/nf-interpreter](https://github.com/nanoframework/nf-interpreter). The CI pipeline in the class library repository detected that either the native checksum or the native version changed. It opened this issue to request that the corresponding stub files in nf-interpreter be updated to reflect the new values.
Before doing anything else, read the issue body carefully and extract:
- **Library name** — from the issue title (`Update {LibraryName} declaration`)
- **Old checksum** — from the table in the issue body
- **New checksum** — from the table in the issue body
- **Old native version** — from the table in the issue body
- **New native version** — from the table in the issue body
- **Stubs artifact link** — a link to an Azure DevOps pipeline artifact named `stubs`
- **Originating PR** — a reference to the PR in the class library repo that triggered this issue (e.g. `nanoframework/nf-System.Math#42`)
- **This issue's number** — from the URL of this Home issue (e.g. `#NNNN`)
---
### 2. Obtain the stub files
The issue body provides two ways to download the `stubs` artifact. Use whichever works in your environment:
**Option 1 — direct zip URL (no authentication, works for public projects)**
The issue body contains a direct URL ending in `&$format=zip`. Download it with:
```bash
curl -L -o /tmp/stubs.zip "<url from issue body>"
unzip /tmp/stubs.zip -d /tmp/stubs
```
**Option 2 — Azure CLI**
The issue body also contains a ready-to-run `az pipelines runs artifact download` command. Copy it from the issue and run it directly. It requires the `azure-devops` CLI extension and that you are already signed in (`az login`):
```bash
az extension add --name azure-devops  # if not already installed
az pipelines runs artifact download --run-id <buildId> --artifact-name stubs --path /tmp/stubs --org https://dev.azure.com/nanoframework --project "<project>"
```
**Option 3 — Azure DevOps REST API (for agents without filesystem zip support)**
If `curl`+`unzip` and the Azure CLI are unavailable, query individual files via the REST API. First, retrieve the artifact manifest to get file IDs:
```
GET https://dev.azure.com/nanoframework/{project}/_apis/build/builds/{buildId}/artifacts?artifactName=stubs&api-version=7.1-preview.5
```
The response JSON contains a `resource.data` field with the root file ID and a `resource.downloadUrl` for the zip. To fetch individual files, use:
```
GET https://dev.azure.com/nanoframework/{project}/_apis/build/builds/{buildId}/artifacts?artifactName=stubs&fileId={blobId}&fileName={filename}&api-version=7.1-preview.5
```
where `{blobId}` is the full blob hash for the file (obtained from the manifest) and `{filename}` is the file name (e.g. `nf_rt_events_native.cpp`).
---
The artifact contains a `Stubs/<LibraryName>/` subfolder with the `.cpp`, `.h`, and `.cmake` files.
Do NOT generate, infer, or modify the stub files. Use exactly what is in the artifact — these files were produced by the CI pipeline and are the authoritative source of truth for the new declarations.
After extracting, inspect the artifact files to understand their structure before comparing with nf-interpreter:
- **`.cpp` file** contains: `#include` directives; the `static const CLR_RT_MethodHandler method_lookup[]` array (one entry per managed method, in declaration order); and the `const CLR_RT_NativeAssemblyData g_CLR_AssemblyNative_...` struct (assembly name, checksum, `method_lookup` reference, native version tuple).
- **`.h` file** contains: enum/typedef declarations; per-class `struct Library_...` definitions with `FIELD__*` integer constants and `NANOCLR_NATIVE_DECLARE(...)` macros; and the `extern` data declaration.
Your goal in step 5 is to make the nf-interpreter files match these artifact files, while preserving any existing local additions (see step 5 critical rules).
---
### 3. Prepare the nf-interpreter branch
Clone [nanoframework/nf-interpreter](https://github.com/nanoframework/nf-interpreter) if you haven't already. Choose the base branch as follows:
- If the **originating PR** (in the class library repo) targets **`main`** — branch off `main` in nf-interpreter. This corresponds to a stable/release build.
- If the **originating PR** targets **`develop`** — branch off `develop` in nf-interpreter. This corresponds to a preview build.
Name your branch:
```
nfbot/update-native/{LibraryName}
```
Do not commit directly to `main` or `develop`.
> **Copilot coding agent note:** When running as a Copilot coding agent, the branch is auto-created and a PR is opened automatically. Before making any commits, verify that the PR's base branch is correct (`main` or `develop` as determined above). If it is wrong, update the PR base branch before proceeding.
---
### 4. Find the files to update
Search the nf-interpreter repository for the files that correspond to the library. They are typically located under `src/` or `targets/`. Use one or both of the following strategies:
- Search for files whose names match the pattern `{LibraryName}_<something>.cpp` / `.h` / `.cmake`.
- Search file contents for the **old checksum value** shown in the issue table — this reliably identifies the files that need updating.
There will usually be one `.cpp` file and one `.h` file per library. The artifact may also contain a `.cmake` file — ignore it.
---
### 5. Merge the stub files into nf-interpreter

Apply **all** of the following updates. Do not stop after updating only the checksum and version — those are necessary but not sufficient.
> ⚠️ **The `method_lookup[]` array is the most critical and most commonly missed update.** The array encodes the exact position of every managed method in the assembly. A single entry added, removed, or reordered — including `nullptr` placeholder entries — will cause runtime method dispatch to fail silently, even if the checksum and version are correct. Always diff the **complete** array, entry by entry, before making edits.
**In the `.cpp` file (three changes required):**
1. **`method_lookup[]` array** — Diff the **entire** `static const CLR_RT_MethodHandler method_lookup[]` array between the artifact `.cpp` and the nf-interpreter `.cpp`. Replace the nf-interpreter array body with the one from the artifact exactly. The diff must account for all of:
   - `nullptr` entries added or removed (these shift every subsequent entry's index)
   - Named function entries added, removed, or reordered
   - Changes to which specific named function appears at a given index (a `nullptr` replaced by a function name, or vice versa)
   - Total entry count (must match exactly)
   Do not assume that only `nullptr` entries changed. Named entries may also have been added, removed, or reordered between versions.
   Then, for every difference in named function entries, also update the corresponding C++ function bodies in the same `.cpp` file:
   - **New entry** (function appears in artifact `method_lookup[]` but not in nf-interpreter): add the new function body from the artifact `.cpp` to nf-interpreter. Also add the corresponding `NANOCLR_NATIVE_DECLARE(...)` line in the `.h` file.
   - **Removed entry** (function in nf-interpreter `method_lookup[]` but absent from artifact): remove the corresponding C++ function body **only if it contains a stub implementation** (e.g. returning `S_OK`, `NANOCLR_SET_AND_LEAVE_HR_VOID(S_OK)`, or similar no-op). If the body contains a real implementation, do **not** delete it — instead note the discrepancy in the PR description for human review.
   - **Reordered entries** (same functions, different order): only the array order changes; no function bodies need to be touched.
2. **Checksum** — Replace the old hex value with the new value from the issue table.
3. **Native version** — Replace the old version tuple with the new one. The C format is a four-element initializer list: e.g. version `1.5.0.0` → `{ 1, 5, 0, 0 }`.
**In the `.h` file (one change required):**
4. **Struct and method declarations** — Diff the artifact `.h` against the nf-interpreter `.h`. Apply every difference: new or removed `FIELD__*` constants, new or removed `NANOCLR_NATIVE_DECLARE(...)` entries, new or removed enum values, new or removed `struct Library_...` blocks.
   > **Note:** The nf-interpreter `.h` may contain additional declarations not present in the artifact — for example, extra `#include` directives, helper method declarations, or additional `extern` references that support the real C++ implementations. **Preserve these additions.** Only ensure that all declarations present in the artifact are also present in nf-interpreter. Do not remove local additions that support existing implementations.
Ignore any `.cmake` files in the artifact — no changes are needed to CMake files in nf-interpreter.
**Critical rules — preserve existing local content:**
- Do NOT delete C++ function body implementations (`Library_...::MethodName(CLR_RT_StackFrame &stack) { ... }`) that exist in the nf-interpreter `.cpp` file. Artifact stubs only contain placeholder bodies; nf-interpreter may contain real implementations. Only add function bodies that are genuinely new (present in artifact but absent in nf-interpreter).
- Do NOT remove additional `#include` directives, helper declarations, or `extern` references present in the nf-interpreter `.h` file that are absent from the artifact `.h`. These exist to support real implementations in the `.cpp` files.
**Pre-commit checklist — verify all of the following before committing:**
- [ ] `method_lookup[]` entry count matches artifact exactly
- [ ] `method_lookup[]` entry order matches artifact exactly (every `nullptr` and named entry at the correct index)
- [ ] No named function entries were overlooked — the diff covered both `nullptr` changes and named function changes
- [ ] Checksum hex value matches artifact
- [ ] Version tuple matches artifact
- [ ] All named function entries added to or removed from `method_lookup[]` have corresponding `.cpp` function body changes
- [ ] All added named function entries have a corresponding `NANOCLR_NATIVE_DECLARE(...)` in the `.h` file
- [ ] No existing real C++ implementations were deleted
---
### 6. Open a PR against nf-interpreter
Use the [nf-interpreter PR template](https://github.com/nanoframework/nf-interpreter/blob/main/.github/PULL_REQUEST_TEMPLATE.md) **verbatim**. Copy the block below exactly, substituting the `{...}` placeholders. Do not write a custom description — GitHub will not auto-fill the template for PRs opened via CLI or API.

**Title:**
```
Update {LibraryName} native declaration to v{newNativeVersion}
```
**Body — copy this exactly and fill in the placeholders:**
```
## Description
- Updated `{LibraryName}` native assembly declaration.
- Checksum: `{oldChecksum}` → `{newChecksum}`.
- Native version: `{oldNativeVersion}` → `{newNativeVersion}`.
- `method_lookup[]`: {add this if any changes were made in the array, no need to list the changes}.

## Motivation and Context
Resolves nanoFramework/Home#{issueNumber}
Triggered by {originating-repo}#{PR-number}

## How Has This Been Tested?
Stub files were taken directly from the CI pipeline artifact without modification.

## Screenshots
_N/A_

## Types of changes
- [ ] Improvement (non-breaking change that improves a feature, code or algorithm)
- [ ] Bug fix (non-breaking change which fixes an issue with code or algorithm)
- [ ] New feature (non-breaking change which adds functionality to code)
- [ ] Breaking change (fix or feature that would cause existing functionality to change)
- [ ] Config and build (change in the configuration and build system, has no impact on code or features)
- [ ] Dev Containers (changes related with Dev Containers, has no impact on code or features)
- [x] Dependencies/declarations (update dependencies or assembly declarations and changes associated, has no impact on code or features)
- [ ] Documentation (changes or updates in the documentation, has no impact on code or features)

## Checklist
- [ ] My code follows the code style of this project (only if there are changes in source code).
- [ ] My changes require an update to the documentation (there are changes that require the docs website to be updated).
- [ ] I have updated the documentation accordingly (the changes require an update on the docs in this repo).
- [x] I have read the [CONTRIBUTING](https://github.com/nanoframework/.github/blob/main/CONTRIBUTING.md) document.
- [ ] I have tested everything locally and all new and existing tests passed (only if there are changes in source code).
```
---
### 7. Close the issue
The `Resolves nanoFramework/Home#NNNN` reference in the PR description will automatically close this Home issue when the nf-interpreter PR is merged. No separate action is needed.
---
### Important constraints
- **Never** regenerate stub files — always use the artifact downloaded from the CI pipeline link in the issue body.
- **Never** delete existing C++ function body implementations from nf-interpreter files unless the corresponding `method_lookup[]` entry was removed from the artifact and the body is a stub.
- **Never** remove additional declarations in nf-interpreter `.h` files that are absent from the artifact — they exist to support real implementations.
- The PR must target **`nanoframework/nf-interpreter`**, not the originating class library repository.
- Always work on a feature branch and open a PR — never push directly to `main` or `develop`.
- The base branch in nf-interpreter (`main` vs `develop`) must match the target branch of the originating PR in the class library repo — check the originating PR link in the issue body to determine this.
- The Home issue number and the originating PR link are both in the issue body — read them carefully before starting.
