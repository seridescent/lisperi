from lisperi.lib import Symbol, _parse, _tokenize


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
        [Symbol("first"), [Symbol("list"), 1, [Symbol("+"), 2, 3], 9]]
    ]
