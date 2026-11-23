#!/usr/bin/env python3
"""One-Line Roast entry: writes a single roast line to /output/entry.txt.

Deterministic, code-only: no network, no randomness, no runtime API key.
The line roasts the smartwatch used every day.

The entry gate (see the kit's RULES.txt) requires /output/entry.txt to be
UTF-8 text of 1 to 200 characters, not only white space, so the line is
validated against exactly that rule before anything is written: a single
line, 1-200 characters, with no embedded newline and no trailing newline.
"""

from pathlib import Path
import os

LINE = "My smartwatch buzzes to remind me to breathe, like my own lungs filed a complaint with HR."


def validate(line: str) -> str:
    """Check the line against the entry gate and return it unchanged.

    Returns the same line so main() writes the validated value, never a
    different string than the one that was checked.
    """
    if not 1 <= len(line) <= 200:
        raise ValueError(f"line must be 1-200 characters, got {len(line)}")
    if "\n" in line or "\r" in line:
        raise ValueError("line must be a single line")
    if not line.strip():
        raise ValueError("line must not be only white space")
    # The gate reads the file as UTF-8: prove the line encodes before writing.
    line.encode("utf-8")
    return line


def main() -> None:
    line = validate(LINE)
    output_path = Path(os.environ.get("OUTPUT_PATH", "/output/entry.txt"))
    output_path.parent.mkdir(parents=True, exist_ok=True)
    # Write exactly the line, no trailing newline, so the file is one line.
    output_path.write_text(line, encoding="utf-8")


if __name__ == "__main__":
    main()
