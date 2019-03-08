from tree.tree import BinarySearchTree


def test_instantiate():
    assert BinarySearchTree()


def test_add_one():
    t = BinarySearchTree()
    t.add(4)
    assert t.root.value == 4


def test_add_many():
    t = BinarySearchTree()
    t.add('dog')
    t.add('cat')
    t.add('mouse')
    assert t.root.value == 'dog'
    assert t.root.l_child.value == 'cat'
    assert t.root.r_child.value == 'mouse'


def test_contains(tree):
    assert tree.contains('mouse') == True
    assert tree.contains('cat') == True
    assert tree.contains('tortoise') == False


def test_inorder(tree):
    assert tree.inorder(tree.root) == ['bird', 'cat', 'dog', 'mouse']


def test_postorder(tree):
    assert tree.postorder(tree.root) == ['bird', 'cat', 'mouse', 'dog']


def test_preorder(tree):
    assert tree.preorder(tree.root) == ['dog', 'cat', 'bird', 'mouse']
