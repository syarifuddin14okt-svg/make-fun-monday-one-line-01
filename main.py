#!/usr/bin/env python3
"""Monday, Reviewed in One Line — make.fun entry.

Writes one line, under 200 characters, to /output/entry.txt:
a one-line review of the entrant's own Monday. Concrete detail
(a broken elevator, six floors, a meeting about working smarter)
with the turn at the end — arriving too tired to disagree.
"""

import os

LINE = "The elevator broke, so I climbed six floors to a meeting about working smarter, and arrived too tired to disagree."


def verify_output() -> None:
    """Read the written file back as bytes and confirm it is byte-identical."""
    with open("/output/entry.txt", "rb") as f:
        data = f.read()
    assert data.decode("utf-8") == LINE.strip(), "output differs from LINE"
    assert 1 <= len(data) <= 200, f"output must be 1-200 bytes, got {len(data)}"
    print(f"verified {len(data)} bytes, byte-identical")


def main() -> None:
    text = LINE.strip()
    assert 1 <= len(text) <= 200, f"line must be 1-200 chars, got {len(text)}"
    assert text.strip(), "line must not be whitespace-only"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)
    print(f"wrote {len(text)} chars to /output/entry.txt")
    verify_output()


if __name__ == "__main__":
    main()
