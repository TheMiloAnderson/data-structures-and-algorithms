from hashtable.hashtable import Hashtable


def find_common_vals(tree_1, tree_2):
    """ Accepts two binary tree objects, returns a list of values present
    in both trees. Uses a hashtable class. """
    ht = Hashtable()
    rtn = []
    val_list_1 = tree_1.inorder(tree_1.root)
    val_list_2 = tree_2.inorder(tree_2.root)
    for val in val_list_1:
        ht.add(val, str(val))
    for val in val_list_2:
        if ht.contains(val):
            rtn.append(val)
    return rtn


def find_common_vals_with_sets(tree_1, tree_2):
    """ Accepts two binary tree objects, returns a list of values present
    in both trees. Uses sets. """
    set_1 = set(tree_1.traverse_inorder())
    set_2 = set(tree_2.traverse_inorder())
    return list(set_1.intersection(set_2))
