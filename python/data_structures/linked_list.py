class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class LinkedList:
    pass

class LinkedList:

    def __init__(self):
        self.head = None
        self.next = next
        self.count = 0


    def __str__(self, head=None, next=None):
        current = self.head
        text = ""
        while current is not None:
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

    def append(self, new_value):
        if not self.head:
            self.head = Node(new_value, self.head)
        else:
            pointer = self.head
            while pointer.next:
                pointer = pointer.next
            pointer.next = Node(new_value, pointer.next)

    def insert_before(self, target_val, value_to_insert):
        current = self.head
        if not current:
            raise TargetError
        if current.value is target_val:
            placeholder = self.head
            new_node = Node(value_to_insert)
            self.head = new_node
            self.head.next = placeholder
            return self
        while current.next and current.next.value is not target_val:
            current = current.next
        if current.next and current.next.value is target_val:
            placeholder = current.next
            new_node = Node(value_to_insert)
            current.next = new_node
            current = current.next
            current.next = placeholder
            return self
        raise TargetError

    def insert_after(self, target_val, value_to_insert):
        current = self.head
        while current and current.value is not target_val:
            current = current.next
        if current and current.value is target_val:
            placeholder = current.next
            new_node = Node(value_to_insert)
            current.next = new_node
            current = current.next
            current.next = placeholder
            return self
        raise

    def kth_from_end(self, k):
        slow = fast = self.head
        if fast.next is None:
            return fast.value
        print(f"The value of fast: {fast.value}")
        print(f"The value of slow: {slow.value}")
        for i in range(k):
            if not fast:
                raise TargetError
        fast = fast.next
        print(f"The new value of fast: {fast.value}")
        while fast.next:
            fast = fast.next
            # print(f"The WHILE new value of fast: {fast.value}")
            slow = slow.next
            # print(f"The WHILE new value of slow: {slow.value}")
        if k == 0:
            return fast.value
        elif k == 1:
            return slow.value
        elif k == 2:
            return self.head.value



class TargetError(BaseException):

    def __int__(self):
        return self

    def __str__(self):
        return self
