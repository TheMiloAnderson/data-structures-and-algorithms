

class BinaryTree(object):
    """  """
    def __init__(self):
        self.root = None

    def inorder(self, node):
        """  """
        output = []
        if node.l_child:
            output += self.inorder(node.l_child)
        output.append(node.value)
        if node.r_child:
            output += self.inorder(node.r_child)
        return output

    def postorder(self, node):
        """  """
        output = []
        if node.l_child:
            output += self.postorder(node.l_child)
        if node.r_child:
            output += self.postorder(node.r_child)
        output.append(node.value)
        return output

    def preorder(self, node):
        """  """
        output = []
        output.append(node.value)
        if node.l_child:
            output += self.preorder(node.l_child)
        if node.r_child:
            output += self.preorder(node.r_child)
        return output


class BinarySearchTree(BinaryTree):
    """  """
    def add(self, val):
        """  """
        if not self.root:
            self.root = Node(val)
        else:
            self._add_child(val, self.root)

    def _add_child(self, val, curr):
        """  """
        if val < curr.value:
            if not curr.l_child:
                curr.l_child = Node(val)
            else:
                self._add_child(val, curr.l_child)
        else:
            if not curr.r_child:
                curr.r_child = Node(val)
            else:
                self._add_child(val, curr.r_child)

    def contains(self, val, curr=None):
        """  """
        if not self.root:
            return False
        if not curr:
            curr = self.root
        if curr.value == val:
            return True
        elif val < curr.value:
            if curr.l_child:
                return self.contains(val, curr.l_child)
            else:
                return False
        elif val > curr.value:
            if curr.r_child:
                return self.contains(val, curr.r_child)
            else:
                return False


class Node(object):
    """  """
    def __init__(self, val):
        self.value = val
        self.l_child = None
        self.r_child = None
