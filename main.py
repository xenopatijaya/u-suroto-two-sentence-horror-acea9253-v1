"""Two-Sentence Horror — make.fun entry program (program/v1).

Writes one horror story of exactly two sentences (155 characters) to
/output/entry.txt, the location the competition kit's RULES.txt requires.
Local verification can redirect the output directory with the
MAKEFUN_OUTPUT_DIR environment variable; the grader runs with it unset,
so the entry lands at /output/entry.txt exactly as the rules require.

Stdlib only. No network, no reads outside this repository, deterministic.
"""

import os
import sys

ENTRY = (
    "Every morning I find my slippers exactly where I left them, "
    "toes pointing toward the door. "
    "This morning they were facing the bed, and they were still warm."
)


def main() -> int:
    # Gate the entry the same way the sealed scorer does: UTF-8 text,
    # 1 to 400 characters, not only white space, exactly two sentences.
    # The story is one line of prose: no line breaks inside it, and its
    # only full stops are the two sentence ends (the second sentence's
    # turn — the slippers facing the bed, still warm — is what reframes
    # the first sentence's quiet routine as a night-time intruder).
    text = ENTRY.strip()
    if not (1 <= len(text) <= 400):
        print(f"entry is {len(text)} characters, must be 1-400", file=sys.stderr)
        return 1
    if "\n" in text or text.count(".") != 2 or not text.endswith("."):
        print("entry must be exactly two sentences on one line", file=sys.stderr)
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    # No trailing newline: the file must hold exactly the entry text.
    with open(out_path, "w", encoding="utf-8") as fh:
        fh.write(text)

    print(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
