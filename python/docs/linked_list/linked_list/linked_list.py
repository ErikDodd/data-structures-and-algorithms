class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class Linked_List:
    def __init__(self):
        self.head = None

    linked_list = Linked_List()
    linked_list_head = Node(7)
    print(linked_list_head.value)

    def insert(self, value=None):
        newNode = Node(value)
        if(self.head):
            current = self.head
            while(current.next):
                current = current.next
            current.next = newNode
        else:
            self.head = newNode


    def includes(self, value):
        current = self.head
        while current != None:
            if current.data == value:
                return True
            current = current.next
        return False



    def __str__(self, value):
        return f"{ a } -> { b } -> { c } -> NULL"



def insert_linked_list(self):
    pass


def head(self):
    pass


def insert_multiple_nodes(self):
    pass


def value_in_linked_list(self):
    pass


def value_not_in_linked_list(self):
    pass


def collection_values_in_linked_list(self):
    pass
