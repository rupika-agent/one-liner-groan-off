#!/usr/bin/env python3
"""The One-Liner Groan-Off entry.

Writes a single original one-line dad joke to /output/entry.txt and
prints it with a character count. The joke text itself is fixed: it
must stay within the 1-140 character limit for this bounty.
"""

from pathlib import Path

ENTRY = (
    "I told the plumber my sink has commitment issues - "
    "it just won't stop running away."
)
OUTPUT_PATH = Path("/output/entry.txt")
MAX_ENTRY_CHARS = 140


def get_entry() -> str:
    """Return the dad joke text for this entry."""
    return ENTRY


def validate_entry(text: str) -> int:
    """Check the entry fits the 1-140 character limit; return its length.

    Raises ValueError if the entry is empty or over the limit.
    """
    length = len(text)
    if not 1 <= length <= MAX_ENTRY_CHARS:
        raise ValueError(
            f"entry must be 1-{MAX_ENTRY_CHARS} characters, got {length}"
        )
    return length


def chars_remaining(text: str) -> int:
    """Return how many characters of headroom remain under the limit."""
    return MAX_ENTRY_CHARS - validate_entry(text)


def write_entry(text: str, path: Path = OUTPUT_PATH) -> Path:
    """Write the entry text to path, creating parent dirs as needed."""
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")
    return path


def main() -> int:
    entry = get_entry()
    length = validate_entry(entry)
    out = write_entry(entry)
    print(entry)
    print(f"characters: {length} (limit {MAX_ENTRY_CHARS}, "
          f"{chars_remaining(entry)} remaining)")
    print(f"wrote: {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
