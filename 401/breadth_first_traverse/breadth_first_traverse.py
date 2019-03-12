from tree.tree import BinarySearchTree
from stacks_and_queues.stacks_and_queues import Queue


class BreadthFirstTree(BinarySearchTree):
    """ Extends BinarySearchTree, introduces method for
    breadth-first traversal of binary tree """

    def breadth_traverse(self):
        """ Breadth-first traversal of binary tree """

        output = []
        q = Queue()
        q.enqueue(self.root)
        while q.peek():
            curr = q.dequeue()
            output.append(curr.value)
            if curr.l_child:
                q.enqueue(curr.l_child)
            if curr.r_child:
                q.enqueue(curr.r_child)
        return output

    def __repr__(self):
        return str(self.__class__) + str(self.__dict__)

    def __str__(self):
        return 'Extends BinarySearchTree; self.root == ' + str(self.root)
