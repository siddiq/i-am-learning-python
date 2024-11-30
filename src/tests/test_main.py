""" module doc string """

from src.main import square


def test_square():
    """ this is function doc string """

    assert square(1) == 1
    assert square(2) == 4
    assert square(3) == 9
    assert square(-2) == 4
    assert square(0) == 0
