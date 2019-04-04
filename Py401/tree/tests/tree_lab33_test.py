from tree.tree import BinarySearchTree
import pytest


def test_class():
    assert BinarySearchTree


def test_traverse_inorder():
    tree = BinarySearchTree()
    tree.add('bananas')
    tree.add('apples')
    tree.add('cucumbers')
    items = list(tree.traverse_inorder())
    assert items == ['apples', 'bananas', 'cucumbers']


def test_traverse_preorder():
    tree = BinarySearchTree()
    tree.add('bananas')
    tree.add('apples')
    tree.add('cucumbers')
    items = list(tree.traverse_preorder())
    assert items == ['bananas', 'apples', 'cucumbers']


def test_traverse_postorder():
    tree = BinarySearchTree()
    tree.add('bananas')
    tree.add('apples')
    tree.add('cucumbers')
    items = list(tree.traverse_postorder())
    assert items == ['apples', 'cucumbers', 'bananas']


def test_traverse_breadth_first():
    tree = BinarySearchTree()
    tree.add('bananas')
    tree.add('apples')
    tree.add('cucumbers')
    tree.add('cantelope')
    items = list(tree.traverse_breadth_first())
    assert items == ['bananas', 'apples', 'cucumbers', 'cantelope']


def test_traverse_for_loop():
    tree = BinarySearchTree()
    tree.add('bananas')
    tree.add('apples')
    tree.add('cucumbers')
    items = []
    for item in tree.traverse_inorder():
        items.append(item)
    assert items == ['apples', 'bananas', 'cucumbers']

####### Recursive Yield Example ###
# def traverse_in_order(self):

#         def _traverse(node):
#             if not node:
#                 return
#             yield from _traverse(node.left)
#             yield node.value
#             yield from _traverse(node.right)

#         return _traverse(self.root)
