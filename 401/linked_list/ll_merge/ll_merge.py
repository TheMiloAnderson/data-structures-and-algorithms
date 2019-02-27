
def ll_zip(ll_1, ll_2):
    curr_1 = output = ll_1.head
    curr_2 = ll_2.head
    while curr_1._next and curr_2:
        tmp_1 = curr_1._next
        tmp_2 = curr_2._next
        curr_1._next = curr_2
        curr_2._next = tmp_1
        ll_2.head = tmp_2
        curr_2 = ll_2.head
        curr_1 = curr_1._next._next
    if curr_2:
        curr_1._next = curr_2
    return output
