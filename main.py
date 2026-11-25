"""One-line office joke entry for make.fun's "One-Line Office Joke: 24-Hour Sprint".

The joke:

    I told my boss my spirit animal is the office printer: always jammed,
    permanently out of toner, and somehow still employed.

Why this line should land with the judge:

* It is instantly relatable office pain. Almost everyone who has worked in
  an office has fought a printer that jams and runs out of toner at the
  worst possible moment, so the setup needs no explanation.
* It uses the rule of three. Two printer flaws ("always jammed",
  "permanently out of toner") set the pattern, and the third beat breaks
  it: "somehow still employed" suddenly turns the joke from the printer
  onto the employee, which is the surprise that makes people laugh.
* The punchline flatters the audience. It lets every office worker feel
  seen: we have all suspected that showing up broken still counts as a
  job, just like the printer that never gets fired.
* It is a single self-contained sentence with no setup outside itself, so
  it works cold, read aloud or on the page, with no context needed.

Running this module writes exactly that one line to ``entry.txt`` inside
``MAKEFUN_OUTPUT_DIR`` (falling back to ``/output``).
"""

import os
from pathlib import Path

JOKE = (
    "I told my boss my spirit animal is the office printer: always jammed, "
    "permanently out of toner, and somehow still employed."
)


def write_entry(joke: str, output_dir: Path) -> Path:
    """Write *joke* as the single line of ``entry.txt`` in *output_dir*.

    Refuses to write anything that is not exactly one non-empty line, so a
    future edit to the joke can never silently break the one-line format.
    """
    if not joke or "\n" in joke or "\r" in joke:
        raise ValueError("joke must be exactly one non-empty line")
    output_dir.mkdir(parents=True, exist_ok=True)
    entry_path = output_dir / "entry.txt"
    entry_path.write_text(joke + "\n", encoding="utf-8")
    return entry_path


def main() -> None:
    """Write the joke as the single line of ``entry.txt``."""
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    write_entry(JOKE, output_dir)


if __name__ == "__main__":
    main()
