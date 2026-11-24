"""Writes the entry text to /output/entry.txt.

Python 3.13, standard library only, no network.
"""

# The entry text is one review line: a sincere approval carrying quiet
# existential dread, with the punch landing on the shrug at the end.
# One sentence, 116 characters — inside the 140-character gate.
import os

TEXT = (
    "LGTM. The tests pass, the diff is clean, and in a hundred years "
    "none of this will have mattered, but today it ships."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
