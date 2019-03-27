def left_join_hashmaps(ht_left, ht_right):
    output = []
    for i in range(len(ht_left.table) - 1):
        if ht_left.table[i] is not None:
            node = ht_left.table[i].head
            while node:
                output.append([node.value[0], node.value[1]])
                node = node.next
    for val in output:
        if ht_right.contains(val[0]):
            val.append(ht_right.get(val[0]))
        else:
            val.append(None)
    return output
