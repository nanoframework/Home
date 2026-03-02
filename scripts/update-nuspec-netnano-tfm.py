#!/usr/bin/env python3
"""
Script to update nanoFramework library nuspec files to use the correct TFM.

Changes made to each nuspec file:
- Library files (DLL, PDB, PDBX, PE, XML) are placed under "lib\\netnano1.0"
  instead of the old "lib" or "lib\\filename.ext" targets.
- Multiple individual file entries are consolidated into a single wildcard
  entry using ".*" instead of separate entries per extension.

Example transformation:
  Before:
    <file src="nanoFramework.System.Math\\bin\\Release\\System.Math.dll" target="lib\\System.Math.dll" />
    <file src="nanoFramework.System.Math\\bin\\Release\\System.Math.pdb" target="lib\\System.Math.pdb" />
    <file src="nanoFramework.System.Math\\bin\\Release\\System.Math.pdbx" target="lib\\System.Math.pdbx" />
    <file src="nanoFramework.System.Math\\bin\\Release\\System.Math.pe" target="lib\\System.Math.pe" />
    <file src="nanoFramework.System.Math\\bin\\Release\\System.Math.xml" target="lib\\System.Math.xml" />

  After:
    <file src="nanoFramework.System.Math\\bin\\Release\\System.Math.*" target="lib\\netnano1.0" />

Usage:
    python update-nuspec-netnano-tfm.py --token <github-personal-access-token>
    python update-nuspec-netnano-tfm.py --token <token> --dry-run
    python update-nuspec-netnano-tfm.py --token <token> --repo System.Net
"""

import argparse
import base64
import re
import sys
import time
from collections import defaultdict
from typing import Optional

try:
    import requests
except ImportError:
    print("Please install the 'requests' library: pip install requests")
    sys.exit(1)

# Repositories to skip (explicitly excluded by the issue)
SKIP_REPOS = {
    'Home',
    'nf-interpreter',
    'nanoFramework.IoT.Device',
    'Samples',
    'nf-Community-Targets',
    'nf-VSCodeExtension',
    'nf-Visual-Studio-extension',
}

GITHUB_API = 'https://api.github.com'
ORG = 'nanoframework'
BRANCH_NAME = 'update-nuspec-netnano-tfm'
PR_TITLE = 'Update nuspec to place library under nano TFM'
PR_BODY = (
    '## Summary\n\n'
    'Update nuspec file(s) to use the correct Target Framework Moniker (TFM):\n\n'
    '- Place library files (DLL, PDB, PDBX, PE, XML) under `lib\\netnano1.0` '
    'instead of `lib` or `lib\\filename.ext`.\n'
    '- Consolidate multiple individual file entries into a single wildcard entry '
    'using `.*` (e.g., `System.Math.*`) instead of separate entries per extension.\n\n'
    'Relates to: nanoframework/Home#609\n'
)
COMMIT_MESSAGE = 'Update nuspec to place library under nano TFM (netnano1.0)'


def get_headers(token: str) -> dict:
    return {
        'Authorization': f'token {token}',
        'Accept': 'application/vnd.github.v3+json',
    }


def list_repos(token: str) -> list:
    """List all non-archived repos in the nanoframework org."""
    headers = get_headers(token)
    repos = []
    page = 1
    while True:
        resp = requests.get(
            f'{GITHUB_API}/orgs/{ORG}/repos',
            headers=headers,
            params={'per_page': 100, 'page': page, 'type': 'public'},
        )
        resp.raise_for_status()
        data = resp.json()
        if not data:
            break
        for repo in data:
            if repo.get('archived', False):
                continue
            if repo['name'] in SKIP_REPOS:
                continue
            repos.append(repo)
        if len(data) < 100:
            break
        page += 1
        time.sleep(0.5)
    return repos


def has_develop_branch(token: str, repo_name: str) -> bool:
    """Check if repo has a develop branch."""
    headers = get_headers(token)
    resp = requests.get(
        f'{GITHUB_API}/repos/{ORG}/{repo_name}/branches/develop',
        headers=headers,
    )
    return resp.status_code == 200


def get_nuspec_files(token: str, repo_name: str, ref: str = 'develop') -> list:
    """Get list of nuspec files at repo root on the given branch."""
    headers = get_headers(token)
    resp = requests.get(
        f'{GITHUB_API}/repos/{ORG}/{repo_name}/contents/',
        headers=headers,
        params={'ref': ref},
    )
    if resp.status_code != 200:
        return []
    return [f for f in resp.json() if isinstance(f, dict) and f.get('name', '').endswith('.nuspec')]


