from data_structures.binary_tree import BinaryTree
from data_structures.queue import Queue


def tree_intersection(tree1, tree2):
    if tree1.root is None:
        return
    if tree2.root is None:
        return

    results = []
    value_dict = {}
    tree1_queue = Queue()
    tree2_queue = Queue()
    tree1_queue.enqueue(tree1.root)

    while tree1_queue.front:
        temp = tree1_queue.dequeue()
        value_dict[temp.value] = "exists"
        if temp.left:
            tree1_queue.enqueue(temp.left)
        if temp.right:
            tree1_queue.enqueue(temp.right)

    tree2_queue.enqueue(tree2.root)
    while tree2_queue.front:
        temp = tree2_queue.dequeue()
        if temp.value in value_dict:
            results.append(temp.value)
        if temp.left:
            tree2_queue.enqueue(temp.left)
        if temp.right:
            tree2_queue.enqueue(temp.right)
    return set(results)








