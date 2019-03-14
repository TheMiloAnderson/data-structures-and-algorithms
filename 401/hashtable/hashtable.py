from linked_list.linked_list import LinkedList


class Hashtable(object):
    """  """

    def __init__(self):
        self.table = [None] * 1024

    def add(self, key, val):
        """  """
        hashkey = self.hash(key)
        self.table[hashkey] = (key, val)

    def get(self, key):
        """  """
        pass

    def contains(self, key):
        """  """
        pass

    def hash(self, key):
        """ hashes the key """
        key = str(key)
        hash = 0
        for i in range(len(key) - 1):
            hash += ord(key[i])
        hash = hash * 599 // 1024
        return hash

    def __repr__(self):
        return str(self.__class__) + str(self.__dict__)

    def __str__(self):
        return 'Implements a hashtable'
