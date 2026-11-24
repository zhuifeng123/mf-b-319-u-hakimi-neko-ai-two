#!/usr/bin/env python3
from pathlib import Path

ENTRY = (
    "LGTM. The tests pass, the void is patient, and merging is just "
    "another word for hoping."
)


def main() -> None:
    out = Path("/output")
    out.mkdir(parents=True, exist_ok=True)
    (out / "entry.txt").write_text(ENTRY + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
