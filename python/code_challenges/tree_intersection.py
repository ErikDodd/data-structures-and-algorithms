from data_structures.binary_tree import BinaryTree


def tree_intersection(tree1, tree2):
    if tree1.root is None:
        return
    if tree2.root is None:
        return
    values1 = set()
    values2 = set()
    results = []

    def depth_first(node, values):
        if node:
            values.add(node.val)
            depth_first(node.left, values)
            depth_first(node.right, values)

    depth_first(tree1, values1)
    depth_first(tree2, values2)

    for value in values1:
        if value in values2:
            results.append(value)

    return results




