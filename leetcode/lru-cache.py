class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}
        self.head = None
        self.tail = None

    def print(self, head = None):
        if not head:
            head = self.head
        if head.next:
            self.print(head.next)


    def get(self, key):
        if key in self.cache:
            node = self.cache[key]
            if node == self.head and len(self.cache) > 1:
                self.head = node.next

            if node != self.tail:
                pre = node.prev
                nex = node.next

                node.next = None
                node.prev = self.tail
                self.tail.next = node
                self.tail = node
                
                if pre:
                    pre.next = nex
                if nex:
                    nex.prev = pre


            return node.value

        return -1

    def reduce(self):
        if len(self.cache) > self.capacity:
            new_head = self.head.next
            key = self.head.key

            new_head.prev = None
            self.head.next = None
            self.head = new_head

            del self.cache[key]

    def put(self, key, value):
        node = Node(key, value)

        if not self.head:
            self.head = node
            self.tail = node
        else:
            if not key in self.cache:
                node.prev = self.tail
                self.tail.next = node
                self.tail = node
            else:
                node = self.cache[key]
                node.value = value
                self.get(key)

        self.cache[key] = node
        self.reduce()

# Your LRUCache object will be instantiated and called as such:
cache = LRUCache(1)

cache.put(1,1)
cache.put(2,2)
cache.put(3,3)
cache.put(4,4)

print(cache.get(1))
print(cache.get(4))
print(cache.get(3))
print(cache.get(2))
cache.put(5,5)
print(cache.get(5))
# print(cache.get(3))
# cache.put(6,6)
# print(cache.get(2))