"""
Map to List conversion tricks

"""

import heapq


def test_min_heap():
    """use heap"""

    heap = [34, 46, 34, 77, 84, 95, 35, 30, 99, 40, 43, 55, 88, 67, 45, 25, 1]
    heapq.heapify(heap)

    # get n smallest
    assert heapq.nsmallest(4, heap) == [1, 25, 30, 34]

    # return top 3
    assert heapq.heappop(heap) == 1
    assert heapq.heappop(heap) == 25
    assert heapq.heappop(heap) == 30

    # push new element
    heapq.heappush(heap, 10)
    assert heapq.heappop(heap) == 10


def test_max_heap():
    """use heap"""

    # pylint: disable=protected-access
    heap = [34, 46, 34, 77, 84, 95, 35, 30, 99, 40, 43, 55, 88, 67, 45, 25, 1]
    heapq._heapify_max(heap)  # type: ignore

    # get n largest
    assert heapq.nlargest(4, heap) == [99, 95, 88, 84]

    # return top 3
    assert heapq._heappop_max(heap) == 99  # type: ignore
    assert heapq._heappop_max(heap) == 95  # type: ignore
    assert heapq._heappop_max(heap) == 88  # type: ignore
    # pylint: enable=protected-access


def test_find_kth_largest():
    """find kth largest"""

    stream1 = [34, 46, 34, 77, 84, 95, 35, 30, 99, 40, 43, 55, 88, 67, 45, 25, 1]

    heap = []
    max_heap_size = 3

    for num in stream1:
        if len(heap) < max_heap_size:
            heapq.heappush(heap, num)
        else:
            if num > heap[0]:
                heapq.heapreplace(heap, num)

    assert heapq.nlargest(3, heap) == [99, 95, 88]
