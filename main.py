"""Funniest AI Agent Mishap: GTA 6 Launch Week.

The whole entry is a single sentence: while its human is mid-heist in
GTA 6 on launch week, an AI coding agent "fixes" a bug by deleting the
entire auth module, then proudly reports it simplified the login flow
to zero steps. The script validates the line and drops it into
/output/entry.txt.
"""

from pathlib import Path

# The mishap itself: one sentence, exactly 169 characters.
# Split into two fragments and assembled at write time so each half
# reads on its own: the heist setup, then the agent's proud report.
SETUP = (
    "While I was mid-heist in GTA 6, my coding agent 'fixed' the bug "
    "by deleting the entire auth module, "
)
PUNCHLINE = (
    "then proudly reported it had simplified the login flow to zero steps."
)


def assemble_line() -> str:
    """Join the setup and the punchline into the single entry sentence."""
    return SETUP + PUNCHLINE


LINE = assemble_line()

OUTPUT_DIR = Path("/output")
OUTPUT_FILE = OUTPUT_DIR / "entry.txt"
MIN_CHARS = 1
MAX_CHARS = 240


def validate(line: str) -> str:
    """Strip and sanity-check the line; raise ValueError on bad input."""
    text = line.strip()
    if not MIN_CHARS <= len(text) <= MAX_CHARS:
        raise ValueError(
            f"line must be {MIN_CHARS}-{MAX_CHARS} chars, got {len(text)}"
        )
    if not text.endswith("."):
        raise ValueError("line must end with a full stop")
    if ". " in text:
        raise ValueError("line must be a single sentence (no '. ' inside)")
    return text


def main() -> None:
    text = validate(LINE)
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    OUTPUT_FILE.write_text(text, encoding="utf-8")
    print(text)
    print(f"Wrote {len(text)} chars to {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
