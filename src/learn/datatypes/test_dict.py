""" module to learn dict """


def test_dict_creating():
    """ dict creating """

    dict1 = {}
    assert dict1 == {}

    dict2 = {"a": 1, "b": 2, "c": 3}
    assert dict2 == {"a": 1, "b": 2, "c": 3}
    assert isinstance(dict2, dict)

    dict3 = dict(a=1, b=2, c=3)
    assert dict3 == {"a": 1, "b": 2, "c": 3}
    assert isinstance(dict3, dict)

    dict4 = dict([("a", 1), ("b", 2), ("c", 3)])
    assert dict4 == {"a": 1, "b": 2, "c": 3}
    assert isinstance(dict4, dict)

    dict5 = dict([["a", 1], ["b", 2], ["c", 3]])
    assert dict5 == {"a": 1, "b": 2, "c": 3}
    assert isinstance(dict5, dict)

    dict6 = dict([("a", 1), ["b", 2], ("c", 3)])
    assert dict6 == {"a": 1, "b": 2, "c": 3}
    assert isinstance(dict6, dict)

    dict7 = dict({"a": 1, "b": 2, "c": 3})
    assert dict7 == {"a": 1, "b": 2, "c": 3}
    assert isinstance(dict7, dict)

    dict9 = dict({"a": 1, "b": 2, "c": 3})
    assert list(dict9.keys()) == ["a", "b", "c"]
    assert list(dict9.values()) == [1, 2, 3]
    assert list(dict9.items()) == [("a", 1), ("b", 2), ("c", 3)]


def test_dict_access_members():
    """ dict access members """

    dict1 = {"a": 1, "b": 2, "c": 3}
    assert dict1["a"] == 1
    assert dict1.get("a") == 1
    assert dict1.get("d") is None
    assert dict1.get("d", 4) == 4
    dict1["d"] = 4
    assert dict1.get("d") == 4
    assert dict1.get("d", 5) == 4
    assert dict1.pop("d") == 4
    assert dict1.get("d") is None


def test_dictr_iterating():
    """ dict iterating """

    dict1 = {"a": 1, "b": 2, "c": 3}

    for key in dict1:
        assert key in ["a", "b", "c"]

    for value in dict1.values():
        assert value in [1, 2, 3]

    for key, value in dict1.items():
        assert key in ["a", "b", "c"]
        assert value in [1, 2, 3]
