from linked_list import LinkedList
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
    assert mammals.head._next.value == 'whale'


def test_insert_three():
    mammals = LinkedList()
    mammals.insert('whale')
    mammals.insert('wolf')
    mammals.insert('ape')

    assert mammals.head.value == 'ape'
    assert mammals.head._next.value == 'wolf'
    assert mammals.head._next._next.value == 'whale'


def test_append():
    mammals = LinkedList()
    mammals.insert('mouse')
    mammals.insert('dog')
    mammals.append('cat')

    assert mammals.print() == 'dog; mouse; cat; '


def test_append_multiple():
    mammals = LinkedList()
    mammals.append('mouse')
    mammals.append('dog')
    mammals.append('cat')

    assert mammals.print() == 'mouse; dog; cat; '


def test_insert_before():
    mammals = LinkedList()
    mammals.append('whale')
    mammals.append('wolf')
    mammals.append('ape')
    mammals.insert_before('wolf', 'bat')

    assert mammals.print() == 'whale; bat; wolf; ape; '


def test_insert_after():
    mammals = LinkedList()
    mammals.append('whale')
    mammals.append('wolf')
    mammals.append('ape')
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

    assert mammals.print() == 'The print() method only works if all node values are strings.'


def test_find_from_k():
    mammals = LinkedList()
    mammals.append('orca')
    mammals.append('beluga')
    mammals.append('porpoise')
    mammals.append('otter')
    mammals.append('seal')

    assert mammals.find_from_end(2) == 'porpoise'
    assert mammals.find_from_end(4) == 'orca'
    assert mammals.find_from_end(5) == 'Error: There is no value 5 nodes from the end of this linked list'
