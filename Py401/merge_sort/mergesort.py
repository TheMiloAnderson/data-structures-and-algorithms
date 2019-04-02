def mergesort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = mergesort(arr[:mid])
        right = mergesort(arr[mid:])
        output = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                output.append(left[i])
                i += 1
            else:
                output.append(right[j])
                j += 1
        if i < len(left):
            output += left[i:]
        if j < len(right):
            output += right[j:]
        return output
    else:
        return arr
