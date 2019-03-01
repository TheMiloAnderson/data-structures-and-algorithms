
class Stack(object):

    top = None

    def push(self, val):
        node = Node(val)
        if not self.top:
            self.top = node
        else:
            curr = self.top
            self.top = node
            self.top.next = curr

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
