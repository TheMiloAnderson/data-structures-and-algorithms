from tree.tree import BinarySearchTree
from fizz_buzz_tree.fbt import fizz_buzz_tree
import pytest


@pytest.fixture()
def tree():
    tree = BinarySearchTree()
    tree.add(1)
    tree.add(3)
    tree.add(5)
    tree.add(9)
    tree.add(10)
    tree.add(15)
    tree.add(18)
    tree.add(19)
    tree.add(20)
    tree.add(30)
    tree.add(31)
    tree.add(33)
    return tree


def test_fizz_buzz_tree(tree):
    fizz_buzz_tree(tree)
    assert tree.inorder(tree.root) == [
        1,
        'Fizz',
        'Buzz',
        'Fizz',
        'Buzz',
        'FizzBuzz',
        'Fizz',
        19,
        'Buzz',
        'FizzBuzz',
        31,
        'Fizz'
    ]
