#!/usr/bin/env python3
"""One Line, One Laugh entry.

Writes a single funny line to entry.txt in the output directory
($MAKEFUN_OUTPUT_DIR, default /output).
"""

import os

LINE = "I tried to ghost my gym, but it keeps texting me 'we miss you', the only relationship that's ever chased me."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
