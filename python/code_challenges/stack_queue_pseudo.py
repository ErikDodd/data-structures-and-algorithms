class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class Stack:

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
        if self.top is None:
            raise InvalidOperationError
        popped = self.top
        self.top = self.top.next
        return popped.value

    def peek(self):
        # Returns: Value of the node located at the top of the stack
        # Should raise exception when called on empty stack
        if self.top is None:
            raise InvalidOperationError
        if self.top is not None:
            return self.top.value

    def is_empty(self):
        if self.top is None:
            return True
        return False



class PseudoQueue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.stack_a = Stack()
        self.stack_b = Stack()

    def enqueue(self, value):
        #Inserts a value into the PseudoQueue, using a first-in, first-out approach.
        while self.stack_b.top:
            temp = self.stack_b.pop()
            self.stack_a.push(temp)
        if not self.stack_b.top:
            self.stack_a.push(value)


    def dequeue(self):
        while self.stack_a.top:
            temp = self.stack_a.pop()
            self.stack_b.push(temp)
        return self.stack_b.pop()

class InvalidOperationError(Exception):
    def __int__(self):
        pass
        # print("This is an Invalidation Operation")

    def __str__(self):
        return "Method not allowed on empty collection"
