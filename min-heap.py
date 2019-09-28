class MinHeap:
    def __init__(self, array):
        # Do not edit the line below.
        self.heap = self.buildHeap(array)
    
    # O(nlog(n)) time
    def buildHeap(self, array):
        self.heap = array
        first_parent = (len(self.heap)-2)//2
        for i in range(first_parent, -1, -1):
            print(self.heap)
            self.siftDown(i)
            print(self.heap)
        return self.heap
    
    # O(log(n)) time
    def siftDown(self, curr_i = 0):
        child_i = curr_i*2+2 if self.heap[curr_i*2+1] > self.heap[curr_i*2+2] else curr_i*2+1
        while child_i < len(self.heap) and self.heap[curr_i] > self.heap[child_i]:
            print('swap', (curr_i, child_i), self.heap[curr_i], self.heap[child_i])
            self.heap[curr_i], self.heap[child_i] = self.heap[child_i], self.heap[curr_i]
            if curr_i*2+1 >= len(self.heap):
                break
            if curr_i*2+2 >= len(self.heap):
                child_i = curr_i*2+1
            else:
                child_i = curr_i*2+2 if self.heap[curr_i*2+1] > self.heap[curr_i*2+2] else curr_i*2+1
    
    # O(log(n)) time
    def siftUp(self):
        curr_i = len(self.heap)-1
        parent_i = (curr_i-1)//2
        while parent_i >=0 and self.heap[parent_i] > self.heap[curr_i]:
            self.heap[curr_i], self.heap[parent_i] = self.heap[parent_i], self.heap[curr_i]
            curr_i = parent_i
            parent_i = (curr_i-1)//2

    # O(1) time
    def peek(self):
        return self.heap[0]
    
    # O(log(n)) time
    def remove(self):
        last_i = len(self.heap) - 1
        self.heap[0], self.heap[last_i] = self.heap[last_i], self.heap[0]
        value = self.heap.pop()
        self.siftDown()
        
        return value
    
    # O(log(n)) time
    def insert(self, value):
        # Write your code here.
        self.heap.append(value)
        self.siftUp()

# heap = MinHeap([1, 2, 3, 4, 5, 6, 7, 8, 9])
heap = MinHeap([9,8,7,6,5,4,3,2,1])
print(heap.heap)
# print(heap.remove())
# print(heap.remove())
# print(heap.remove())
# print(heap.remove())
# print(heap.remove())
# print(heap.remove())
