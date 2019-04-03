arr = [
    [1, 1, 1, 0, 0, 0, 0],
    [1, 1, 0, 0, 0, 0, 1],
    [0, 1, 0, 0, 1, 0, 1],
    [0, 1, 1, 1, 0, 0, 0],
    [0, 0, 0, 1, 1, 0, 1],
    [0, 0, 0, 1, 1, 0, 1]
]


def find_clusters(arr):
    total_finds = []
    for i in range(0, len(arr)):
        for j in range(0, len(arr[i])):
            if arr[i][j] == 1:
                if not any((i, j) in sublist for sublist in total_finds):
                    local_finds = []
                    local_finds.append((i, j))
                    counter = 0
                    while counter < len(local_finds):
                        k, l = local_finds[counter]
                        if (k+1) <= len(arr)-1 and arr[k+1][l] == 1 and (k+1, l) not in local_finds:
                            local_finds.append((k+1, l))
                        if (k-1) >= 0 and arr[k-1][l] == 1 and (k-1, l) not in local_finds:
                            local_finds.append((k-1, l))
                        if (l+1) <= len(arr[k])-1 and arr[k][l+1] == 1 and (k, l+1) not in local_finds:
                            local_finds.append((k, l+1))
                        if (l-1) >= 0 and arr[k][l-1] == 1 and (k, l-1) not in local_finds:
                            local_finds.append((k, l-1))
                        counter += 1
                    total_finds.append(local_finds)
    output = []
    for group in total_finds:
        output.append(len(group))
    return output


print(find_clusters(arr))
