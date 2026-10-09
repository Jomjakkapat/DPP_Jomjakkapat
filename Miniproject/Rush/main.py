import sys
from pathlib import Path

if __package__:
    from .checkmate import is_in_check
else:
    from checkmate import is_in_check


def main() -> None:
    for filename in sys.argv[1:]:
        try:
            rows = Path(filename).read_text(encoding="utf-8").splitlines()
        except (OSError, UnicodeError):
            print("Error")
            continue

        in_check = is_in_check(*rows)
        if in_check is None:
            print("Error")
        else:
            print("Success" if in_check else "Fail")


if __name__ == "__main__":
    main()
