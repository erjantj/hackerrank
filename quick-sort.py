def order(array, l, r, pivot):
    while l <= r:
        if array[l] < pivot:
            l += 1
        elif array[r] > pivot:
            r -= 1
        elif l <= r:
            array[l], array[r] = array[r], array[l]
            l += 1
            r -= 1
    return l - 1

def helper(array, l, r):
    if l >= r:
        return
    pivot = array[l]
    index = order(array, l+1, r, pivot)
    array[l], array[index] = array[index], array[l]
    helper(array, l, index-1)
    helper(array, index+1, r)
    
def quickSort(array):
    helper(array, 0, len(array)-1)
    return array

# array = [3,4,1,2,4,6,2,5,7]
# array = [5,4,3,2,1]
# array = [8,5,2,9,5,6,3]
print(quickSort(array))