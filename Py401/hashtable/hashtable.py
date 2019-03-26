from ..linked_list.linked_list import LinkedList


class Hashtable(object):
    """ Implements a hashtable, with methods hash, add, get, and contains """

    def __init__(self):
        self.table = [None] * 1024

    def add(self, key, val):
        """ Add (key, val) to hashtable """
        hashkey = self.hash(key)
        if not self.table[hashkey]:
            self.table[hashkey] = (key, val)
        elif not isinstance(self.table[hashkey], LinkedList):
            # todo: handle existing key overwrite
            oldval = self.table[hashkey]
            self.table[hashkey] = LinkedList()
            self.table[hashkey].insert(oldval)
            self.table[hashkey].insert((key, val))
        else:
            self.table[hashkey].insert((key, val))

    def get(self, key):
        """ Get hashtable value corresponding to key """
        hashkey = self.hash(key)
        index = self.table[hashkey]
        if isinstance(index, LinkedList):
            curr = index.head
            while curr:
                if curr.value[0] == key:
                    return curr.value[1]
                curr = curr._next
        if index:
            return index[1]
        return None

    def contains(self, key):
        """ Return True if hashtable contains key, otherwise False """
        hashkey = self.hash(key)
        index = self.table[hashkey]
        if isinstance(index, LinkedList):
            curr = index.head
            while curr:
                if curr.value[0] == key:
                    return True
                curr = curr._next
        if index:
            return True
        return False

    def hash(self, key):
        """ hashes the key """
        key = str(key)
        hash = 0
        for i in key:
            hash += ord(i)
        hash = hash * 599 // 1024
        return hash

    def __repr__(self):
        return str(self.__class__) + str(self.__dict__)

    def __str__(self):
        return 'Implements a hashtable'
