"""Rename the Planet -- one-line entry.

Writes a single funny new name for Mars, plus the why, to the output
file the grader reads. The line is fixed and deterministic: the same
bytes come out on every run.
"""

import os

# The entry: Mars as a fixer-upper property listing. The joke is the
# idea, not a pun on the name -- the least habitable planet in the
# solar system is somehow the one everyone is planning to move to.
ENTRY_LINE = (
    "Mars is now 'The Fixer-Upper': red dust everywhere, no water, "
    "no refunds, and everyone's still planning to move in."
)

MAX_CHARS = 200


def output_path():
    """Where the entry line goes: $OUTPUT_PATH wins, then the harness
    directory, then /output/entry.txt."""
    explicit = os.environ.get("OUTPUT_PATH")
    if explicit:
        return explicit
    base = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    return os.path.join(base, "entry.txt")


def main():
    os.umask(0o022)

    line = ENTRY_LINE
    if not line.strip():
        raise SystemExit("entry line must not be blank")
    if "\n" in line or "\r" in line:
        raise SystemExit("entry must be a single line")
    if not 1 <= len(line) <= MAX_CHARS:
        raise SystemExit(
            "entry is %d characters, limit is %d" % (len(line), MAX_CHARS)
        )

    path = output_path()
    parent = os.path.dirname(path)
    if parent:
        os.makedirs(parent, exist_ok=True)

    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(line)

    # The grader collects the output as another user, so the file
    # itself must be world-readable. Only the file is chmodded --
    # never the /output directory, which the sandbox owns.
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
