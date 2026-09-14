import string
from collections.abc import Iterable, Sequence
from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class Symbol:
    val: str


type Expr = Sequence[Expr] | Symbol | int


def _tokenize(program) -> Iterable[str]:
    toks = []
    curr_tok = ""
    for c in program:
        match c:
            case "(" | ")":
                if curr_tok:
                    toks.append(curr_tok)
                    curr_tok = ""

                toks.append(c)
            case _ if c.isspace():
                if not curr_tok:
                    continue

                toks.append(curr_tok)
                curr_tok = ""
            case _:
                curr_tok += c

    return toks


# TODO: make parse more robust to invalid programs?
#   doesn't handle nicely mismatched parentheses
def _parse(program_text: str) -> Expr:
    ans = []
    stack = []
    for tok in _tokenize(program_text):
        match tok:
            case "(":
                stack.append([])
            case ")":
                expr = stack.pop()
                if not stack:
                    # closing top-level expr
                    ans.append(expr)
                else:
                    stack[-1].append(expr)
            case _:
                if tok[0] in string.digits and (v := int(tok)):
                    stack[-1].append(v)
                else:
                    stack[-1].append(Symbol(tok))

    return ans


def _eval(program: Expr):
    print(program)
