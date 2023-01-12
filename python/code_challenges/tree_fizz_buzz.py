from data_structures.binary_tree import BinaryTree
from data_structures.kary_tree import KaryTree, Node
from code_challenges.queue import Queue


def fizz_buzz_tree(tree):
    # Make a copy of the KaryTree using Clone
    fizzy_tree = KaryTree.clone(tree)
    # Check to see if the KaryTree is Empty
    if tree.root is None:
        return None
    queue = Queue()
    # Add the root of the tree to the queue
    queue.enqueue(fizzy_tree.root)
    # We enter the while loop if there is something in the queue
    while not queue.is_empty():
        temp_dequeue_node = queue.dequeue()
        temp_dequeue_node.value = fizz_buzz_helper(temp_dequeue_node.value)
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
    elif value % 3 == 0:
        return "Fizz"
    elif value % 5 == 0:
        return "Buzz"
    else:
        return str(value)
