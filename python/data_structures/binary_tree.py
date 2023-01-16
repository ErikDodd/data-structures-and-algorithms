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
            #return
        if nodes is None:
            print("Nodes is None")
            nodes = []
        #print(root.value)
        nodes.append(root.value)
        if root.left:
            self.pre_order(root.left, nodes)
        if root.right:
            self.pre_order(root.right, nodes)
        return nodes

    def in_order(self, root=None, nodes=None):
        # method body here
        if root is None:
            root = self.root
        if nodes is None:
            nodes = []
        if root.left:
            self.in_order(root.left, nodes)
        #print(root.value)
        nodes.append(root.value)
        if root.right:
            self.in_order(root.right, nodes)
        return nodes

    def find_maximum_value(self):
        if self.root is None:
            return None
        nodes = self.pre_order()
        # nodes = [1,2,3,4,5,2]
        max_value = float('-inf')
        for value in nodes:
            if max_value < value:
                max_value = value
        return max_value









class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
