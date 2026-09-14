from lisperi.lib import _tokenize


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
