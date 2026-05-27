# GitHub Copilot Instructions

## Updating Native Assembly Declarations in nf-interpreter
When you are assigned to an issue titled **"Update {LibraryName} declaration"** in this repository, follow the steps below end-to-end. The issue body contains all the specific data you need: old and new values for native version and checksum, a link to the stubs build artifact, and a reference to the originating PR in the class library repository.

---
### 1. Understand the task
You are updating the native assembly declaration for a class library in [nanoframework/nf-interpreter](https://github.com/nanoframework/nf-interpreter). The CI pipeline in the class library repository detected that either the native checksum or the native version changed. It opened this issue to request that the corresponding stub files in nf-interpreter be updated to reflect the new values.
Before doing anything else, read the issue body carefully.

Extract all of the following before touching any file:

- **Library name** — from the issue title (`Update {LibraryName} declaration`)
- **Old checksum** — from the table (`Previously published` column)
- **New checksum** — from the table (`New` column)
- **Old native version** — from the table (`Previously published` column)
- **New native version** — from the table (`New` column)
- **Stubs artifact link** — direct zip URL or Azure DevOps build link in the issue body
- **Originating PR** — the PR in the class library repo that triggered this issue (e.g. `nanoframework/System.Device.Spi#171`)
- **This issue's number** — from the URL of the nf-interpreter issue (e.g. `#NNNN`)

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
- **`Find{LibraryName}.cmake`**: CMake module — **ignore this file**, DO NOT make any changes to it.

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
- Search for the files by **old checksum value**:

```bash
grep -r "0x{oldChecksum}" --include="*.cpp" --include="*.h" .
```

Typically one `.cpp` and one `.h` file under `src/` or `targets/`.
There will usually be one `.cpp` file and one `.h` file per library. The artifact may also contain a `.cmake` file — IGNORE IT.

---
### 5. Update the `.cpp` file — three changes required

#### 5a. Update `method_lookup[]` array (CRITICAL — most commonly missed)

The `method_lookup[]` array encodes the exact position of every managed method. A single wrong entry (including a misplaced `nullptr`) will cause runtime dispatch failures.

**Diff the entire array** between the artifact and nf-interpreter:

```bash
diff <artifact>/sys_dev_spi_native.cpp <nf-interpreter>/src/.../sys_dev_spi_native.cpp
```

Replace the nf-interpreter `method_lookup[]` body **exactly** with the artifact's array body. Check for:
- `nullptr` entries added or removed (these shift all subsequent indices)
- Named function entries added, removed, or reordered
- Total entry count (must match the artifact exactly)

For each **new** named function entry (appears in artifact but not in nf-interpreter):
- Add the function body from the artifact `.cpp`
- Add `NANOCLR_NATIVE_DECLARE(...)` in the `.h` file

For each **removed** named function entry (in nf-interpreter but not in artifact):
- Remove the function body **only if it is a stub** (returns `S_OK` / `NANOCLR_SET_AND_LEAVE_HR_VOID(S_OK)` / calls `stack.NotImplementedStub()`)
- If the function contains a real implementation, **do not delete it** — note the discrepancy in the PR description

#### 5b. Update the checksum

```cpp
// Before:
0xOLDCHECKSUM,
// After:
0xNEWCHECKSUM,
```

#### 5c. Update the native version tuple

```cpp
// Before:
{ 100, 2, 0, 0 }
// After:
{ 100, 2, 0, 1 }
```
### 6. Update the `.h` file — apply only additive changes

**CRITICAL RULES — read before touching the header:**

### What TO update:
- Add any new `FIELD___*` constants present in the artifact but missing in nf-interpreter
- Add any new `NANOCLR_NATIVE_DECLARE(...)` entries present in the artifact but missing in nf-interpreter
- Add any new struct blocks, enums, or typedefs that exist in the artifact but not in nf-interpreter

### What NOT to change:
- **Do NOT uncomment code** that is intentionally commented out. Comments such as `// moved to src/PAL/...` indicate deliberate decisions — if code is commented out in nf-interpreter but appears active in the artifact, preserve the commented-out form in nf-interpreter.
- **Do NOT remove helper method declarations** (e.g. `static HRESULT NativeTransfer(CLR_RT_StackFrame &stack, bool bufferIs16bits);`) that exist in nf-interpreter but not in the artifact. These declarations support real implementations in the `.cpp` file.
- **Do NOT remove** `#include` directives, `extern` references, or any other local additions that are absent from the artifact. They exist to support platform-specific implementations.
- **Do NOT remove** commented-out blocks or documentation comments.

> **Rule of thumb**: When the artifact `.h` is a *subset* of the nf-interpreter `.h` (artifact has less content), the correct action is to leave the extra content in place and only add what is genuinely new. When the artifact `.h` has *more* content (new entries), add only those new entries.

---

### 7. Pre-commit checklist

Before committing, verify **all** of the following:

- [ ] `method_lookup[]` entry count matches the artifact exactly
- [ ] `method_lookup[]` entry order matches the artifact exactly (every `nullptr` and named entry at the correct index)
- [ ] Checksum hex value updated to match the new value from the issue
- [ ] Version tuple updated to match the new value from the issue
- [ ] No existing real C++ function bodies were deleted
- [ ] No intentionally commented-out code was uncommented
- [ ] No local helper declarations were removed from `.h`
- [ ] All new named function entries have a corresponding function body in `.cpp`
- [ ] All new named function entries have a corresponding `NANOCLR_NATIVE_DECLARE(...)` in `.h`

---
### 7. Open a PR against nf-interpreter
Use the [nf-interpreter PR template](https://github.com/nanoframework/nf-interpreter/blob/main/.github/PULL_REQUEST_TEMPLATE.md) **verbatim**. Copy the block below exactly, substituting the `{...}` placeholders. Do not write a custom description — GitHub will not auto-fill the template for PRs opened via CLI or API.

**Title:**
```
Update {LibraryName} native declaration to v{newNativeVersion}
```

**Body — use the PR template exactly:**
```markdown
## Description
- Updated `{LibraryName}` native assembly declaration.
- Checksum: `{oldChecksum}` → `{newChecksum}`.
- Native version: `{oldNativeVersion}` → `{newNativeVersion}`.
- `method_lookup[]`: updated to match artifact (entry count changed).

## Motivation and Context
Resolves nanoFramework/nf-interpreter#{issueNumber}
Triggered by nanoframework/{ClassLibraryRepo}#{PR-number}

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
## Common mistakes to avoid

| Mistake | Correct behaviour |
|---|---|
| Uncommenting code that is intentionally commented out in nf-interpreter | Preserve the commented-out form; only add genuinely new content |
| Removing `static HRESULT Helper(...)` declarations from `.h` | Keep them — they support real implementations in `.cpp` |
| Updating only the checksum/version and skipping `method_lookup[]` | Always diff and update the complete `method_lookup[]` array |
| Copying the artifact `.h` verbatim over the nf-interpreter `.h` | Merge: add new entries, preserve all existing nf-interpreter content |
| Removing function body implementations from `.cpp` | Only remove stubs; never delete real implementations |
| Writing a custom PR description instead of following the template | Always use the template from this guide verbatim |
