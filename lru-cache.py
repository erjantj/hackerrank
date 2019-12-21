class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None
            
class LRUCache:
    def __init__(self, maxSize):
        self.maxSize = maxSize or 1
        self.cache = {}
        self.head = None
        self.tail = None

    def evict(self):
        key = self.tail.key
        self.tail = self.tail.prev
        self.tail.next = None
        del self.cache[key]

    def makeRecent(self, node):
        if node == self.head:
            return
        if node.prev:
            node.prev.next = node.next
            if node == self.tail:
                self.tail = node.prev
        if node.next:
            node.next.prev = node.prev
        node.prev = None
        self.head.prev = node
        node.next = self.head
        self.head = node

    def insertKeyValuePair(self, key, value):
        node = None
        if key in self.cache:
            node = self.cache[key]
            node.value = value
        else:
            node = Node(key, value)
            self.cache[key] = node
            if not self.head:
                self.head = node
                self.tail = node
        if len(self.cache) > 1:
            self.makeRecent(node)
        if len(self.cache) > self.maxSize:
                self.evict()

    def getValueFromKey(self, key):
        if key not in self.cache:
            return None
        node = self.cache[key]
        self.makeRecent(node)
        return self.cache[key].value

    def getMostRecentKey(self):
        if len(self.cache) == 0:
            return None
        return self.head.key


cache = LRUCache(3)
cache.insertKeyValuePair('a',1)
cache.insertKeyValuePair('b',2)
cache.insertKeyValuePair('c',3)
print(cache.getMostRecentKey())
print(cache.getValueFromKey('a'))
print(cache.getMostRecentKey())
