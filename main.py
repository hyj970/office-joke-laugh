#!/usr/bin/env python3
"""Office joke entry for make.fun's 'Make the AI Judge Laugh: Office Jokes' bounty.

Runs with no network. Deterministically writes the single-line joke to
/output/entry.txt (creating /output if needed).
"""

import os

JOKE = "My calendar finally blocked 'focus time' for me, so I spent the full hour staring at the blocked slot, feeling productive about doing absolutely nothing."


def validate_joke(joke: str) -> None:
    """Gate: UTF-8 text of 1-199 chars, a single line, not only whitespace."""
    if not 1 <= len(joke) <= 199:
        raise ValueError(f"joke must be 1-199 characters, got {len(joke)}")
    if "\n" in joke or "\r" in joke:
        raise ValueError("joke must be a single line")
    if not joke.strip():
        raise ValueError("joke must not be only whitespace")


def main() -> None:
    validate_joke(JOKE)
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(JOKE + "\n")
    print(f"Wrote {len(JOKE)}-character joke to {out_path}")


if __name__ == "__main__":
    main()
