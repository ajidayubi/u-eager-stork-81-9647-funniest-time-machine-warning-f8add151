"""Funniest Time Machine Warning Label — make.fun entry.

Writes a single warning label for a time machine to /output/entry.txt.

The label turns the core hazard of time travel — meddling with the past —
into the joke itself, in the flat voice of a printed safety notice, with the
punch saved for the last two words. No network, no randomness, no input:
the same bytes come out on every run.
"""

import os

LABEL = "WARNING: Do not fix your past. It is load-bearing."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    # The sealed scorer gates on 1-120 UTF-8 characters; refuse to emit
    # anything that would fail it instead of writing a bad entry.
    if not 1 <= len(LABEL) <= 120 or LABEL != LABEL.strip():
        raise ValueError("label fails the 1-120 character gate")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(LABEL)


if __name__ == "__main__":
    main()
