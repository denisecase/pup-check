# Changelog

<!-- markdownlint-disable MD024 -->

All notable changes to this project will be documented in this file.

The format is based on **[Keep a Changelog](https://keepachangelog.com/en/1.1.0/)**
and this project adheres to **[Semantic Versioning](https://semver.org/spec/v2.0.0.html)**.

---

## [Unreleased]

- updated pyproject.toml build section and keywords
- added pup and updated docs/

---

## [0.0.4] - 2026-08-08

### Added

- Initial release of `pup-check`.
- Added professional Python repository consistency checking.
- Added repository and project metadata inspection using `pup-core`.
- Added checks for Python package structure and declared project entry-point modules.
- Added concise terminal reporting with a successful or failed check result.

---

## Notes on Versioning and Releases

- We use **SemVer**:
  - **MAJOR** - breaking changes
  - **MINOR** - backward-compatible additions
  - **PATCH** - fixes, documentation, tooling
- Versions are driven by git tags.
- Tag `vX.Y.Z` to release.
- Docs are deployed per version tag and aliased to **latest**.

## Release Procedure

Follow these steps when creating a new release.

### Task 1. Update release metadata

1. Update `CITATION.cff`: change `version` and `date-released`
2. Update `CHANGELOG.md`: move from unreleased, add entry, update links
3. Update `pyproject.toml`: update `[tool.hatch.version] fallback-version`

### Task 2. Validate

````shell
uv lock --upgrade
uv sync --upgrade
uv run pre-commit install

uv run pup-check

git add -A
uv run pre-commit run --all-files
# rerun if changes made
uv run pre-commit run --all-files

uv run python -m pytest
uv run python -m pyright
uv run python -m zensical build

uv run python -c "import shutil; from pathlib import Path; shutil.rmtree(Path('dist'), ignore_errors=True)"

uv build
uvx twine check dist/*
```

### Task 4. Commit, push, tag

```shell
git add -A
git commit -m "Prepare X.Y.Z"
git push -u origin main
````

Verify actions run on GitHub. After success:

```shell
git tag vX.Y.Z -m "X.Y.Z"
git push origin vX.Y.Z
```

## Only As Needed (delete a tag)

```shell
git tag -d vX.Z.Y
git push origin :refs/tags/vX.Z.Y
```

## Links

[Unreleased]: https://github.com/denisecase/pup-up/compare/v0.0.4...HEAD
[0.0.4]: https://github.com/denisecase/pup-up/releases/tag/v0.0.4

<!-- markdownlint-enable MD024 -->
