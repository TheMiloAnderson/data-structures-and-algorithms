from hashtable.hashtable import Hashtable


def find_common_vals(tree_1, tree_2):
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
