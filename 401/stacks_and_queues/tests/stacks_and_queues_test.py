from stacks_and_queues import Stack


def test_push_one():
    letters = Stack()
    letters.push('A')
    assert letters.print_all() == 'A; '


def test_push_many():
    letters = Stack()
    letters.push('A')
    letters.push('B')
    letters.push('C')
    assert letters.print_all() == 'C; B; A; '


def test_pop():
    letters = Stack()
    letters.push('A')
    letters.push('B')
    letters.push('C')
    assert letters.pop() == 'C'


def test_pop_all():
    letters = Stack()
    letters.push('A')
    letters.push('B')
    letters.push('C')
    assert letters.pop() == 'C'
    assert letters.pop() == 'B'
    assert letters.pop() == 'A'
    assert letters.print_all() == ''


def test_pop_too_many():
    letters = Stack()
    letters.push('A')
    letters.push('B')
    letters.push('C')
    assert letters.pop() == 'C'
    assert letters.pop() == 'B'
    assert letters.pop() == 'A'
    assert letters.pop() == 'Cannot pop(), Stack is empty'


def test_peek():
    letters = Stack()
    assert not letters.peek()

    letters.push('A')
    assert letters.peek() == 'A'

    letters.push('B')
    assert letters.peek() == 'B'
