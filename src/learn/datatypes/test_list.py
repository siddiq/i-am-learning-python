""" module to learn list """


def test_list_creating():
    """ list creating """

    list1 = [1, 2, 3, 4, 5]
    assert list1 == [1, 2, 3, 4, 5]
    assert isinstance(list1, list)

    list2 = list(range(1, 6))
    assert list2 == [1, 2, 3, 4, 5]

    list3 = list("hello")
    assert list3 == ["h", "e", "l", "l", "o"]

    list4 = list((1, 2, 3, 4, 5))
    assert list4 == [1, 2, 3, 4, 5]

    list5 = list({1, 2, 3, 4, 5})
    assert list5 == [1, 2, 3, 4, 5]

    list6 = list({"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}.keys())
    assert list6 == ["a", "b", "c", "d", "e"]

    list7 = list({"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}.values())
    assert list7 == [1, 2, 3, 4, 5]

    list8 = range(5)
    assert isinstance(list8, range)
    assert not isinstance(list8, list)
    assert len(list8) == 5
    assert list(list8) == [0, 1, 2, 3, 4]

    list9 = range(6)
    assert list(list9) == [0, 1, 2, 3, 4, 5]


def test_lists_operations():
    """ list ops """

    list8 = [1] * 4
    assert list8 == [1, 1, 1, 1]

    list1 = [1, 2, 3]
    list2 = [4, 5, 6]
    assert list1 + list2 == [1, 2, 3, 4, 5, 6]


def test_lists_sort():
    """ list sort """

    list1 = ["1", "6", "9", "15", "10"]
    list1.sort() 
    assert list1 == ["1", "10", "15", "6", "9"]

    list2 = [1, 6, 9, 15, 10]
    list2.sort()
    assert list2 == [1, 6, 9, 10, 15]

    list3 = [1, 6, 9, 15, 10]
    list3.sort(reverse=True)
    assert list3 == [15, 10, 9, 6, 1]


def test_lists_comprehension():
    """ list comprehension """

    list1 = [i for i in range(10)]
    assert list1 == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    list2 = [i for i in range(10) if i % 2 == 0]
    assert list2 == [0, 2, 4, 6, 8]

    list3 = [i for i in range(10) if i % 2 == 0 and i > 5]
    assert list3 == [6, 8]

    list4 = [i if i % 2 == 0 else 0 for i in range(10)]
    assert list4 == [0, 0, 2, 0, 4, 0, 6, 0, 8, 0]

    squares = [i * i for i in range(10)]
    assert squares == [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]


def test_lists_stack():
    """ list as stack """

    stack = [1, 2, 3]
    stack.append(4)
    assert stack == [1, 2, 3, 4]

    stack.pop()
    assert stack == [1, 2, 3]

    stack.pop()
    assert stack == [1, 2]

    stack.pop()
    assert stack == [1]

    stack.pop()
    assert len(stack) == 0


def test_lists_queue():
    """ list as queue """

    queue = [1, 2, 3]
    queue.insert(0, 4)
    assert queue == [4, 1, 2, 3]

    queue.pop(0)
    assert queue == [1, 2, 3]

    queue.pop(0)
    assert queue == [2, 3]
    
    queue.pop(0)
    assert queue == [3]

    queue.pop(0)
    assert len(queue) == 0
