"""Project entry-point checks."""

from pathlib import Path

from pup_core.base.errors import PyprojectError
from pup_core.inspect.packages import module_exists
from pup_core.inspect.pyproject import inspect_pyproject

from pup_check.base.types import CheckResult

__all__ = ["check_entry_points"]


def check_entry_points(root: Path) -> tuple[CheckResult, ...]:
    """Check that declared project-script modules exist."""
    try:
        info = inspect_pyproject(root)
    except PyprojectError:
        return ()

    if not info.scripts:
        return (
            CheckResult(
                name="entry points",
                passed=True,
                detail="no project scripts declared",
            ),
        )

    results: list[CheckResult] = []

    for script_name, target in sorted(info.scripts.items()):
        module_name, separator, function_name = target.partition(":")

        if not separator or not module_name or not function_name:
            results.append(
                CheckResult(
                    name=f"entry point {script_name}",
                    passed=False,
                    detail=f"invalid target {target}",
                )
            )
            continue

        exists = module_exists(root, module_name)

        results.append(
            CheckResult(
                name=f"entry point {script_name}",
                passed=exists,
                detail=(
                    f"{target} module exists"
                    if exists
                    else f"{target} module not found"
                ),
            )
        )

    return tuple(results)
