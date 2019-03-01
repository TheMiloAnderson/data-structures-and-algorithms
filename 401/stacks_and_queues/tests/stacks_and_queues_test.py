from stacks_and_queues import Stack


def test_push():
    letters = Stack()
    letters.push('A')
    letters.push('B')
    letters.push('C')
    assert letters.print_all() == 'C; B; A; '
