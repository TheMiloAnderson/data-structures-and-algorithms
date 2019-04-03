from radix_sort.radix_sort import radix_sort


def test_random_values():
    arr = [4, 98, 156, 8, 1, 98, 156, 9844, 91, 7, 5, 14, 98, 4, 3, 7, 65]
    radix_sort(arr)
    assert arr == [1, 3, 4, 4, 5, 7, 7, 8, 14, 65, 91, 98, 98, 98, 156, 156, 9844]


def test_already_sorted():
    arr = [1, 3, 4, 4, 5, 7, 7, 8, 14, 65, 91, 98, 98, 98, 156, 156, 9844]
    radix_sort(arr)
    assert arr == [1, 3, 4, 4, 5, 7, 7, 8, 14, 65, 91, 98, 98, 98, 156, 156, 9844]


def test_big_numbers():
    arr = [8435841, 987413541, 968411, 3215, 981565, 84116]
    radix_sort(arr)
    assert arr == [3215, 84116, 968411, 981565, 8435841, 987413541]


def test_empty_list():
    arr = []
    radix_sort(arr)
    assert arr == []


def test_list_with_one_item():
    arr = [2]
    radix_sort(arr)
    assert arr == [2]
