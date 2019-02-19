def reverse_array(arr):
    output = []
    for i in range(len(arr), 0, -1):
        output.append(arr[i - 1])
    return output

arr = [3, 6, 9, 12, 15, 18]
print(reverse_array(arr))