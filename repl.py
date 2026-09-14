#!/usr/bin/env -S uv run --script
#
# /// script
# requires-python = ">=3.14"
# ///

def _eval(program: str):
    print(program)
    print()


if __name__ == "__main__":
    while program := input("> "):
        _eval(program)
