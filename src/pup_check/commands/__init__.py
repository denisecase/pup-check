"""Command modules.

Each command module exposes a stable run(...) -> int entry point.

The CLI parser lives in pup_check.cli.
Behavior lives here.
"""

from pup_check.commands import check

__all__ = ["check"]
