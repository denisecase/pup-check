"""Typed records."""

from dataclasses import dataclass

__all__ = ["CheckResult"]


@dataclass(frozen=True)
class CheckResult:
    """Result of one deterministic repository consistency check."""

    name: str
    passed: bool
    detail: str
