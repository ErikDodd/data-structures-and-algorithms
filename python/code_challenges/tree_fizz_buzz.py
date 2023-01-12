from data_structures.binary_tree import BinaryTree
from data_structures.kary_tree import KaryTree, Node
from code_challenges.queue import Queue


def fizz_buzz_tree(tree):
    fizzy_tree = KaryTree.clone(tree)
    if tree.root is None:
        return None
    queue = Queue()
    queue.enqueue(fizzy_tree.root)
    # We enter the while loop if there is something in the queue
    while not queue.is_empty():
        temp_dequeue_node = queue.dequeue()
        node_value = temp_dequeue_node.value
        node_value = fizz_buzz_helper(node_value)
        #print(f"The result of fizz_buzz_result: {node_value}")

        # add children to queue
        child_node_list = temp_dequeue_node.children
        for node in child_node_list:
            queue.enqueue(node)
    for node in fizzy_tree.root.children:
        print(node.value)
    #print(fizzy_tree.root.children)
    return fizzy_tree


def fizz_buzz_helper(value):
    if value % 3 == 0 and value % 5 == 0:
        return "FizzBuzz"
    if value % 3 == 0:
        return "Fizz"
    if value % 5 == 0:
        return "Buzz"
    else:
        return str(value)
