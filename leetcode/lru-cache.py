class LRUCache:

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.lru = {}
        self.key_index = []

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.lru:
            index = self.key_index.index(key)
            value = self.lru[key]

            self.key_index.pop(index)
            self.key_index.append(key)

            return value
        return -1
        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """        
        if key not in self.lru:
            if len(self.key_index) >= self.capacity:
                old_key = self.key_index.pop(0)
                print(old_key)
                del self.lru[old_key]
        else:
            self.get(key)
        
        if key not in self.lru:
            self.key_index.append(key)
        self.lru[key] = value

# Your LRUCache object will be instantiated and called as such:
cache = LRUCache(2)
cache.put(2, 1)
cache.put(1, 1)
cache.put(2, 3)
cache.put(4, 1)
print(cache.get(1))
print(cache.get(2))


