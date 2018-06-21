 # Enter your code here. Read input from STDIN. Print output to STDOUT
with open('input2.txt') as f:
    content = f.readlines()

    n, k = [int(x) for x in content[0].split(" ")]
    items = [int(x) for x in content[1].split(" ")]

    heap = []
    heapSize = 0

    def insertItem(item):
        global heapSize

        heap.append(item)
        heapSize = heapSize + 1
        heapifyUp()

    def removeItem(index):
        global heapSize

        if index != heapSize - 1:
            heap[index],heap[heapSize-1] = heap[heapSize-1],heap[index]
            heapSize = heapSize - 1
            heapifyDown(index)
        else:
            heapSize = heapSize - 1

    def heapifyUp(index = None):
        global heapSize

        if not index:
            index = heapSize - 1

        parentIndex = (index-1)/2
        while parentIndex >= 0 and parentIndex < heapSize and heap[parentIndex] > heap[index]:
            heap[index], heap[parentIndex] =  heap[parentIndex], heap[index]
            index = parentIndex
            parentIndex = (index-1)/2
            
    def heapifyDown(index = None):
        global heapSize

        if not index:
            index = 0

        if heap[0] == heap[1] == heap[2]:
            return 

        leftChildIndex = (index*2)+1
        rightChildIndex = (index*2)+2

        if leftChildIndex >= heapSize:
            leftChildIndex = -1
        if rightChildIndex >= heapSize:
            rightChildIndex = -1
        
        while leftChildIndex >= 0 and leftChildIndex < heapSize:
            smallerChildIndex = leftChildIndex
            if rightChildIndex >= 0 and rightChildIndex < heapSize and heap[rightChildIndex] < heap[leftChildIndex]:
                smallerChildIndex = rightChildIndex
                
            if heap[index] > heap[smallerChildIndex]:
                heap[index], heap[smallerChildIndex] = heap[smallerChildIndex],heap[index]
            index = smallerChildIndex
            leftChildIndex = (index*2)+1
            rightChildIndex = (index*2)+2

            if leftChildIndex >= heapSize:
                leftChildIndex = -1
            if rightChildIndex >= heapSize:
                rightChildIndex = -1
    
    for i in xrange(n):
        insertItem(items[i])

    steps = 0

    while heap[0] < k and heapSize >= 2:
        secondSmallestIndex = 1

        if heapSize > 3 and heap[2] < heap[1]:
            secondSmallestIndex = 2

        c1 = heap[0]
        c2 = heap[secondSmallestIndex]
        
        # removeItem(secondSmallestIndex)
        heap[0] = 1*c1+2*c2
        heapifyDown()

        steps = steps + 1

    if heap[0] >= k:    
        print steps
    else:
        print -1