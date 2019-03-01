
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
        try:
            while curr:
                output += curr.value + '; '
                curr = curr.next
            return output
        except TypeError:
            return 'Cannot print; not all stack values are strings'


class Node(object):
    def __init__(self, val):
        self.value = val
        self.next = None
