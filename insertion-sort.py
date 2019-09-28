import sys

def insertionSort(array):
    if not array or len(array) == 1:
        return array
    
    array = [-sys.maxsize] + array
    for i in range(1, len(array)):
        j = i - 1
        carry = array[i]
        while j >= 0 and array[i] < array[j]:
            array[j+1] = array[j]
            j -= 1
        array[j+1] = array[i]
    return array[1:]
            
array = [8,5,2,9,5,6,3]
# array = [8,5]
# array = [1,1,1,2,2,2,3,4]
print(insertionSort(array))