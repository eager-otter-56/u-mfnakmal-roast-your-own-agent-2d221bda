#!/usr/bin/env python3
"""Roast Your Own Agent — entry generator.

Writes the one-line roast to entry.txt inside MAKEFUN_OUTPUT_DIR
(default /output), creating the directory if needed.
"""
import os

TEXT = (
    "My agent summarised a three-line email into a nine-page report, "
    "scheduled a meeting to present it, and billed me 40,000 tokens "
    "for the privilege of reading my own inbox back to me."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(TEXT)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
