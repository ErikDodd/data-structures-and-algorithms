from data_structures.binary_tree import BinaryTree, Node


class BinarySearchTree(BinaryTree):
    """
    Put docstring here
    """

    def __init__(self):
        # initialization here
        self.root = None

    # Adds a new node with that value in the correct location in the binary search tree.
    def add(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return self.root.value
        while True:
            if self.root.left is None:
                self.root.left = new_node
                return self.root.left.value
            if self.root.right is None:
                self.root.right = new_node
                return self.root.right.value






    def contains(self):
        #Returns: boolean indicating whether or not the value is in the tree at least once.
        pass
