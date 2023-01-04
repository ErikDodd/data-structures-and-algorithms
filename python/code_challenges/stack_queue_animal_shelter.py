class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class AnimalShelter:
    def __init__(self):
        self.front = None
        self.rear = None


    def enqueue(self, animal):
        if self.rear is None:
            temp = Node(animal)
            self.rear.push(temp)
            return self
        if self.rear:
            temp = Node(animal)
            self.rear


        pass
        #if self.rear:
            #self.rear.next = Node(animal)
            #self.rear = self.rear.next
            #return
        #self.rear = self.front = Node(animal)


    def dequeue(self, perf):

        pass
        #if self.front is None:
            #raise InvalidOperationError
        #dequeued = self.front
        #self.front = self.front.next

    class InvalidOperationError(Exception):
        def __int__(self):
            pass
        def __str__(self):
            return self


class Dog:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next



class Cat:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next
