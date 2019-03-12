from breadth_first_traverse.breadth_first_traverse import BreadthFirstTree
import pytest


@pytest.fixture()
def tree():
    tree = BreadthFirstTree()
    tree.add(5)
    tree.add(3)
    tree.add(8)
    tree.add(1)
    tree.add(4)
    return tree


def test_exists(tree):
    assert tree


def test_breadth_traverse(tree):
    assert tree.breadth_traverse() == [5, 3, 8, 1, 4]


def test_empty_tree():
    tree = BreadthFirstTree()
    assert tree.breadth_traverse() == []
