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


def test_breadth_traverse(tree, capsys):
    assert tree.root.value == 5
    assert tree.root.l_child.value == 3
    assert tree.root.r_child.value == 8
    assert tree.breadth_traverse() == [5, 3, 8, 1, 4]
