
def ll_zip(ll_1, ll_2):
    curr_1 = output = ll_1.head
    curr_2 = ll_2.head
    while curr_1.next and curr_2:
        tmp_1 = curr_1.next
        tmp_2 = curr_2.next
        curr_1.next = curr_2
        curr_2.next = tmp_1
        ll_2.head = tmp_2
        curr_2 = ll_2.head
        curr_1 = curr_1.next.next
    if curr_2:
        curr_1.next = curr_2
    return output


def ll_reverse(ll):
    prev = None
    curr = ll.head
    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    ll.head = prev
