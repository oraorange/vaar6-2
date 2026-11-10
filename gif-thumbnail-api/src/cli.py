"""Command-line entry point for GIF thumbnail generation."""

import argparse
import sys
from pathlib import Path

from src.converter import create_thumbnail


def main() -> int:
    """Parse arguments, convert the GIF, and print the output path."""
    parser = argparse.ArgumentParser(description="GIF to PNG thumbnail")
    parser.add_argument("input", type=Path, help="Input GIF file")
    parser.add_argument("--output", type=Path, help="Output PNG file")
    parser.add_argument("--size", type=int, default=128)
    args = parser.parse_args()
    target = args.output or Path("output") / f"{args.input.stem}.png"
    try:
        result = create_thumbnail(args.input, target, args.size)
    except (OSError, ValueError) as error:
        print(f"Error: {error}", file=sys.stderr)
        return 1
    print(result)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
