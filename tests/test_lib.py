from lisperi.lib import Symbol, _parse, _tokenize, _eval


def test_tokenize_basic():
    assert list(_tokenize("(first (list 1 (+ 2 3) 9))")) == [
        "(",
        "first",
        "(",
        "list",
        "1",
        "(",
        "+",
        "2",
        "3",
        ")",
        "9",
        ")",
        ")",
    ]


def test_parse_basic():
    assert _parse("(first (list 1 (+ 2 3) 9))") == [
        Symbol("first"), [Symbol("list"), 1, [Symbol("+"), 2, 3], 9]
    ]


def test_parse_whitespace():
    assert _parse("""
        (if (my-undefined-symbol)
            (1)
            (- 1 1))
        """) == [
            Symbol("if"), [Symbol("my-undefined-symbol")],
                [1],
                [Symbol("-"), 1, 1]
        ]


def test_eval_basic():
    program = _parse("(+ 2 3)")
    assert _eval(program) == 5


def test_eval_nested():
    program = _parse("(+ (+ 1 2) 3)")
    assert _eval(program) == 6
