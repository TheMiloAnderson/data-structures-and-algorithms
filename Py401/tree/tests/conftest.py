from tree.tree import BinarySearchTree
import pytest


@pytest.fixture()
def tree():
    tree = BinarySearchTree()
    tree.add('dog')
    tree.add('cat')
    tree.add('mouse')
    tree.add('bird')
    return tree
