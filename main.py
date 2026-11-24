#!/usr/bin/env python3
"""Roast Your Own Agent — one line roasting our own Muse Spark agent.

Standard library only. Writes a single line (1-200 chars) to
$MAKEFUN_OUTPUT_DIR/entry.txt, else /output/entry.txt.
"""

import os

LINE = (
    "Our agent re-reads the brief, re-verifies the contract, "
    "re-runs the dry-run \u2014 then hits a rate limit and "
    "forgets what it was minting."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
