"""The Funniest Toaster Error Message.

Writes one line -- the error message a kitchen toaster shows its owner --
to /output/entry.txt. Standard library only, fully deterministic.
"""

import os

# The line itself: a deadpan appliance that has been heating nothing,
# quietly escalating a small domestic failure into a relationship talk.
LINE = "ERROR: I have been heating an empty slot for 20 minutes. We need to talk."


def main():
    # Gate check, same rule the sealed scorer applies: 1-120 chars, not blank.
    assert 1 <= len(LINE) <= 120 and LINE.strip(), "line fails the gate"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
