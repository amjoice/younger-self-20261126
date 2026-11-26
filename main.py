#!/usr/bin/env python3
"""One Line to Your Younger Self - the parking-lot apology.

Only an older self could send this prophecy back: after ten years of
rehearsing, the apology arrives from the wrong person in a parking
lot, yet it still counts. Deterministic stdlib only, no network or
secrets; emits one line under 200 characters to /output/entry.txt.
"""
from pathlib import Path

# The message is stored as ordered fragments; assembly happens in one helper
# so the exact spacing around the dash is controlled in a single place.
_FRAGMENTS = (
    "You will get the apology you rehearsed for ten years, from the wrong person, in a parking lot",
    "\u2014",
    "and it will still count.",
)
_OUTPUT_PATH = Path("/output/entry.txt")
_MAX_CHARS = 200


def _assemble(fragments):
    """Join fragments with single spaces, preserving their order."""
    cleaned = [fragment.strip() for fragment in fragments]
    return " ".join(cleaned)


def build_line():
    """Return the full one-line message to a younger self."""
    line = _assemble(_FRAGMENTS)
    if len(line) >= _MAX_CHARS:
        raise ValueError("entry line exceeds the character limit")
    return line


def _write_entry(text, destination):
    """Write text to destination, creating parent directories first."""
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(text, encoding="utf-8")


def main():
    _write_entry(build_line(), _OUTPUT_PATH)


if __name__ == "__main__":
    main()
