
def ll_zip(ll_1, ll_2):
    curr_1 = output = ll_1.head
    curr_2 = ll_2.head
    while curr_1.nxt and curr_2:
        tmp_1 = curr_1.nxt
        tmp_2 = curr_2.nxt
        curr_1.nxt = curr_2
        curr_2.nxt = tmp_1
        ll_2.head = tmp_2
        curr_2 = ll_2.head
        curr_1 = curr_1.nxt.nxt
    if curr_2:
        curr_1.nxt = curr_2
    return output


def ll_reverse(ll):
    prev = None
    curr = ll.head
    while curr:
        nxt = curr.nxt
        curr.nxt = prev
        prev = curr
        curr = nxt
    ll.head = prev
