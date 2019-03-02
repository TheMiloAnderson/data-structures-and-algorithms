
class Stack(object):

    top = None

    def peek(self):
        if self.top:
            return self.top.value
        else:
            return None

    def push(self, val):
        node = Node(val)
        if not self.peek():
            self.top = node
        else:
            curr = self.top
            self.top = node
            self.top.next = curr

    def pop(self):
        if self.peek():
            curr = self.top
            self.top = curr.next
            curr.next = None
            return curr.value
        else:
            return 'Cannot pop(), Stack is empty'

    def print_all(self):
        output = ''
        curr = self.top
        while curr:
            output += str(curr.value) + '; '
            curr = curr.next
        return output


class Queue(object):

    front = None
    rear = None

    def _set_rear(self):
        if self.front:
            curr = self.front
            while curr.next:
                curr = curr.next
            self.rear = curr
        else:
            self.rear = None

    def peek(self):
        if self.front:
            return self.front.value
        else:
            return None

    def enqueue(self, val):
        node = Node(val)
        if not self.rear:
            self.rear = node
            self.front = node
        else:
            self.rear.next = node
            self.rear = node

    def print_all(self):
        output = ''
        curr = self.front
        while curr:
            output += str(curr.value) + '; '
            curr = curr.next
        return output


class Node(object):
    def __init__(self, val):
        self.value = val
        self.next = None
