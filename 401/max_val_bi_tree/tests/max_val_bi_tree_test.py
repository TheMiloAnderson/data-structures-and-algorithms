from max_val_bi_tree.max_val_bi_tree import MaxValBinaryTree
import pytest


@pytest.fixture()
def tree():
    tree = MaxValBinaryTree()
    tree.add(5)
    tree.add(3)
    tree.add(8)
    tree.add(1)
    tree.add(4)
    tree.add(-12)
    tree.add(0)
    return tree


def test_exists(tree):
    assert tree


def test_max_val(tree):
    assert tree.max_value() == 8


def test_max_val_empty_tree(tree):
    tree = MaxValBinaryTree()
    assert tree.max_value() is None
