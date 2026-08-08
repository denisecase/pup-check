"""pyproject.toml consistency checks."""

from pathlib import Path

from pup_core.base.errors import PyprojectError
from pup_core.inspect.pyproject import inspect_pyproject

from pup_check.base.types import CheckResult

__all__ = ["check_pyproject"]


def check_pyproject(root: Path) -> CheckResult:
    """Check that pyproject.toml can be read and identifies the project."""
    try:
        info = inspect_pyproject(root)
    except PyprojectError as exc:
        return CheckResult(
            name="pyproject.toml",
            passed=False,
            detail=str(exc),
        )

    if not info.project_name:
        return CheckResult(
            name="pyproject.toml",
            passed=False,
            detail="project.name is missing",
        )

    return CheckResult(
        name="pyproject.toml",
        passed=True,
        detail=f"project name is {info.project_name}",
    )
