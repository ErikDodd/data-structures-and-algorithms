from data_structures.binary_tree import BinaryTree
from code_challenges.queue import Queue
def breadth_first(tree):
    results = []
    queue = Queue()
    if tree.root is None:
        return results
    queue.enqueue(tree.root)
    # We enter the while loop if there is something in the stack
    while not queue.is_empty():
        popped_node = queue.dequeue()
        results.append(popped_node.value)
        #print(f"The value of popped node: {popped_node.value}")
        if popped_node.left:
            queue.enqueue(popped_node.left)
        if popped_node.right:
            queue.enqueue(popped_node.right)
    return results





