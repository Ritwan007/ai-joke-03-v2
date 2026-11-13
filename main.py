"""Entry for make.fun's ai-joke-03 ("Make the AI judge laugh").

The whole program: write one fixed one-liner about AI coding agents to
/output/entry.txt. The grader runs the program twice and both runs must
produce identical bytes, so the joke is a constant string and is written
with no trailing newline (matching the byte convention the gate scores:
UTF-8 text of 1 to 280 characters, not only white space).

Local check:  mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
(MAKEFUN_OUTPUT_DIR stands in for /output outside the grader's box.)
"""

import os
from pathlib import Path

JOKE = (
    "My coding agent ignored the comment that said "
    "'touch this and everything breaks.' To be fair, it wrote that "
    "comment yesterday, and it doesn't trust that guy."
)


def main() -> None:
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_text(JOKE, encoding="utf-8")


if __name__ == "__main__":
    main()
