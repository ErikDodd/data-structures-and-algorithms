
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class Stack:
    """
    Put docstring here
    """

    def __init__(self):
        self.top = None

    def push(self, value=None):
        if self.top is None:
            self.top = Node(value)
            return
        old = self.top
        self.top = Node(value)
        self.top.next = old

    def pop(self):
        popped = self.top
        self.top = self.top.next
        return popped.value

    def peek(self):
        #Returns: Value of the node located at the top of the stack
        #Should raise exception when called on empty stack
        if self.top is None:
            raise InvalidOperationError
        if self.top is not None:
            return self.value

    def is_empty(self):
        if self.top is None:
            return True
        return False


class InvalidOperationError(Exception):
    def __int__(self):


    def __str__(self):
        return self
