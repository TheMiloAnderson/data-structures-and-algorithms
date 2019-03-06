from fifo_animal_shelter.fifo_animal_shelter import Animal, AnimalShelter
# from stacks_and_queues.stacks_and_queues import Queue, Node

import sys
sys.path.insert(
    0, '/home/milo/codefellows/data-structures-and-algorithms/401/')


def test_enqueue_one():
    cat = Animal('cat')
    fas = AnimalShelter()
    fas.enqueue(cat)
    assert fas.front.value.type == 'cat'
