class BinaryTree:
    """
    Put docstring here
    """

    def __init__(self):
        # initialization here
        self.root = None

    def post_order(self, root=None, nodes=None):
        # method body here
        if root is None:
            root = self.root
        if nodes is None:
            nodes = []
        if root.left:
            self.post_order(root.left, nodes)
        if root.right:
            self.post_order(root.right, nodes)
        nodes.append(root.value)
        return nodes

    def pre_order(self, root=None, nodes=None):
        if root is None:
            root = self.root
            print(root)
        if nodes in None:
            nodes = []
        if root.left:
            self.pre_order(root.left)
        if root.right:
            self.pre_order(root.right)




class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
