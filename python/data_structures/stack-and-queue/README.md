# Stacks and Queues
<!-- Short summary or background information -->

Code challenge to do a new implementation of Stack and Queue classes.
.
## Challenge
<!-- Description of the challenge -->

Node:
- Create a Node class that has properties for the value stored in the Node, and a pointer to the next node.

- Stack
- Create a Stack class that has a top property. It creates an empty Stack when instantiated.
- This object should be aware of a default empty value assigned to top when the stack is created.
- The class should contain the following methods:

- push
Arguments: value
adds a new node with that value to the top of the stack with an O(1) Time performance.

- pop
Arguments: none
Returns: the value from node from the top of the stack
Removes the node from the top of the stack
Should raise exception when called on empty stack

- peek
Arguments: none
Returns: Value of the node located at the top of the stack
Should raise exception when called on empty stack

- is empty
Arguments: none
Returns: Boolean indicating whether or not the stack is empty.

- Queue
Create a Queue class that has a front property. It creates an empty Queue when instantiated.
This object should be aware of a default empty value assigned to front when the queue is created.
The class should contain the following methods:

- enqueue
Arguments: value
adds a new node with that value to the back of the queue with an O(1) Time performance.

- dequeue
Arguments: none
Returns: the value from node from the front of the queue
Removes the node from the front of the queue
Should raise exception when called on empty queue

- peek
Arguments: none
Returns: Value of the node located at the front of the queue
Should raise exception when called on empty stack
is empty
Arguments: none
Returns: Boolean indicating whether or not the queue is empty

## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->

The Big 0 for time and space efficiency for Pop(), Push(), Peek() and is_empty() are all 0(1).
This is because all these functions are essentially looking at the top of the queue or stack.
Regardless of how many nodes are in the stack it will take the same time and space to run.


## API
<!-- Description of each method publicly available to your Stack and Queue-->

- push(), pop(), peek(), is_empty(), __str__(), __init__()

## Attributions

A special Thank you to Tammy Do my tutor. This challenge required less assistance
but she helped me troubleshoot my import issues and talk through my code. She has been a great help
and has made it easier for me to learn.

A special thank you to Adam Owada for demo'ing how to get this code challenge started.
