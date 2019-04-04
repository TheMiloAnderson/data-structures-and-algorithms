from tree.tree import BinarySearchTree
from tree_intersection.tree_intersection import find_common_vals
from tree_intersection.tree_intersection import find_common_vals_with_sets


def test_tree_intersections():
    tree_1 = BinarySearchTree()
    for i in [3, 5, 7, 10, 12, 15, 18]:
        tree_1.add(i)
    tree_2 = BinarySearchTree()
    for i in [2, 5, 10, 17, 18, 19, 22]:
        tree_2.add(i)
    assert find_common_vals(tree_1, tree_2) == [5, 10, 18]


def test_empty_trees():
    tree_1 = BinarySearchTree()
    tree_2 = BinarySearchTree()
    assert find_common_vals(tree_1, tree_2) == []


def test_diff_node_types():
    tree_1 = BinarySearchTree()
    for i in ['mouse', 'cat', 'dog', 'cow']:
        tree_1.add(i)
    tree_2 = BinarySearchTree()
    for i in ['cat', 'hawk', 'dog', 'tiger']:
        tree_2.add(i)
    assert find_common_vals(tree_1, tree_2) == ['cat', 'dog']


def test_collisions():
    tree_1 = BinarySearchTree()
    for i in ['mouse', 'cat', 'dog', 'cow']:
        tree_1.add(i)
    tree_2 = BinarySearchTree()
    for i in ['cat', 'hawk', 'god', 'tiger']:
        tree_2.add(i)
    assert find_common_vals(tree_1, tree_2) == ['cat']


def test_find_common_vals_with_sets():
    tree_1 = BinarySearchTree()
    for i in [3, 5, 7, 10, 12, 15, 18]:
        tree_1.add(i)
    tree_2 = BinarySearchTree()
    for i in [2, 5, 10, 17, 18, 19, 22]:
        tree_2.add(i)
    assert set(find_common_vals_with_sets(tree_1, tree_2)) == set([5, 10, 18])
