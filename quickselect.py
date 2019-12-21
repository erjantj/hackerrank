def order(array, l, r, pivot):
    while l <= r:
        if array[l] < pivot:
            l += 1
        elif array[r] > pivot:
            r -= 1
        else:
            array[l], array[r] = array[r], array[l]
            l += 1
            r -= 1
    return l - 1

def helper(array, l, r, k):
    while l < r:
        pivot = array[l]
        index = order(array, l+1, r, pivot)
        array[l], array[index] = array[index], array[l]
        print(array, index)

        if k < index:    
            r = index-1
        elif k > index:
            l = index+1
        else:
            break

def quickselect(array, k):
    k -= 1
    helper(array, 0, len(array)-1, k)
    return array[k]

array = [8,5,2,9,5,6,3]
print(quickselect(array, 1))