def doMerge(array, tmp_array, left_start, right_end):
    left = left_start
    left_end = (left_start+right_end)//2
    right = left_end + 1
    index = left_start

    while left <= left_end and right <= right_end:
        if tmp_array[left] <= tmp_array[right]:
            array[index] = tmp_array[left]
            left += 1
        else:
            array[index] = tmp_array[right]
            right += 1
        index += 1

    while left <= left_end:
        array[index] = tmp_array[left]
        left += 1
        index += 1

    while right <= right_end:
        array[index] = tmp_array[right]
        right += 1
        index += 1

    for i in range(left_start, right_end+1):
        tmp_array[i] = array[i]
        
def sortPart(array, tmp_array, left_start, right_end):
    if left_start >= right_end:
        return 

    middle = (left_start+right_end)//2
    sortPart(array, tmp_array, left_start, middle)
    sortPart(array, tmp_array, middle+1, right_end)
    doMerge(array, tmp_array, left_start, right_end)

def mergeSort(array):
    tmp_array = array[:]
    sortPart(array, tmp_array, 0, len(array)-1)
    return array

array = [5,4,3,2,4,6,4,3,7,8]
array = [2,1]
array = [2]
array = []
print(mergeSort(array))

[2,3,3,4,4,4,5,6,7,8]


