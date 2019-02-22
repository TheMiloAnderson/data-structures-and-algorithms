class LinkedList(object):
    """
    Implements a singly linked list, with methods to add nodes,
    search node values, and print all node values
    """

    head = None

    def insert(self, val):
        """ insert a new node into linked list """
        node = Node(val)
        if not self.head:
            self.head = node
        else:
            current = self.head
            self.head = node
            self.head._next = current

    def includes(self, val):
        """ search for value in linked list """
        if self.head:
            current = self.head
            while current._next:
                if current.value == val:
                    return True
                current = current._next
            return False
        else:
            return False

    def print(self):
        """ returns a concatenated string of all linked list values """
        output = ''
        current = self.head
        while current:
            output += current.value + '; '
            current = current._next
        return output


class Node(object):
    """
    Implements a single linked list node
    """

    def __init__(self, val):
        self.value = val
        self._next = None
