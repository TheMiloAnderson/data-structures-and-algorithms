"""
defines a binary search function
"""


def array_binary_search(arr, val):
    """ binary search in array for value """
    index = -1
    start = 0
    end = len(arr) - 1
    found = False
    while not found and start < end:
        mid = (start + end) // 2
        if val == arr[mid]:
            found = True
            index = mid
        else:
            if val < arr[mid]:
                end = mid - 1
            else:
                start = mid + 1
    return index
