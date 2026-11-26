#!/usr/bin/env python3
"""One Line to Your Younger Self - the apology, in one line.

The line is a prophecy only an older self could send back: the apology
rehearsed for ten years arrives from the wrong person in a parking lot,
and it still counts. Pure stdlib, deterministic, no network, no secrets;
writes a single line under 200 characters to /output/entry.txt.
"""
import os

# The line, assembled from its two halves so the wording stays in one place.
_OPENING = "You will get the apology you rehearsed for ten years, from the wrong person, in a parking lot"
_CLOSING = "and it will still count."
_DASH = "\u2014"


def build_line():
    """Return the full one-line message to a younger self."""
    return " ".join((_OPENING, _DASH, _CLOSING))


def main():
    line = build_line()
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as out:
        out.write(line)


if __name__ == "__main__":
    main()
