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


def test_includes():
    mammals = LinkedList()
    mammals.insert('whale')
    mammals.insert('wolf')
    mammals.insert('ape')

    assert mammals.includes('wolf')


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
