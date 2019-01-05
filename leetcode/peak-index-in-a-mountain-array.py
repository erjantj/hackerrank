def peakIndexInMountainArray(arr):
    l = 0
    r = len(arr)-1

    while l <= r:
        middle = (r+l)//2
        if middle == len(arr) - 1:
            break
        elif arr[middle] <= arr[middle+1]:
            l = middle + 1
        else:
            r = middle - 1
    return l
            

arr = [0,2,4,5,6,10,3,2,1]
print(peakIndexInMountainArray(arr))