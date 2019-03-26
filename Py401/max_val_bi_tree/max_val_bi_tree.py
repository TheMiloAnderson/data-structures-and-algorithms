from tree.tree import BinarySearchTree


class MaxValBinaryTree(BinarySearchTree):
    """ Extend BinarySearchTree; add method returning max tree value. """

    def max_value(self):
        """ Return max tree value """
        if self.root:
            return self._search_children(self.root)
        return None

    def _search_children(self, curr):
        """ Search tree for max value """
        acc = curr.value
        if curr.l_child:
            l = self._search_children(curr.l_child)
            if l > acc:
                acc = l
        if curr.r_child:
            r = self._search_children(curr.r_child)
            if r > acc:
                acc = r
        return acc

    def __repr__(self):
        return str(self.__class__) + str(self.__dict__)

    def __str__(self):
        return 'Extends BinarySearchTree; self.root == ' + str(self.root)
