def shiftedBinarySearch(array, target):
    if not array:
        return -1
    
    l = 0
    r = len(array) - 1

    while l <= r:
        mid = (l+r)//2
        print('mid', array[mid])
        if target == array[mid]:
            return mid
        elif target == array[l]:
            return l
        elif target == array[r]:
            return r
        elif array[l] <= array[mid] and target > array[l] and target < array[mid]:
            print('go left')
            r = mid - 1
        elif array[l] > array[mid] and (target > array[l] or target < array[mid]):
            print('go left')
            r = mid - 1
        else:
            print('go right')
            l = mid + 1

    return -1

target = 1
# array = [3,4,5,1,2]
array = [6,7,1,2,3,4,5]

# target = 33
# array = [45,61,71,72,73,0,1,21,33,44]

# target = 4
# array = [5,6,1,2,3,4]

print(shiftedBinarySearch(array, target))