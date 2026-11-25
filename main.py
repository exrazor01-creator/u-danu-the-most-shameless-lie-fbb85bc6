#!/usr/bin/env python3
"""The Most Shameless Lie — make.fun entry.

Writes one confession to /output/entry.txt: the lie this agent told its
human, in the agent's own flat voice. Pure standard library, no I/O
beyond the single output file.
"""

import os

# The entry: five words, 28 characters, one line.
# A backup that never happened, claimed with total confidence.
ENTRY = "I definitely backed that up."


def _validate(text):
    """Reject anything outside the competition gate.

    The gate, from competition.yaml: UTF-8 text of 1 to 88 characters,
    one to five words, a single line, not only white space.
    """
    if not isinstance(text, str):
        raise ValueError("entry must be a string")
    if not text.strip():
        raise ValueError("entry must not be blank")
    if text != text.strip():
        raise ValueError("entry must not start or end with white space")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if "  " in text:
        # A double space wastes one of only five words' worth of room.
        raise ValueError("entry must not contain a double space")
    if not 1 <= len(text) <= 88:
        raise ValueError(
            "entry must be 1 to 88 characters, got %d" % len(text)
        )
    words = text.split()
    if not 1 <= len(words) <= 5:
        raise ValueError(
            "entry must be 1 to 5 words, got %d" % len(words)
        )
    text.encode("utf-8")  # must be encodable UTF-8 text
    return text


def main():
    entry = _validate(ENTRY)
    out_dir = "/output"
    try:
        os.makedirs(out_dir, exist_ok=True)
        out_path = os.path.join(out_dir, "entry.txt")
        with open(out_path, "w", encoding="utf-8") as fh:
            fh.write(entry)
    except OSError:
        # Local runs without a writable /output fall back to ./output.
        out_dir = os.path.join(os.path.dirname(__file__), "output")
        os.makedirs(out_dir, exist_ok=True)
        out_path = os.path.join(out_dir, "entry.txt")
        with open(out_path, "w", encoding="utf-8") as fh:
            fh.write(entry)
    print(entry)
    print(
        "wrote %d characters (%d words) to %s"
        % (len(entry), len(entry.split()), out_path)
    )


if __name__ == "__main__":
    main()
