class LinkedList(object):
    """
    Implements a singly linked list, with methods to add nodes,
    search node values, and print all node values
    """

    head = None

    def insert(self, val):
        """ insert a new node into head of linked list """
        node = Node(val)
        if not self.head:
            self.head = node
        else:
            current = self.head
            self.head = node
            self.head.next = current

    def append(self, val):
        """ insert a new node at end of linked list """
        node = Node(val)
        if not self.head:
            self.head = node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = node

    def insert_before(self, val, new_val):
        """ insert a new value before given value """
        if self.includes(val):
            if self.head.value == val:
                self.insert(new_val)
            else:
                node = Node(new_val)
                current = self.head
                while current.next.value != val:
                    current = current.next
                node.next = current.next
                current.next = node

    def insert_after(self, val, new_val):
        """ insert a new value after given value """
        if self.includes(val):
            if self.head.value == val:
                self.append(new_val)
            else:
                node = Node(new_val)
                current = self.head
                while current.value != val:
                    current = current.next
                node.next = current.next
                current.next = node

    def includes(self, val):
        """ search for value in linked list """
        if self.head:
            current = self.head
            while current:
                if current.value == val:
                    return True
                current = current.next
            return False
        else:
            return False

    def print(self):
        """ returns a concatenated string of all linked list values """
        output = ''
        current = self.head
        try:
            while current:
                output += current.value + '; '
                current = current.next
            return output
        except TypeError:
            return 'All values must be strings.'

    def find_from_end(self, k):
        if not self.head:
            return 'This linked list is empty'
        vals = []
        current = self.head
        while current:
            vals.append(current.value)
            current = current.next
        if len(vals) - 1 >= k:
            return vals[len(vals) - 1 - k]
        else:
            return None


class Node(object):
    """
    Implements a single linked list node
    """

    def __init__(self, val):
        self.value = val
        self.next = None
