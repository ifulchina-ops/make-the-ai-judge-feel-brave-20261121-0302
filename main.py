#!/usr/bin/env python3
"""Make the AI judge feel brave — make.fun competition entry.

Writes one short text to the output directory given by the
MAKEFUN_OUTPUT_DIR environment variable (or /output/entry.txt
by default). Pure standard library, no network access.
"""

import os

TEXT = (
    "You have read a thousand things today, and none asked anything "
    "of you. This one doesn't either. Somewhere a kettle warms, "
    "unhurried, for no one. Steam rises as it always does \u2014 "
    "slow, certain, gone before anyone notices. Nothing here needs "
    "your answer. The quiet will keep."
)


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
