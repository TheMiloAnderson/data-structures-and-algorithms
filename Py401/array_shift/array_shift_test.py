from array_shift import insert_shift_array

def test_even_len_array_given():
    """ test array where length is even number """
    actual = insert_shift_array([1, 2, 3, 4, 5, 6], 99)
    expected = [1, 2, 3, 99, 4, 5, 6]
    assert actual == expected

def test_odd_len_array_given():
    """ test array where length is odd number """
    actual = insert_shift_array([1, 2, 3, 4, 5], 99)
    expected = [1, 2, 3, 99, 4, 5]
    assert actual == expected

def test_0_len_array_given():
    """ test array where length is 0 """
    actual = insert_shift_array([], 99)
    expected = [99]
    assert actual == expected