class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class LinkedList:
    pass


class LinkedList:
    def __init__(self):
        self.head = None


    def __str__(self, head=None):
        if self.head:
            return "NULL"

    linked_list = LinkedList()
    linked_list_head = Node(7)
    print(linked_list_head.value)

    def insert(self, value=None):
        new_node = Node(value)
        if self.head:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        else:
            self.head = new_node

    def includes(self, value):
        current = self.head
        while current != None:
            if current.data == value:
                return True
            current = current.next
        return False

    def __str__(self):
        pass


