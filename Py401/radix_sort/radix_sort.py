def radix_sort(arr):
    """ Implements radix sort in conjunction with
    counting sort function below """
    if len(arr) > 0:
        biggest_number = max(arr)
        exp = 1
        while biggest_number/exp > 1:
            counting_sort(arr, exp)
            exp *= 10


def counting_sort(arr, exp):
    """ Implements counting sort, to be called by radix_sort 
    with appropriate exponent """
    n = len(arr)
    output = [0] * n
    count = [0] * 10
    for i in range(n):
        index = arr[i] // exp
        count[index % 10] += 1
    for i in range(1, 10):
        count[i] += count[i-1]
    i = n - 1
    while i >= 0:
        index = arr[i] // exp
        count[index % 10] -= 1
        output[count[index % 10]] = arr[i]
        i -= 1
    for i in range(n):
        arr[i] = output[i]

