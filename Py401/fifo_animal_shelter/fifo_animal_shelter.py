from stacks_and_queues.stacks_and_queues import Queue, Node
import sys
sys.path.insert(0, '/home/milo/codefellows/data-structures-and-algorithms/401')


class AnimalShelter(object):
    def __init__(self):
        self._queue = Queue()

    def enqueue(self, animal):
        self._queue.enqueue(animal)

    def dequeue(self, pref):
        if pref not in ('dog', 'cat'):
            return None
        if self._queue.front:
            curr = self._queue.front
            prev = None
            while curr.value.species != pref:
                prev = curr
                curr = curr.nxt
            if prev:
                prev.nxt = curr.nxt
            else:
                self._queue.front = curr.nxt
            curr.nxt = None
            return curr.value
        return None


class Animal(object):
    def __init__(self, species, name):
        self.name = name
        self.species = species
