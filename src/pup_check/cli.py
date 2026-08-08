"""Command-line interface for pup-check.

This module parses arguments and dispatches repository checking behavior.

Commands:
uv run pup-check

Equivalent uvx usage after release:
uvx pup-check
uvx pup-check@latest
"""

import argparse
from collections.abc import Sequence
from pathlib import Path

from pup_check.commands import check

__all__ = ["build_parser", "main"]


def build_parser() -> argparse.ArgumentParser:
    """Build the argument parser."""
    parser = argparse.ArgumentParser(
        prog="pup-check",
        description=(
            "Check a professional Python repository for deterministic "
            "internal consistency."
        ),
    )

    parser.add_argument(
        "--root",
        type=Path,
        default=None,
        help=(
            "Repository root to check. Defaults to the nearest parent "
            "directory containing .git, or the current directory."
        ),
    )

    return parser


def main(argv: Sequence[str] | None = None) -> int:
    """Run the command-line interface.

    Args:
        argv: Optional command-line arguments. If None, uses sys.argv.

    Returns:
        Exit code from the check command.
    """
    parser = build_parser()
    args = parser.parse_args(argv)

    return check.run(
        root=args.root,
    )


if __name__ == "__main__":
    raise SystemExit(main())
