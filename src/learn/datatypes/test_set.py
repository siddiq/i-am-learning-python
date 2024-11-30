import pytest
""" module to learn set """


def test_set_creating():
    """ test set creating """
    
    set1 = {1, 2, 3, 4, 5}
    assert set1 == {1, 2, 3, 4, 5}

    set2 = set([1, 2, 3, 4, 5])
    assert set2 == {1, 2, 3, 4, 5}

    set4 = set("hello")
    assert set4 == {'h', 'e', 'l', 'o'}

    set3 = set()
    assert set3 == set()


def test_set_add_remove():
    """ test set add, remove, update """

    set1 = {1, 2, 3, 4, 5}
    set1.add(6)
    assert set1 == {1, 2, 3, 4, 5, 6}

    set1.remove(6)
    assert set1 == {1, 2, 3, 4, 5}
    with pytest.raises(KeyError):
        set1.remove(6)
        
    set1.discard(6)
    set1.discard(6)
    set1.discard(6)
    assert set1 == {1, 2, 3, 4, 5}

    set1.update([6, 7, 8])
    assert set1 == {1, 2, 3, 4, 5, 6, 7, 8}

    set1.update([6, 7, 8], [9, 10])
    assert set1 == {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}


def test_set_operations():
    """ union, intersections etc """

    set1 = {1, 2, 3}
    set2 = {3, 4, 5}

    set3 = set1 | set2
    assert set3 == {1, 2, 3, 4, 5}
    
    set4 = set1.union(set2)
    assert set4 == {1, 2, 3, 4, 5}

    set5 = set1 & set2
    assert set5 == {3}

    set6 = set1.intersection(set2)
    assert set6 == {3}

    set7 = set1 - set2
    assert set7 == {1, 2}

    set8 = set1.difference(set2)
    assert set8 == {1, 2}

    set9 = set1 ^ set2
    assert set9 == {1, 2, 4, 5}

    set10 = set1.symmetric_difference(set2)
    assert set10 == {1, 2, 4, 5}

    set11 = set1.copy()
    assert set11 == {1, 2, 3}


def test_set_check_membership():
    """ check membership """

    set1 = {1, 2, 3}
    assert 1 in set1
    assert 4 not in set1

    len1 = len(set1)
    assert len1 == 3


def test_set_check_subset():
    """ check subset """

    set1 = {1, 2, 3}
    set2 = {1, 2, 3, 4, 5}
    set3 = {1, 2, 4, 5}

    assert set1.issubset(set2)
    assert not set1.issubset(set3)

    assert set1 <= set2
    assert not set1 <= set3

    assert set2.issuperset(set1)
    assert not set3.issuperset(set1)

    assert set2 >= set1
    assert not set3 >= set1


def test_set_check_disjoint():
    """ check disjoint """

    set1 = {1, 2, 3}
    set2 = {1, 2, 3, 4, 5}
    set3 = {1, 2, 4, 5}
    set4 = {4, 5, 6}

    assert not set1.isdisjoint(set2)
    assert set1.isdisjoint(set4)
    assert not set1.isdisjoint(set3)


def test_set_clear():
    """ clear set """

    set1 = {1, 2, 3}
    set1.clear()
    assert set1 == set()


def test_set_frozenset():
    """ frozenset """

    set1 = {1, 2, 3}
    set2 = frozenset(set1)

    assert set2 == frozenset({1, 2, 3})
    assert isinstance(set2, frozenset)
