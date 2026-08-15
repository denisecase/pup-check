# pup-check: Professional Python Project: Repo Self Consistency Checker

[![PyPI](https://img.shields.io/pypi/v/pup-check?logo=pypi&label=pypi)](https://pypi.org/project/pup-check/)
[![Docs Site](https://img.shields.io/badge/docs-site-blue?logo=github)](https://pup-pack.github.io/pup-check/)
[![Repo](https://img.shields.io/badge/repo-GitHub-black?logo=github)](https://github.com/pup-pack/pup-check)
[![Python 3.15](https://img.shields.io/badge/python-3.15%2B-blue?logo=python)](./pyproject.toml)
[![License](https://img.shields.io/badge/license-MIT-yellow.svg)](./LICENSE)

[![CI](https://github.com/pup-pack/pup-check/actions/workflows/ci-python-zensical.yml/badge.svg?branch=main)](https://github.com/pup-pack/pup-check/actions/workflows/ci-python-zensical.yml)
[![Docs-Deploy](https://github.com/pup-pack/pup-check/actions/workflows/deploy-zensical.yml/badge.svg?branch=main)](https://github.com/pup-pack/pup-check/actions/workflows/deploy-zensical.yml)
[![Pre-Release](https://github.com/pup-pack/pup-check/actions/workflows/pre-release.yml/badge.svg?branch=main)](https://github.com/pup-pack/pup-check/actions/workflows/pre-release.yml)
[![Release](https://github.com/pup-pack/pup-check/actions/workflows/release-pypi.yml/badge.svg)](https://github.com/pup-pack/pup-check/actions/workflows/release-pypi.yml)
[![Links](https://github.com/pup-pack/pup-check/actions/workflows/links.yml/badge.svg?branch=main)](https://github.com/pup-pack/pup-check/actions/workflows/links.yml)
[![Dependabot](https://img.shields.io/badge/Dependabot-enabled-brightgreen.svg)](https://github.com/pup-pack/pup-check/security)

<img
src="https://raw.githubusercontent.com/pup-pack/pup-check/main/docs/images/pup.png"
alt="pup logo"
width="110">

> Opinionated professional Python repository self-consistency checker

## Purpose

Professional Python repositories contain many declarations that should agree
with one another.

Examples include:

- project and package names
- `src/` package structure
- `pyproject.toml` metadata
- command-line entry points
- Python module paths
- dependency declarations
- Python version declarations
- repository-relative file paths
- workflow and tooling configuration

Small inconsistencies can remain unnoticed until a command, build, test,
documentation workflow, or release fails.

`pup-check` performs deterministic checks for internal repository consistency
and reports problems that should be reviewed.

## Check a Repository

```shell
# check the current repository
uvx pup-check

# check using the latest published version
uvx pup-check@latest
```

A successful check returns exit code `0`.

A failed consistency check returns a nonzero exit code and reports the
detected problem.

## Checks

This release checks:

- `pyproject.toml` exists
- `pyproject.toml` can be read and identifies the project
- a Python package can be detected when a `src/` layout is present
- modules referenced by `[project.scripts]` entry points exist

## Developer Command Reference

<details>
<summary>Show command reference</summary>

### In a machine terminal

Open a machine terminal where you want the project:

```shell
git clone https://github.com/pup-pack/pup-check

cd pup-check
code .
```

### In a VS Code terminal

```shell
uv self update
uv python pin 3.15
uv python install
uv lock --upgrade
uv sync

uv run pre-commit install
uv run pre-commit autoupdate

git add -A
uv run pre-commit run --all-files
# repeat if changes were made
uv run pre-commit run --all-files

# run locally to test
uv run pup-check
uv run pup-check --diff
uv run pup-check --write
uv run pup-check --write .gitattributes .github/.yamllint.yml .github/workflows/links.yml

# types, tests, docs
uv run ty check
uv run python -m pytest
uv run python -m zensical build

# save progress
git add -A
git commit -m "update"
git push -u origin main
```

</details>

## Documentation

- [Documentation](https://pup-pack.github.io/pup-check/)

## Annotations

[.annotations/annotations.md](./.annotations/annotations.md)

## Citation

[CITATION.cff](./CITATION.cff)

## License

[MIT](./LICENSE)
