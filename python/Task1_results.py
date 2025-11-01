"""Simple script with a main function that writes 'hello world' to a file."""
from pathlib import Path


OUTPUT_FILENAME = "..\hello.txt"


def main() -> None:
    """Write 'hello world' to the output file."""
    Path(OUTPUT_FILENAME).write_text("hello world\n", encoding="utf-8")


if __name__ == "__main__":
    main()
