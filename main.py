#!/usr/bin/env python3
"""Houseplant out-of-office auto-reply.

Writes one original out-of-office auto-reply, as if a houseplant sent it,
to ``entry.txt`` inside the output directory named by the
``MAKEFUN_OUTPUT_DIR`` environment variable (``/output`` by default).

The reply is a single line of at most 120 characters: the office fern,
last watered in March and still alive out of spite, files the sender's
email under "compost".

Standard library only. No network, no clock, no randomness, no input
files: every run writes exactly the same bytes, so the output is fully
deterministic.
"""

import os

# The entry: one out-of-office auto-reply from a houseplant, 115 chars.
LINE = (
    "Out of office: I'm the office fern, last watered in March, "
    "alive out of spite. Your email is filed under 'compost'."
)

MAX_CHARS = 120


def main() -> None:
    if not 1 <= len(LINE) <= MAX_CHARS:
        raise ValueError(
            "entry must be 1 to 120 characters, got %d" % len(LINE)
        )
    if not LINE.strip():
        raise ValueError("entry must not be only white space")

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # No trailing newline: the file holds exactly the reply, so its
    # character count is unambiguous.
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(LINE)


if __name__ == "__main__":
    main()
