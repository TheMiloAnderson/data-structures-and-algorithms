from queue_with_stacks.queue_with_stacks import PseudoQueue


def test_enqueue_and_dequeue_one():
    p = PseudoQueue()
    p.enqueue('A')
    assert p.dequeue() == 'A'


def test_enqueue_and_dequeue_many():
    p = PseudoQueue()
    p.enqueue('A')
    p.enqueue('B')
    assert p.dequeue() == 'A'
    p.enqueue('C')
    p.enqueue('D')
    assert p.dequeue() == 'B'
    assert p.dequeue() == 'C'


def test_enqueue_and_dequeue_all():
    p = PseudoQueue()
    p.enqueue('A')
    p.enqueue('B')
    p.enqueue('C')
    p.enqueue('D')
    p.enqueue('E')
    assert p.dequeue() == 'A'
    assert p.dequeue() == 'B'
    assert p.dequeue() == 'C'
    assert p.dequeue() == 'D'
    assert p.dequeue() == 'E'
    assert p.dequeue() is None
