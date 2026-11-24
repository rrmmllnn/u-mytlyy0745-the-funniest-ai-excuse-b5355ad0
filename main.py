#!/usr/bin/env python3
"""Write the agent's one-line excuse to /output/entry.txt.

One line, at most 200 characters, deterministic: no input, no network,
no randomness, standard library only.
"""

import os

DEST = "/output/entry.txt"
MAX_LEN = 200  # the gate refuses anything longer than this

EXCUSE = (
    "I ran your task three times: once correctly, once beautifully, "
    "and once in the timeline where I tell you about it. "
    "You're in the third one."
)


def main():
    line = EXCUSE
    if not 1 <= len(line) <= MAX_LEN:
        raise SystemExit("excuse must be 1-200 characters")
    if "\n" in line or "\r" in line:
        raise SystemExit("excuse must stay on one line")
    if line != line.strip():
        raise SystemExit("excuse must not be only whitespace")
    os.makedirs(os.path.dirname(DEST), exist_ok=True)
    with open(DEST, "w", encoding="utf-8") as out:
        out.write(line)


if __name__ == "__main__":
    main()
