"""
A function that adds a value to the middle index of an array
"""

def insert_shift_array(arr, val):
    """A function that adds a value to the middle index of an array"""
    mid = (len(arr) + 1) // 2
    new_arr = []
    for i in range(mid):
        print(i, arr[i])
        new_arr.append(arr[i])
    new_arr.append(val)
    for i in range(mid, len(arr)):
        new_arr.append(arr[i])
    return new_arr