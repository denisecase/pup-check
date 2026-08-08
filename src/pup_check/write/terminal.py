"""Terminal reporting."""

from collections.abc import Sequence

from pup_core.base.types import RepositoryContext

from pup_check.base.types import CheckResult

__all__ = ["print_check_results"]


def print_check_results(
    context: RepositoryContext,
    results: Sequence[CheckResult],
) -> None:
    """Print repository check results."""
    print("[pup-check] CHECK")
    print(f"[pup-check] repo: {context.repo_name}")
    print(f"[pup-check] root: {context.root}")
    print("")

    for result in results:
        status = "PASS" if result.passed else "FAIL"
        print(f"{status:5} {result.name}: {result.detail}")

    passed = sum(result.passed for result in results)
    failed = len(results) - passed

    print("")
    print(f"[pup-check] summary: {passed} passed, {failed} failed")
