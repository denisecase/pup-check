"""Python package structure checks."""

from pup_core.base.types import RepositoryContext

from pup_check.base.types import CheckResult

__all__ = ["check_package_structure"]


def check_package_structure(context: RepositoryContext) -> CheckResult:
    """Check that a src/ repository contains a detectable Python package."""
    has_src = "src" in context.files or "src/" in context.files

    if not has_src:
        return CheckResult(
            name="package structure",
            passed=True,
            detail="no src/ layout detected; check not applicable",
        )

    if context.src_package:
        return CheckResult(
            name="package structure",
            passed=True,
            detail=f"detected package {context.src_package}",
        )

    return CheckResult(
        name="package structure",
        passed=False,
        detail="src/ exists but no Python package was detected",
    )
