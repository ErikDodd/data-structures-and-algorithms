class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class LinkedList:
    pass


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self, head=None, next=None):
        current = self.head
        text = ""
        while current:
            node_string = "{ " + current.value + " } -> "
            text += node_string
            current = current.next
        return text + "NULL"


    linked_list = LinkedList()

    def insert(self, value=None):
        insert_node = Node(value)
        previous_head = self.head
        self.head = insert_node
        self.head.next = previous_head

    def includes(self, value):
        current = self.head
        while current is None:
            if current == value:
                return False
            current = current.next
        return True