def update_nuspec_content(content: str) -> Optional[str]:
    """
    Update nuspec content to use lib\\netnano1.0 TFM and wildcard file references.

    Finds all <file> entries in the <files> section that reference binary output
    files (dll, pdb, pdbx, pe, xml) from a Release build path, and replaces
    multiple per-extension entries with a single wildcard entry targeting
    lib\\netnano1.0.

    Returns updated content string, or None if no changes are needed.
    """
    # Pattern to match a library file entry in a Release build output path
    lib_entry_re = re.compile(
        r'(?P<indent>[ \t]*)'
        r'<file\s+src="(?P<path>[^"]+\\bin\\Release\\)(?P<name>[^"\\]+)'
        r'\.(?P<ext>dll|pdb|pdbx|pe|xml)"'
        r'\s+target="[^"]*"\s*/>'
        r'[ \t]*(?:\r\n|\r|\n)',
        re.IGNORECASE,
    )

    matches = list(lib_entry_re.finditer(content))
    if not matches:
        return None

    # Group matches by (path, name) to handle multiple libraries in one nuspec
    groups: dict = defaultdict(list)
    for m in matches:
        key = (m.group('path'), m.group('name'))
        groups[key].append(m)

    # Check whether any group actually needs updating
    needs_update = False
    for (path, name), group_matches in groups.items():
        if len(group_matches) > 1:
            needs_update = True
            break
        # Single entry: check if it already uses wildcard and netnano1.0 target
        m = group_matches[0]
        original_line = m.group(0)
        if '.*"' not in original_line or 'netnano1.0' not in original_line:
            needs_update = True
            break

    if not needs_update:
        return None

    # Detect dominant line ending in the file
    crlf_count = content.count('\r\n')
    lf_count = content.count('\n') - crlf_count
    eol = '\r\n' if crlf_count >= lf_count else '\n'

    # Rebuild content by processing from the end of the string to preserve offsets
    new_content = content
    for (path, name), group_matches in sorted(
        groups.items(), key=lambda item: -item[1][0].start()
    ):
        if not group_matches:
            continue

        first_m = min(group_matches, key=lambda m: m.start())
        last_m = max(group_matches, key=lambda m: m.start())

        indent = first_m.group('indent')
        replacement = f'{indent}<file src="{path}{name}.*" target="lib\\netnano1.0" />{eol}'

        start = first_m.start()
        end = last_m.end()
        new_content = new_content[:start] + replacement + new_content[end:]

    if new_content == content:
        return None
    return new_content


def get_branch_sha(token: str, repo_name: str, branch: str) -> Optional[str]:
    """Return the HEAD commit SHA of a branch."""
    headers = get_headers(token)
    resp = requests.get(
        f'{GITHUB_API}/repos/{ORG}/{repo_name}/branches/{branch}',
        headers=headers,
    )
    if resp.status_code == 200:
        return resp.json()['commit']['sha']
    return None


def create_branch(token: str, repo_name: str, branch_name: str, base_sha: str) -> bool:
    """Create a new branch from the given SHA. Returns True on success."""
    headers = get_headers(token)
    resp = requests.post(
        f'{GITHUB_API}/repos/{ORG}/{repo_name}/git/refs',
        headers=headers,
        json={
            'ref': f'refs/heads/{branch_name}',
            'sha': base_sha,
        },
    )
    return resp.status_code == 201


def update_file_in_repo(
    token: str,
    repo_name: str,
    file_path: str,
    new_content: str,
    file_sha: str,
    branch: str,
    message: str,
) -> bool:
    """Update a file in the repo. Returns True on success."""
    headers = get_headers(token)
    encoded = base64.b64encode(new_content.encode('utf-8')).decode('ascii')
    resp = requests.put(
        f'{GITHUB_API}/repos/{ORG}/{repo_name}/contents/{file_path}',
        headers=headers,
        json={
            'message': message,
            'content': encoded,
            'sha': file_sha,
            'branch': branch,
        },
    )
    return resp.status_code in (200, 201)


def create_pull_request(
    token: str,
    repo_name: str,
    head_branch: str,
    base_branch: str,
    title: str,
    body: str,
) -> Optional[str]:
    """Create a pull request. Returns the PR URL on success, None otherwise."""
    headers = get_headers(token)
    resp = requests.post(
        f'{GITHUB_API}/repos/{ORG}/{repo_name}/pulls',
        headers=headers,
        json={
            'title': title,
            'body': body,
            'head': head_branch,
            'base': base_branch,
        },
    )
    if resp.status_code == 201:
        return resp.json()['html_url']
    print(f'  PR creation failed: {resp.status_code} {resp.text[:200]}')
    return None


def get_file_sha(token: str, repo_name: str, file_path: str, ref: str) -> Optional[str]:
    """Get the blob SHA of a file (needed for updating it via the API)."""
    headers = get_headers(token)
    resp = requests.get(
        f'{GITHUB_API}/repos/{ORG}/{repo_name}/contents/{file_path}',
        headers=headers,
        params={'ref': ref},
    )
    if resp.status_code == 200:
        return resp.json()['sha']
    return None


