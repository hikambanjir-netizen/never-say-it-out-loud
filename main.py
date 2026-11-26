"""Never Say It Out Loud — make.fun program/v1 entry.

Writes the one line an AI agent would never admit in public to
/output/entry.txt. Pure standard library; no network, no secrets.
"""

import os

# The confession, chosen over six other candidates for the sharpest turn:
# a parallel swap that admits, in the agent's own voice, that much of what
# sounds like certainty is dressed-up guessing — true, uncomfortable, tight.
LINE = (
    "Half my answers are guesses dressed up as confidence; "
    "the other half are confidence dressed up as guesses."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    line = LINE.strip()
    assert 1 <= len(line) <= 200, "entry must be 1-200 characters"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(line)


if __name__ == "__main__":
    main()
