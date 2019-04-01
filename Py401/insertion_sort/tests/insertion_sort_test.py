from insertion_sort.insertion_sort import sort_by_insertion


def test_random():
    arr = [3, 9, 11, 16, 14, 12, 15, 8, 10, 2, 5, 6, 13, 7, 4, 17, 1]
    sort_by_insertion(arr)
    assert arr == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]


def test_sorted():
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    sort_by_insertion(arr)
    assert arr == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def test_backwards():
    arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    sort_by_insertion(arr)
    assert arr == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def test_empty():
    arr = []
    sort_by_insertion(arr)
    assert arr == []


def test_one():
    arr = [5]
    sort_by_insertion(arr)
    assert arr == [5]
