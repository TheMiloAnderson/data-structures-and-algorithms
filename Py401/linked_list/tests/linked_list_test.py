from linked_list.linked_list import LinkedList
from linked_list.ll_merge import ll_zip, ll_reverse
"""
Unit tests for the linked_list.LinkedList class
"""


def test_exists():
    assert LinkedList


def test_instantiation():
    assert LinkedList()


def test_insert_one():
    mammals = LinkedList()
    mammals.insert('bear')
    expected = 'bear'
    actual = mammals.head.value

    assert actual == expected


def test_insert_two():
    mammals = LinkedList()
    mammals.insert('whale')
    mammals.insert('wolf')

    assert mammals.head.value == 'wolf'
    assert mammals.head.nxt.value == 'whale'


def test_insert_three():
    mammals = LinkedList()
    mammals.insert('whale')
    mammals.insert('wolf')
    mammals.insert('ape')

    assert mammals.head.value == 'ape'
    assert mammals.head.nxt.value == 'wolf'
    assert mammals.head.nxt.nxt.value == 'whale'


def test_add():
    mammals = LinkedList()
    mammals.insert('mouse')
    mammals.insert('dog')
    mammals.add('cat')

    assert mammals.print() == 'dog; mouse; cat; '


def test_add_multiple():
    mammals = LinkedList()
    mammals.add('mouse')
    mammals.add('dog')
    mammals.add('cat')

    assert mammals.print() == 'mouse; dog; cat; '


def test_insert_before():
    mammals = LinkedList()
    mammals.add('whale')
    mammals.add('wolf')
    mammals.add('ape')
    mammals.insert_before('wolf', 'bat')

    assert mammals.print() == 'whale; bat; wolf; ape; '


def test_insert_after():
    mammals = LinkedList()
    mammals.add('whale')
    mammals.add('wolf')
    mammals.add('ape')
    mammals.insert_after('wolf', 'bat')

    assert mammals.print() == 'whale; wolf; bat; ape; '


def test_insert_before_head():
    mammals = LinkedList()
    mammals.insert('bear')
    mammals.insert_before('bear', 'tiger')

    assert mammals.print() == 'tiger; bear; '


def test_insert_after_head():
    mammals = LinkedList()
    mammals.insert('bear')
    mammals.insert_after('bear', 'tiger')

    assert mammals.print() == 'bear; tiger; '


def test_includes():
    mammals = LinkedList()
    mammals.insert('whale')
    mammals.insert('wolf')
    mammals.insert('ape')

    assert mammals.includes('whale')


def test_includes():
    mammals = LinkedList()
    mammals.insert('whale')
    mammals.insert('wolf')
    mammals.insert('ape')

    assert not mammals.includes('eagle')


def test_includes_empty():
    mammals = LinkedList()

    assert not mammals.includes('tortoise')


def test_print():
    mammals = LinkedList()
    mammals.insert('ape')
    mammals.insert('wolf')
    mammals.insert('whale')

    assert mammals.print() == 'whale; wolf; ape; '


def test_print_empty():
    mammals = LinkedList()

    assert mammals.print() == ''


def test_print_not_strings():
    mammals = LinkedList()
    mammals.insert(99)
    mammals.insert(['a', 'b', 'c'])

    assert mammals.print() == 'All values must be strings.'


def test_find_from_k():
    mammals = LinkedList()
    mammals.add('orca')
    mammals.add('beluga')
    mammals.add('porpoise')
    mammals.add('otter')
    mammals.add('seal')

    assert mammals.find_from_end(2) == 'porpoise'
    assert mammals.find_from_end(4) == 'orca'
    assert mammals.find_from_end(5) is None


def test_ll_zip_equal():
    ll_1 = LinkedList()
    ll_1.add('A')
    ll_1.add('B')
    ll_1.add('C')
    ll_1.add('D')

    ll_2 = LinkedList()
    ll_2.add('1')
    ll_2.add('2')
    ll_2.add('3')
    ll_2.add('4')

    head = ll_zip(ll_1, ll_2)
    assert head.value == 'A'
    assert ll_1.print() == 'A; 1; B; 2; C; 3; D; 4; '


def test_ll_zip_shorter():
    ll_1 = LinkedList()
    ll_1.add('A')
    ll_1.add('B')
    ll_1.add('C')
    ll_1.add('D')

    ll_2 = LinkedList()
    ll_2.add('1')
    ll_2.add('2')
    ll_2.add('3')
    ll_2.add('4')
    ll_2.add('5')
    ll_2.add('6')

    head = ll_zip(ll_1, ll_2)
    assert head.value == 'A'
    assert ll_1.print() == 'A; 1; B; 2; C; 3; D; 4; 5; 6; '


def test_ll_zip_longer():
    ll_1 = LinkedList()
    ll_1.add('A')
    ll_1.add('B')
    ll_1.add('C')
    ll_1.add('D')
    ll_1.add('E')

    ll_2 = LinkedList()
    ll_2.add('1')
    ll_2.add('2')
    ll_2.add('3')
    ll_2.add('4')

    head = ll_zip(ll_1, ll_2)
    assert head.value == 'A'
    assert ll_1.print() == 'A; 1; B; 2; C; 3; D; 4; E; '


def test_ll_reverse():
    ll = LinkedList()
    ll.add('A')
    ll.add('B')
    ll.add('C')
    ll.add('D')
    ll.add('E')
    ll_reverse(ll)
    assert ll.print() == 'E; D; C; B; A; '


def test_ll_iteration():
    ll = LinkedList()
    ll.add('A')
    ll.add('B')
    ll.add('C')
    ll.add('D')
    ll.add('E')
    items = []
    for item in ll:
        items.append(item)
    assert items == ['A', 'B', 'C', 'D', 'E']


def test_ll_conversion():
    ll = LinkedList()
    ll.add('A')
    ll.add('B')
    ll.add('C')
    ll.add('D')
    ll.add('E')
    items = list(ll)
    assert items == ['A', 'B', 'C', 'D', 'E']


def test_ll_expression():
    ll = LinkedList()
    ll.add('A')
    ll.add('B')
    ll.add('C')
    ll.add('D')
    ll.add('E')
    lowercase = [x.lower() for x in ll]
    assert lowercase == ['a', 'b', 'c', 'd', 'e']


def test_add_operator():
    ll = LinkedList()
    ll += 'one'
    ll += 'two'
    ll += 'three'
    assert list(ll) == ['one', 'two', 'three']


def test_concat():
    montagues = LinkedList(['Romeo', 'Benvolio'])
    capulets = LinkedList(['Juliet', 'Tybalt'])
    tutti = montagues + capulets
    assert len(list(tutti)) == 4
    assert len(list(montagues)) == 2