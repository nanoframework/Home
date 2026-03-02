# Scripts

This folder contains maintenance scripts for the .NET **nanoFramework** organization repositories.

## update-nuspec-netnano-tfm.py

Updates nuspec files across all nanoFramework library repositories to use the correct Target Framework Moniker (TFM).

### What it does

For each library repository that has a `develop` branch and a nuspec file at the root:

1. Replaces multiple individual `<file>` entries for binary outputs (`.dll`, `.pdb`, `.pdbx`, `.pe`, `.xml`) with a single wildcard entry using `.*`.
2. Changes the `target` attribute from `lib` or `lib\filename.ext` to `lib\netnano1.0`.

**Before:**
```xml
<file src="nanoFramework.System.Math\bin\Release\System.Math.dll" target="lib\System.Math.dll" />
<file src="nanoFramework.System.Math\bin\Release\System.Math.pdb" target="lib\System.Math.pdb" />
<file src="nanoFramework.System.Math\bin\Release\System.Math.pdbx" target="lib\System.Math.pdbx" />
<file src="nanoFramework.System.Math\bin\Release\System.Math.pe" target="lib\System.Math.pe" />
<file src="nanoFramework.System.Math\bin\Release\System.Math.xml" target="lib\System.Math.xml" />
```

**After:**
```xml
<file src="nanoFramework.System.Math\bin\Release\System.Math.*" target="lib\netnano1.0" />
```

### Requirements

```shell
pip install requests
```

### Usage

```shell
# Process all library repositories (creates PRs):
python update-nuspec-netnano-tfm.py --token <github-personal-access-token>

# Preview changes without modifying any repository:
python update-nuspec-netnano-tfm.py --token <github-personal-access-token> --dry-run

# Process a single repository:
python update-nuspec-netnano-tfm.py --token <github-personal-access-token> --repo System.Math
```

The GitHub token needs `repo` scope to create branches and pull requests.

### Repositories skipped

The following repositories are explicitly excluded (as per the issue specification):

- `Home`
- `nf-interpreter`
- `nanoFramework.IoT.Device`
- `Samples`
- `nf-Community-Targets`
- `nf-VSCodeExtension`
- `nf-Visual-Studio-extension`

Archived repositories and repositories without a `develop` branch are also skipped.
