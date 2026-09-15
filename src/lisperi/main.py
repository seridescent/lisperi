import readline  # ruff: ignore[F401]  # readline modifies built-in input function

from lisperi.lib import _eval, _parse


def main() -> None:
    while program_text := input("> "):
        program = _parse(program_text)
        res = _eval(program)
        print(res, end="\n\n")


if __name__ == "__main__":
    main()
