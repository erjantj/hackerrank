def buildHeap(heap):
    start_index = (len(heap)-2)//2
    end_index = len(heap) - 1 
    for i in range(start_index, -1, -1):
        heapifyDown(heap, end_index, i)

def heapifyDown(heap, end_index, index):
    l_index = index*2+1
    r_index = index*2+2

    child_index = l_index
    if r_index <= end_index:
        child_index = l_index if heap[l_index] > heap[r_index] else r_index
    while child_index <= end_index and index >= 0 and heap[index] < heap[child_index]:
        heap[index], heap[child_index] = heap[child_index], heap[index]
        index = child_index
        l_index = index*2+1
        r_index = index*2+2
        child_index = l_index
        if r_index <= end_index:
            child_index = l_index if heap[l_index] > heap[r_index] else r_index

def heapSort(heap):
    buildHeap(heap)
    end_index = len(heap) - 1 
    heap[0], heap[end_index] = heap[end_index], heap[0]
    end_index -= 1
    while end_index >= 0:
        heapifyDown(heap, end_index, 0)
        heap[0], heap[end_index] = heap[end_index], heap[0]
        end_index -= 1
    return heap

array = [6,6,6,5,5,5,4,4]
array = [5,5,4,4,3,3,2,1]
print(heapSort(array))
    

