from stacks_and_queues.stacks_and_queues import Stack, Queue


def print_all(ll):
    """ Testing helper function """
    output = ''
    if hasattr(ll, 'top'):
        curr = ll.top
    elif hasattr(ll, 'front'):
        curr = ll.front
    while curr:
        output += str(curr.value) + '; '
        curr = curr.nxt
    return output


def test_push_one():
    letters = Stack()
    letters.push('A')
    assert print_all(letters) == 'A; '


def test_push_many():
    letters = Stack()
    letters.push('A')
    letters.push('B')
    letters.push('C')
    assert print_all(letters) == 'C; B; A; '


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
    assert print_all(letters) == ''


def test_pop_too_many():
    letters = Stack()
    letters.push('A')
    letters.push('B')
    letters.push('C')
    assert letters.pop() == 'C'
    assert letters.pop() == 'B'
    assert letters.pop() == 'A'
    assert letters.pop() is None


def test_stack_peek():
    letters = Stack()
    assert not letters.peek()

    letters.push('A')
    assert letters.peek() == 'A'

    letters.push('B')
    assert letters.peek() == 'B'


def test_instantiate_queue():
    assert Queue()


def test_enqueue_one():
    letters = Queue()
    letters.enqueue('A')
    assert print_all(letters) == 'A; '


def test_enqueue_many():
    letters = Queue()
    letters.enqueue('A')
    letters.enqueue('B')
    letters.enqueue('C')
    assert print_all(letters) == 'A; B; C; '


def test_dequeue():
    letters = Queue()
    letters.enqueue('A')
    letters.enqueue('B')
    letters.enqueue('C')
    assert letters.dequeue() == 'A'
    assert letters.dequeue() == 'B'
    assert letters.dequeue() == 'C'
    assert letters.dequeue() is None


def test_queue_peek():
    letters = Queue()
    assert not letters.peek()

    letters.enqueue('A')
    assert letters.peek() == 'A'

    letters.enqueue('B')
    assert letters.peek() == 'A'
