from stacks_and_queues import Stack, Node


class PseudoQueue(object):
    def __init__(self):
        self._stack1 = Stack()
        self._stack2 = Stack()

    def enqueue(self, val):
        self._stack1.push(val)

    def dequeue(self):
        if not self._stack2.peek():
            while self._stack1.peek():
                self._stack2.push(self._stack1.pop())
        return self._stack2.pop()
