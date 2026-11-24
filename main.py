#!/usr/bin/env python3
"""Everyday Wonder, Two Days to Find the Line.

One sentence, at most 200 characters, on a small moment of wonder in
everyday life. The surprise here is a small, concrete scene: a dog
riding the lift like it does this every day. No third-party imports;
the grader runs a bare stdlib Python image.
"""

import os
import sys

# One concrete moment, surprise landing in the final clause.
LINE = (
    "The lift doors opened and a small dog stepped in alone, "
    "pressed no button, and rode down like a commuter who knew "
    "the route by heart."
)

MAX_CHARS = 200


def validate(line: str) -> int:
    """Gate the line the way the scorer does; return its length."""
    chars = len(line)
    if chars < 1 or chars > MAX_CHARS:
        raise ValueError(f"Line must be 1-{MAX_CHARS} characters, got {chars}")
    if "\n" in line or "\r" in line:
        raise ValueError("Line must fit on one line")
    if not line.strip():
        raise ValueError("Line must not be only white space")
    # It must be a single sentence: one terminal mark, at the end.
    if line[-1] not in ".!?":
        raise ValueError("Line must end with terminal punctuation")
    if line.count(".") + line.count("!") + line.count("?") != 1:
        raise ValueError("Line must be a single sentence")
    if "  " in line:
        raise ValueError("Line must not contain double spaces")
    for ch in line:
        if ord(ch) < 0x20 and ch != "\t":
            raise ValueError(f"Line contains a control character U+{ord(ch):04X}")
    return chars


def main() -> int:
    length = validate(LINE)

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    out_file = os.path.join(out_dir, "entry.txt")

    with open(out_file, "w", encoding="utf-8") as fh:
        fh.write(LINE + "\n")
    os.chmod(out_file, 0o644)

    # Read the file back and confirm what landed is exactly the line.
    with open(out_file, "r", encoding="utf-8") as fh:
        written = fh.read().removesuffix("\n")
    if written != LINE:
        raise ValueError("Read-back check failed: entry.txt does not match the line")

    print(f"Wrote {length} characters to {out_file}")
    print(LINE)
    return 0


if __name__ == "__main__":
    sys.exit(main())
