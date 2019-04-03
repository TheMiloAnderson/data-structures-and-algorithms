from copy import deepcopy


class LinkedList(object):
    """
    Implements a singly linked list, with methods to add nodes,
    search node values, and print all node values
    """

    def __init__(self, iterable=None):
        self.head = None
        if iterable:
            for val in iterable:
                self.insert(val)

    def __iter__(self):
        curr = self.head
        while curr:
            yield curr.value
            curr = curr.nxt

    def __iadd__(self, val):
        self.add(val)
        return self

    def __add__(self, iterable):
        new_list = deepcopy(self)
        for val in iterable:
            new_list.add(val)
        return new_list

    def insert(self, val):
        """ insert a new node into head of linked list """
        node = Node(val)
        if not self.head:
            self.head = node
        else:
            current = self.head
            self.head = node
            self.head.nxt = current

    def add(self, val):
        """ insert a new node at end of linked list """
        node = Node(val)
        if not self.head:
            self.head = node
        else:
            current = self.head
            while current.nxt:
                current = current.nxt
            current.nxt = node

    def insert_before(self, val, new_val):
        """ insert a new value before given value """
        if self.includes(val):
            if self.head.value == val:
                self.insert(new_val)
            else:
                node = Node(new_val)
                current = self.head
                while current.nxt.value != val:
                    current = current.nxt
                node.nxt = current.nxt
                current.nxt = node

    def insert_after(self, val, new_val):
        """ insert a new value after given value """
        if self.includes(val):
            if self.head.value == val:
                self.add(new_val)
            else:
                node = Node(new_val)
                current = self.head
                while current.value != val:
                    current = current.nxt
                node.nxt = current.nxt
                current.nxt = node

    def includes(self, val):
        """ search for value in linked list """
        if self.head:
            current = self.head
            while current:
                if current.value == val:
                    return True
                current = current.nxt
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
                current = current.nxt
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
            current = current.nxt
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
        self.nxt = None
