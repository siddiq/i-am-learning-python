"""
    Data Types

    Text Type:	str
    Numeric Types:	int, float, complex
    Sequence Types:	list, tuple, range
    Mapping Type:	dict
    Set Types:	set, frozenset
    Boolean Type:	bool
    Binary Types:	bytes, bytearray, memoryview
    None Type:	NoneType
"""


def test_str():
    """str"""

    a = "5"
    assert type(a) == str  # noqa: E721 # pylint: disable=unidiomatic-typecheck
    assert isinstance(a, str)

    b = str(5)
    assert isinstance(b, str)
    assert type(b) == str  # noqa: E721 # pylint: disable=unidiomatic-typecheck
    assert b == "5"
    assert b != 5
    assert not b == 5  # pylint: disable=unnecessary-negation


def test_numeric():
    """numeric"""

    xint = 5
    assert isinstance(xint, int)

    xfloat = float(5)
    assert isinstance(xfloat, float)
    assert str(xfloat) == "5.0"

    xcomplex = complex(5)
    assert isinstance(xcomplex, complex)
    assert str(xcomplex) == "(5+0j)"

    xbool = bool(5)
    assert isinstance(xbool, bool)
    assert str(xbool) == "True"


def test_sequence():
    """sequence"""

    xlist = [1, 2, 3, 4, 5]
    assert isinstance(xlist, list)

    xtuple = (5,)
    assert isinstance(xtuple, tuple)

    xrange = range(5)
    assert isinstance(xrange, range)


def test_mapping():
    """mapping"""

    xdict = {"a": 1, "b": 2}
    assert isinstance(xdict, dict)
    assert xdict["a"] == 1
    assert xdict["b"] == 2


def test_set():
    """set"""

    xset = {1, 2, 3, 4, 5}
    assert isinstance(xset, set)

    xfrozenset = frozenset(xset)
    assert isinstance(xfrozenset, frozenset)


def test_binary():
    """binary"""

    xbytes = bytes(5)
    assert isinstance(xbytes, bytes)

    xbytearray = bytearray(5)
    assert isinstance(xbytearray, bytearray)

    xmemoryview = memoryview(bytes(5))
    assert isinstance(xmemoryview, memoryview)


def test_none():
    """none"""

    xnone = None
    assert isinstance(xnone, type(None))

    if xnone is None:
        assert True

    if xnone is not None:
        assert False
