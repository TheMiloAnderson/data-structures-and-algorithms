from stacks_and_queues.stacks_and_queues import Queue

class BinaryTree(object):
    """ Implements a binary tree with traversal methods """

    def __init__(self):
        self.root = None

    def traverse_inorder(self):
        def _traverse(node):
            if not node:
                return
            yield from _traverse(node.l_child)
            yield node.value
            yield from _traverse(node.r_child)
        return _traverse(self.root)

    def traverse_preorder(self):
        def _traverse(node):
            if not node:
                return
            yield node.value
            yield from _traverse(node.l_child)
            yield from _traverse(node.r_child)
        return _traverse(self.root)

    def traverse_postorder(self):
        def _traverse(node):
            if not node:
                return
            yield from _traverse(node.l_child)
            yield from _traverse(node.r_child)
            yield node.value
        return _traverse(self.root)

    def traverse_breadth_first(self):
        q = Queue()
        q.enqueue(self.root)
        while q.peek():
            curr = q.dequeue()
            yield curr.value
            if curr.l_child:
                q.enqueue(curr.l_child)
            if curr.r_child:
                q.enqueue(curr.r_child)

    def inorder(self, node):
        """ Return binary tree values in left/node/right order """
        output = []
        if node:
            if node.l_child:
                output += self.inorder(node.l_child)
            output.append(node.value)
            if node.r_child:
                output += self.inorder(node.r_child)
        return output

    def postorder(self, node):
        """ Return binary tree values in left/right/node order """
        output = []
        if node:
            if node.l_child:
                output += self.postorder(node.l_child)
            if node.r_child:
                output += self.postorder(node.r_child)
            output.append(node.value)
        return output

    def preorder(self, node):
        """ Return binary tree values in node/left/right order """
        output = []
        if node:
            output.append(node.value)
            if node.l_child:
                output += self.preorder(node.l_child)
            if node.r_child:
                output += self.preorder(node.r_child)
        return output


class BinarySearchTree(BinaryTree):
    """ Extends BinaryTree, populates & searches tree nodes """

    def add(self, val):
        """ Add node to binary tree """
        if not self.root:
            self.root = Node(val)
        else:
            self._add_child(val, self.root)

    def _add_child(self, val, curr):
        """ Add node to binary tree """
        if val < curr.value:
            if not curr.l_child:
                curr.l_child = Node(val)
            else:
                self._add_child(val, curr.l_child)
        else:
            if not curr.r_child:
                curr.r_child = Node(val)
            else:
                self._add_child(val, curr.r_child)

    def contains(self, val, curr=None):
        """ Search binary tree for value """
        if not self.root:
            return False
        if not curr:
            curr = self.root
        if curr.value == val:
            return True
        elif val < curr.value:
            if curr.l_child:
                return self.contains(val, curr.l_child)
            else:
                return False
        elif val > curr.value:
            if curr.r_child:
                return self.contains(val, curr.r_child)
            else:
                return False


class Node(object):
    """ Implements a binary tree node """
    def __init__(self, val):
        self.value = val
        self.l_child = None
        self.r_child = None
