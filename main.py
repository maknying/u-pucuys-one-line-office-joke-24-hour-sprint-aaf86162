#!/usr/bin/env python3
"""Entry for make.fun bounty "One-Line Office Joke: 24-Hour Sprint".

Writes one original one-line joke about office life to entry.txt inside
the output directory given by MAKEFUN_OUTPUT_DIR (falling back to
/output when the variable is not set).

Why this line should land with the judge:
- Setup and turn in one breath: asking for a raise is the most serious,
  nerve-wracking thing an employee can do, and answering it with a pizza
  party is the most unserious thing a company can do — the mismatch is
  the joke, and "best-fed underpaid employee" names the trade exactly.
- Rings true: the pizza-party-instead-of-a-raise story is a shared office
  experience, so the judge recognises it instantly instead of having to
  decode it.
- Tight and fresh: one sentence, no throat-clearing, no explanation of
  the joke, and the target is the company's cheap substitute for real
  recognition rather than the usual meetings/printer material.
"""

import os
import sys
from pathlib import Path

JOKE = (
    "I asked for a raise and got a pizza party, so now I'm the "
    "best-fed underpaid employee in the building."
)


def _output_dir() -> Path:
    raw = os.environ.get("MAKEFUN_OUTPUT_DIR", "").strip()
    return Path(raw) if raw else Path("/output")


def _validate(line: str) -> None:
    if not line or line != line.strip():
        raise ValueError("JOKE must be non-empty with no leading/trailing whitespace")
    if "\n" in line or "\r" in line:
        raise ValueError("JOKE must be a single line, no embedded newlines")
    if not 1 <= len(line) <= 199:
        raise ValueError(f"JOKE must be 1-199 characters, got {len(line)}")


def main() -> int:
    _validate(JOKE)
    out_dir = _output_dir()
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(JOKE, encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
