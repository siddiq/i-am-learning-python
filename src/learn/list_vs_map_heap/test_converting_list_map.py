"""
Map to List conversion tricks

"""


def test_list_to_map():
    """list to map"""

    list1 = [
        "abc",
        "def",
        "ghi",
        "abc",
        "jkl",
        "mno",
        "pqr",
        "stu",
        "vwx",
        "yz",
        "vwx",
        "vwx",
        "vwx",
    ]

    map1 = {}
    for i in list1:
        if i in map1:
            map1[i] += 1
        else:
            map1[i] = 1

    assert map1["abc"] == 2
    assert map1["def"] == 1

    # max items from map
    map1max = max(map1.items(), key=lambda x: x[1])
    assert map1max == ("vwx", 4)

    # sorted items from map
    sorted1 = sorted(map1.items(), key=lambda x: x[1], reverse=True)
    assert sorted1[0] == ("vwx", 4)
    assert sorted1[1] == ("abc", 2)
