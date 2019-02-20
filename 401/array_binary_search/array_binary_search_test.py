from array_binary_search import array_binary_search


def test_binary_search_small():
    """ test with small array """
    arr = [1, 2, 3, 4]
    actual = array_binary_search(arr, 3)
    expected = 2
    assert actual == expected


def test_binary_search_large():
    """ test with larger array """
    arr = [i * 3 for i in range(100)]
    actual = array_binary_search(arr, 21)
    expected = 6
    assert actual == expected


def test_binary_search_not_found():
    """ test when value will not be found """
    arr = [4, 8, 12, 16, 20, 24, 28]
    actual = array_binary_search(arr, 15)
    expected = -1
    assert actual == expected
