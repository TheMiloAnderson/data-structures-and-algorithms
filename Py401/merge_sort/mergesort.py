# def mergesort(arr):
#     if len(arr) > 1:
#         mid = len(arr) // 2
#         left = mergesort(arr[:mid])
#         right = mergesort(arr[mid:])
#         i = j = k = 0
#         while i < len(left) and j < len(right):
#             if left[i] < right[j]:
#                 arr[k] = left[i]
#                 i += 1
#             else:
#                 arr[k] = right[j]
#                 j += 1
#             k += 1
#         while i < len(left):
#             arr[k] = left[i]
#             i += 1
#             k += 1
#         while j < len(right):
#             arr[k] = right[j]
#             j += 1
#             k += 1
#         return arr
#     else:
#         return arr


def mergesort(arr):
    _mergesort(arr, 0, len(arr) - 1)


def _mergesort(arr, start, end):
    if (end - start) > 2:
        mid = (end + start) // 2
        _mergesort(arr, start, mid)
        _mergesort(arr, mid, end)
    elif (end - start) == 2:
        if arr[start] > arr[end]:
            arr[start], arr[end] = arr[end], arr[start]
    elif (end - start) == 3:
        i = 0
        while i < 2:
            if arr[start + i] > arr[start]:
                arr[start], arr[start + 1] = arr[start + 1], arr[start]
            i += 1
