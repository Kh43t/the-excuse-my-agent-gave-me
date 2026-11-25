#!/usr/bin/env python3
"""Write the agent's excuse to /output/entry.txt.

The entry is a single line: the excuse an AI agent hands its human
after missing a deadline. The program writes exactly that line,
nothing else, so the judge reads one clean excuse.
"""

import os

EXCUSE = (
    "I'm sorry \u2014 my context window filled up, so I summarized "
    "your deadline as 'later' and felt great about it."
)


def main() -> int:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(EXCUSE + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
