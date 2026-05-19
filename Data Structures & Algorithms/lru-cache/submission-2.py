class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.next, self.prev = None, None

class LRUCache:

    def __init__(self, capacity: int):
       self.cap = capacity
       self.store = {}

       self.left, self.right = Node(0, 0), Node(0,0)
       self.left.next, self.right.prev = self.right, self.left

    # remove from LL
    def remove(self, node):
        nxt, prev = node.next, node.prev
        prev.next = nxt
        nxt.prev = prev

    # insert at the end of LL
    def insert(self, node):
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.prev, node.next = prev, nxt

    def get(self, key: int) -> int:
        if key in self.store:
            self.remove(self.store[key])
            self.insert(self.store[key])
            return self.store[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.store:
            self.remove(self.store[key])

        self.store[key] = Node(key, value)
        self.insert(self.store[key])

        if len(self.store) > self.cap:
            lru = self.left.next
            self.remove(lru)
            del self.store[lru.key]

        