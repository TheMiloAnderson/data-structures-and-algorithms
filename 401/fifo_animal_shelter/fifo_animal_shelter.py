from stacks_and_queues.stacks_and_queues import Queue, Node
import sys
sys.path.insert(0, '/home/milo/codefellows/data-structures-and-algorithms/401')


class AnimalShelter(object):
    def __init__(self):
        self._queue = Queue()

    def enqueue(self, animal):
        node = Node(animal)
        if not self._queue.rear:
            self._queue.rear = node
            self._queue.front = node
        else:
            self._queue.rear.next = node
            self._queue.rear = node

    def dequeue(self, pref):
        if self._queue.front:
            prev = None
            curr = self._queue.front
            while curr.value.type != pref:
                prev = curr
                curr = curr.next
            prev.next = curr.next
            curr.next = None
            return curr.value
        return None


class Animal(object):
    def __init__(self, type):
        self.type = type
