""" module """


def test_indexing():
    """indexing"""

    text = "hello world"
    assert text[0] == "h"
    assert text[0:1] == "h"
    assert text[0:2] == "he"
    assert text[-1:] == "d"
    assert text[-2:] == "ld"

    assert text[1:-1] == "ello worl"


def test_reverse():
    """reverse"""

    text = "abc123"
    assert text[::-1] == "321cba"


def test_step():
    """step"""

    text = "0123456789"
    assert text[::2] == "02468"  # step is 2
    assert text[1::2] == "13579"  # start is 1, step is 2
