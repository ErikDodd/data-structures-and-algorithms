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
        current = self.root
        while True:
            if value < current.value:
                if current.left is None:
                    current.left = new_node
                    return current.left.value
                    break
                current = current.left
            else:
                if current.right is None:
                    current.right = new_node
                    return current.right.value
                    break
                current = current.right

    # Returns: boolean indicating whether or not the value is in the tree at least once.
    def contains(self, value):
        current = self.root
        while current:
            if current.value == value:
                return True
            elif value < current.value:
                current = current.left
            else:
                current = current.right
        return False




