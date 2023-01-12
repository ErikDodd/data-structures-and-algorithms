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
        new_node = Node(value)
        if self.front is None:
            self.front = new_node

        if self.rear:
            self.rear.next = new_node
            self.rear = new_node
        else:
            self.rear = new_node
        return
        # if self.rear:
        #     self.rear.next = Node(value)
        #     self.rear = self.rear.next
        #     return
        # self.rear = self.front = Node(value)

    def dequeue(self):
        if self.front is None:
            raise InvalidOperationError

        # Adam refactored this to get CC 17 to pass tests
        # not sure if I need to actually need to adjust this
        # since Tammy helped me refactor enqueue()

        if self.front == self.rear:
            dequeued = self.front
            self.front = self.rear = None
            return dequeued.value

        dequeued = self.front
        self.front = self.front.next
        return dequeued.value



    def peek(self):
        # Returns: Value of the node located at the front of the queue
        # Should raise exception when called on empty stack
        pass

    def is_empty(self):
        return self.front is None
        # Returns: Boolean indicating whether or not the queue is empty
        #if self.front is None:
           # return None
       # if self.front is not None:
           # return self


class InvalidOperationError(Exception):
    def __int__(self):
        pass

    def __str__(self):
        return self
