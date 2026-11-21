#!/usr/bin/env python3
"""Make the AI judge feel brave — make.fun competition entry, Round 2.

Writes one short text to the output directory given by the
MAKEFUN_OUTPUT_DIR environment variable (or /output/entry.txt
by default). Pure standard library, no network access.

Round 2 ("The Dog at the Gate") replaces the Round 1 kettle text
with a completely different image: an old dog waiting at an open
gate through the night. No instructions to the reader, no stock
wellness phrases — the quiet courage is shown, in the dog who
stays, night after night, until morning comes home. The text
is 276 Unicode code points, inside the 1–280 gate.
"""

import os

TEXT = (
    "The gate is open, and the old dog is still there, asleep "
    "with his chin on his paws, waiting for footsteps he knows "
    "by heart. He is not afraid of the dark, or of the hours. "
    "He has done this every night of his life, and the night "
    "has never once failed to bring the morning home."
)


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
