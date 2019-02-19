"""
A function that adds a value to the middle index of an array
"""

def insert_shift_array(arr, val):
    """A function that adds a value to the middle index of an array"""
    mid = len(arr) // 2
    new_arr = []
    for i in range(mid):
        new_arr[i] = arr[i]
    new_arr[mid] = val
    for i in range(mid, len(arr) - 1):
        new_arr[i + 1] = arr[i]
    return rew_arr