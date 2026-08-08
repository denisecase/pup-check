"""Repository file checks."""

from pup_core.base.types import RepositoryContext

from pup_check.base.types import CheckResult

__all__ = ["check_required_files"]


def check_required_files(context: RepositoryContext) -> tuple[CheckResult, ...]:
    """Check required project files."""
    required_files = ("pyproject.toml",)

    results: list[CheckResult] = []

    for path in required_files:
        exists = path in context.files

        results.append(
            CheckResult(
                name=f"file {path}",
                passed=exists,
                detail="exists" if exists else "missing",
            )
        )

    return tuple(results)
