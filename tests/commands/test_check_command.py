"""Tests for the check command."""

from pathlib import Path

from pytest import CaptureFixture

from pup_check.commands import check


def test_check_command_passes_consistent_repository(
    tmp_path: Path,
    capsys: CaptureFixture[str],
) -> None:
    """A consistent Python repository should pass all initial checks."""
    repo = tmp_path / "example-python-repo"
    repo.mkdir()
    (repo / ".git").mkdir()

    package = repo / "src" / "example_python_repo"
    package.mkdir(parents=True)
    (package / "__init__.py").write_text("", encoding="utf-8")
    (package / "cli.py").write_text(
        "def main() -> int:\n    return 0\n",
        encoding="utf-8",
    )

    (repo / "pyproject.toml").write_text(
        """
[project]
name = "example-python-repo"
version = "0.1.0"

[project.scripts]
example-python-repo = "example_python_repo.cli:main"
""".strip()
        + "\n",
        encoding="utf-8",
    )

    exit_code = check.run(root=repo)

    captured = capsys.readouterr()

    assert exit_code == 0
    assert "[pup-check] CHECK" in captured.out
    assert "[pup-check] repo: example-python-repo" in captured.out
    assert "PASS  file pyproject.toml: exists" in captured.out
    assert "PASS  pyproject.toml: project name is example-python-repo" in captured.out
    assert (
        "PASS  package structure: detected package example_python_repo" in captured.out
    )
    assert (
        "PASS  entry point example-python-repo: "
        "example_python_repo.cli:main module exists"
    ) in captured.out
    assert "[pup-check] summary: 4 passed, 0 failed" in captured.out


def test_check_command_fails_when_src_package_is_missing(
    tmp_path: Path,
    capsys: CaptureFixture[str],
) -> None:
    """A src/ repository without a detectable package should fail."""
    repo = tmp_path / "example-python-repo"
    repo.mkdir()
    (repo / ".git").mkdir()
    (repo / "src").mkdir()

    (repo / "pyproject.toml").write_text(
        """
[project]
name = "example-python-repo"
version = "0.1.0"
""".strip()
        + "\n",
        encoding="utf-8",
    )

    exit_code = check.run(root=repo)

    captured = capsys.readouterr()

    assert exit_code == 1
    assert (
        "FAIL  package structure: src/ exists but no Python package was detected"
        in (captured.out)
    )
    assert "[pup-check] summary:" in captured.out


def test_check_command_fails_when_entry_point_module_is_missing(
    tmp_path: Path,
    capsys: CaptureFixture[str],
) -> None:
    """A declared script whose Python module does not exist should fail."""
    repo = tmp_path / "example-python-repo"
    repo.mkdir()
    (repo / ".git").mkdir()

    package = repo / "src" / "example_python_repo"
    package.mkdir(parents=True)
    (package / "__init__.py").write_text("", encoding="utf-8")

    (repo / "pyproject.toml").write_text(
        """
[project]
name = "example-python-repo"
version = "0.1.0"

[project.scripts]
example-python-repo = "example_python_repo.cli:main"
""".strip()
        + "\n",
        encoding="utf-8",
    )

    exit_code = check.run(root=repo)

    captured = capsys.readouterr()

    assert exit_code == 1
    assert (
        "FAIL  entry point example-python-repo: "
        "example_python_repo.cli:main module not found"
    ) in captured.out


def test_check_command_fails_without_pyproject(
    tmp_path: Path,
    capsys: CaptureFixture[str],
) -> None:
    """A repository without pyproject.toml should fail."""
    repo = tmp_path / "example-python-repo"
    repo.mkdir()
    (repo / ".git").mkdir()

    exit_code = check.run(root=repo)

    captured = capsys.readouterr()

    assert exit_code == 1
    assert "FAIL  file pyproject.toml: missing" in captured.out
    assert "FAIL  pyproject.toml:" in captured.out
