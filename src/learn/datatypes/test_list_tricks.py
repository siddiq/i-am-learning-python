""" module to learn list """

from collections import Counter


def test_list_counting():
    """list frequency counting"""

    list1 = [1, 1, 1, 2, 2, 3, 4, 5, 6, 7, 77, 7, 7, 7]
    counts = Counter(list1)
    assert counts[1] == 3
    assert counts[7] == 4
    assert counts[77] == 1


def test_list_reference():
    """list reference"""

    list1 = [1, 2, 3, 4, 5]
    list2 = list1

    assert len(list1) == len(list2)
    list1.pop()
    assert len(list1) == len(list2)
    assert list1 == list2


def test_list_copy():
    """list copy"""

    list1 = [1, 2, 3, 4, 5]
    list2 = list1.copy()

    assert len(list1) == len(list2)
    list1.pop()
    assert len(list1) < len(list2)
    assert list1 != list2


def test_unpacking_lists():
    """unpacking lists"""

    list1 = [1, 2, 3, 4, 5]

    a, b, c, d, e = list1
    assert a == 1
    assert b == 2
    assert c == 3
    assert d == 4
    assert e == 5

    a, b, *c = list1
    assert a == 1
    assert b == 2
    assert c == [3, 4, 5]

    *a, b = list1
    assert a == [1, 2, 3, 4]
    assert b == 5

    a, *b, c = list1
    assert a == 1
    assert b == [2, 3, 4]
    assert c == 5