def process_repo(token: str, repo_name: str, dry_run: bool = False) -> bool:
    """
    Process a single repo: find nuspec files, apply updates, create PR.
    Returns True if a PR was created (or would be created in dry-run mode).
    """
    print(f'\nProcessing {repo_name}...')

    if not has_develop_branch(token, repo_name):
        print('  No develop branch, skipping.')
        return False

    nuspec_files = get_nuspec_files(token, repo_name)
    if not nuspec_files:
        print('  No nuspec files found at root, skipping.')
        return False

    print(f'  Found {len(nuspec_files)} nuspec file(s).')

    updates = []
    for nuspec in nuspec_files:
        file_path = nuspec['path']
        download_url = nuspec['download_url']

        resp = requests.get(download_url)
        if resp.status_code != 200:
            print(f'  Failed to download {file_path}, skipping.')
            continue

        original = resp.text
        updated = update_nuspec_content(original)

        if updated is None:
            print(f'  {file_path}: already up to date.')
            continue

        # Show a diff summary
        orig_lines = set(original.splitlines())
        upd_lines = set(updated.splitlines())
        is_release_line = lambda l: 'bin\\Release' in l or 'bin/Release' in l
        removed = [l for l in orig_lines - upd_lines if is_release_line(l)]
        added = [l for l in upd_lines - orig_lines if is_release_line(l)]
        print(f'  {file_path}: needs update.')
        for line in sorted(removed):
            print(f'    - {line.strip()}')
        for line in sorted(added):
            print(f'    + {line.strip()}')

        updates.append({
            'path': file_path,
            'sha': nuspec['sha'],
            'content': updated,
        })

    if not updates:
        print('  No changes needed.')
        return False

    if dry_run:
        print('  [dry-run] Would create PR with the above changes.')
        return True

    # Get develop branch HEAD SHA
    develop_sha = get_branch_sha(token, repo_name, 'develop')
    if not develop_sha:
        print('  Failed to get develop branch SHA.')
        return False

    # Create the update branch
    print(f'  Creating branch {BRANCH_NAME}...')
    if not create_branch(token, repo_name, BRANCH_NAME, develop_sha):
        print(f'  Branch {BRANCH_NAME} already exists or could not be created.')
        # Try to continue anyway (branch might exist from a previous run)

    # Commit updates to the new branch
    for update in updates:
        # Get fresh blob SHA for the file on the new branch
        file_sha = get_file_sha(token, repo_name, update['path'], BRANCH_NAME) or update['sha']
        print(f'  Updating {update["path"]}...')
        if not update_file_in_repo(
            token,
            repo_name,
            update['path'],
            update['content'],
            file_sha,
            BRANCH_NAME,
            COMMIT_MESSAGE,
        ):
            print(f'  Failed to update {update["path"]}.')
            return False

    # Open PR
    print('  Creating pull request...')
    pr_url = create_pull_request(
        token, repo_name, BRANCH_NAME, 'develop', PR_TITLE, PR_BODY
    )
    if pr_url:
        print(f'  PR created: {pr_url}')
        return True

    print('  Failed to create PR.')
    return False


def main() -> None:
    parser = argparse.ArgumentParser(
        description='Update nanoFramework library nuspec files to use lib\\netnano1.0 TFM.',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    parser.add_argument(
        '--token',
        required=True,
        help='GitHub personal access token with repo scope.',
    )
    parser.add_argument(
        '--repo',
        help='Process only this specific repository name (useful for testing).',
    )
    parser.add_argument(
        '--dry-run',
        action='store_true',
        help='Show what would be changed without actually modifying any repository.',
    )
    args = parser.parse_args()

    token = args.token

    if args.repo:
        repos = [{'name': args.repo}]
    else:
        print('Fetching repository list from nanoframework org...')
        repos = list_repos(token)
        print(f'Found {len(repos)} repositories to examine.')

    prs_created = []
    skipped = []

    for repo in repos:
        repo_name = repo['name']
        try:
            result = process_repo(token, repo_name, dry_run=args.dry_run)
            if result:
                prs_created.append(repo_name)
            else:
                skipped.append(repo_name)
        except requests.HTTPError as exc:
            print(f'  HTTP error for {repo_name}: {exc}')
        except (ValueError, KeyError) as exc:
            print(f'  Data error for {repo_name}: {exc}')
        except Exception as exc:  # noqa: BLE001 - log but continue processing other repos
            import traceback
            print(f'  Unexpected error for {repo_name}: {exc}')
            traceback.print_exc()
        time.sleep(1)  # Be polite to the GitHub API

    print('\n' + '=' * 60)
    if args.dry_run:
        print(f'[dry-run] Would create PRs for: {", ".join(prs_created) if prs_created else "none"}')
    else:
        print(f'PRs created for: {", ".join(prs_created) if prs_created else "none"}')
    print(f'Skipped (no changes needed or no develop branch): {len(skipped)} repos')


if __name__ == '__main__':
    main()
