class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def __repr__(self):
        if not self.head:
            return "NULL"
        current = self.head
        string = ""
        while current:
            string += str(current.value) + " -> "
            current = current.next
        str += "NULL"
        return string


    def insert(self, item):
        old = self.head
        self.head = Node(item)
        self.head.next = old



class Hashtable:
    """
    Put docstring here
    """

    def __init__(self, size=1024):
        # initialization here
        self.size = size
        self._buckets = [None] * size


    def _hash(self, key):
        # method body here
        hash = 0
        for char in key:
            hash += ord(char)
        hash = (hash * 19) % self.size
        return hash


    def set(self, key, value):
        hashed_key = self._hash(key)
        bucket = self._buckets[hashed_key]
        if not bucket:
            self._buckets[hashed_key] = LinkedList()
        self._buckets[hashed_key].insert([key, value])


    def get(self, key):
        hashed_key = self._hash(key)
        bucket = self._buckets[hashed_key]
        current = bucket.head
        while current:
            if current.value[0] == key:
                return current.value[1]
            current = current.next
        raise KeyError(f"Key not found: {key}")


    def has(self, key):
        return key in self._buckets


    def keys(self):
        return list(self._buckets.keys())
