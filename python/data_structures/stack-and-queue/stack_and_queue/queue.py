class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class Queue:
    """
    Put docstring here
    """

    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, value):
        if self.rear:
            self.rear.next = Node(value)
            self.rear = self.rear.next
            return
        self.rear = self.front = Node(value)

    def dequeue(self):
        if self.front is None:
            raise InvalidOperationError
        dequeued = self.front
        self.front = self.front.next

    def peek(self):
        # Returns: Value of the node located at the front of the queue
        # Should raise exception when called on empty stack
        pass

    def is_empty(self):
        # Returns: Boolean indicating whether or not the queue is empty
        if self.front is None:
            raise InvalidOperationError
        if self.front is not None:
            return self.value


class InvalidOperationError(Exception):
    def __int__(self):

    def __str__(self):
        return self
