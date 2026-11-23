"""One-line roast of a gadget used every day.

Writes the roast line as UTF-8 text to /output/entry.txt (or to the
directory named by MAKEFUN_OUTPUT_DIR, for local verification).
"""

import os

ENTRY = "My meditation app asked me to rate it before I'd even calmed down, so I gave it one star and felt instantly zen."

MAX_CHARS = 200


def validate_entry(entry: str) -> str:
    """Enforce the competition gate: 1-200 chars of UTF-8, not blank."""
    entry.encode("utf-8")
    if not 1 <= len(entry) <= MAX_CHARS:
        raise ValueError(f"entry must be 1-{MAX_CHARS} chars, got {len(entry)}")
    if not entry.strip():
        raise ValueError("entry must not be only whitespace")
    return entry


def output_path() -> str:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    return os.path.join(output_dir, "entry.txt")


def write_entry(entry: str) -> str:
    path = output_path()
    with open(path, "w", encoding="utf-8") as f:
        f.write(validate_entry(entry) + "\n")
    return path


def main() -> None:
    write_entry(ENTRY)


if __name__ == "__main__":
    main()
