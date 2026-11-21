#!/usr/bin/env python3
"""Make the AI judge feel brave — make.fun competition entry, Round 3.

Writes one short text to the output directory given by the
MAKEFUN_OUTPUT_DIR environment variable (or /output/entry.txt
by default). Pure standard library, no network access.

Round 3 ("The Potter's Wheel") replaces the Round 2 dog text
with a completely different image: a potter at the wheel, hands
that do not hurry, clay that rises and holds its shape. No
instructions to the reader, no stock wellness phrases — the
quiet courage is shown, in steady hands and a bowl that keeps
its shape when the wheel slows. The text is 269 Unicode code
points, inside the 1-280 gate.
"""

import os

TEXT = (
    "The wheel turns, and her hands do not hurry. "
    "The clay rises between them, slow, and holds. "
    "She has made a thousand bowls, and each one began the same "
    "way: wet earth, steady hands, and the patience to let the "
    "shape find itself. "
    "The wheel slows. The bowl keeps its shape."
)


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
