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
curl -L -o stubs.zip "<url from issue body>"
unzip stubs.zip -d ./stubs
```

**Option 2 — Azure CLI**

The issue body also contains a ready-to-run `az pipelines runs artifact download` command. Copy it from the issue and run it directly. It requires the `azure-devops` CLI extension and that you are already signed in (`az login`):

```bash
az extension add --name azure-devops   # if not already installed
az pipelines runs artifact download --run-id <buildId> --artifact-name stubs --path ./stubs --org https://dev.azure.com/nanoframework --project "<project>"
```

The artifact contains a `Stubs/<LibraryName>/` subfolder with the `.cpp`, `.h`, and `.cmake` files.

Do NOT generate, infer, or modify the stub files. Use exactly what is in the artifact — these files were produced by the CI pipeline and are the authoritative source of truth for the new declarations.

---

### 3. Clone and branch nf-interpreter

Clone [nanoframework/nf-interpreter](https://github.com/nanoframework/nf-interpreter). Choose the base branch as follows:

- If the **originating PR** (in the class library repo) targets **`main`** — branch off `main` in nf-interpreter. This corresponds to a stable/release build.
- If the **originating PR** targets **`develop`** — branch off `develop` in nf-interpreter. This corresponds to a preview build.

Name your branch:

```
nfbot/update-native/{LibraryName}
```

Do not commit directly to `main` or `develop`.

---

### 4. Find the files to update

Search the nf-interpreter repository for the files that correspond to the library. They are typically located under `src/` or `targets/`. Use one or both of the following strategies:

- Search for files whose names match the pattern `{LibraryName}_<something>.cpp` / `.h` / `.cmake`.
- Search file contents for the **old checksum value** shown in the issue table — this reliably identifies the files that need updating.

There will usually be one `.cpp` file and one `.h` file per library. The artifact may also contain a `.cmake` file — ignore it.

---

### 5. Merge the stub files into nf-interpreter

For **each `.cpp` and `.h` file** in the artifact, find its matching file in nf-interpreter by name, then apply the following updates:

- **Checksum**: replace the old checksum with the new value from the issue table.
- **Native version**: replace the old version with the new value. The nanoFramework C format for a version is a four-element initializer list — for example, version `1.5.0.0` is written as `{ 1, 5, 0, 0 }`.

Ignore any `.cmake` files that may be present in the artifact — no changes are needed to CMake files in nf-interpreter.

**Critical rule — do not remove existing declarations**: Do NOT delete or overwrite any existing `static` method or field declarations that are already present in the nf-interpreter files, even if those declarations are absent from the artifact stubs. Merge in any new or changed function signatures or bodies from the artifact, but preserve everything that is already there.

---

### 6. Open a PR against nf-interpreter

Use the [nf-interpreter PR template](https://github.com/nanoframework/nf-interpreter/blob/main/.github/PULL_REQUEST_TEMPLATE.md) exactly. Fill it in as follows:

**Title**
```
Update {LibraryName} native declaration to v{newNativeVersion}
```

**Description**
A bulleted list of what changed, for example:
- Updated `{LibraryName}` native assembly declaration.
- Checksum: `{oldChecksum}` → `{newChecksum}`.
- Native version: `{oldNativeVersion}` → `{newNativeVersion}`.

**Motivation and Context**
```
Resolves nanoFramework/Home#NNNN
Triggered by {originating-repo}#{PR-number}
```

Replace `NNNN` with the issue number from this Home repository, and `{originating-repo}#{PR-number}` with the originating class library PR reference from the issue body.

**How Has This Been Tested?**
State that the stub files were taken directly from the CI pipeline artifact without modification.

**Types of changes**
Check **only** the `Dependencies/declarations` checkbox. Leave all other checkboxes unchecked.

**Checklist**
Tick only the boxes that genuinely apply to this change.

---

### 7. Close the issue

The `Resolves nanoFramework/Home#NNNN` reference in the PR description will automatically close this Home issue when the nf-interpreter PR is merged. No separate action is needed.

---

### Important constraints

- **Never** regenerate stub files — always use the artifact downloaded from the CI pipeline link in the issue body.
- **Never** delete existing `static` declarations from nf-interpreter files.
- The PR must target **`nanoframework/nf-interpreter`**, not the originating class library repository.
- Always work on a feature branch and open a PR — never push directly to `main` or `develop`.
- The base branch in nf-interpreter (`main` vs `develop`) must match the target branch of the originating PR in the class library repo — check the originating PR link in the issue body to determine this.
- The Home issue number and the originating PR link are both in the issue body — read them carefully before starting.
