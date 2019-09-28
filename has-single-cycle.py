def getTargetIndex(arr, i):
    target_index = i+arr[i]
    if abs(target_index) >= len(arr):
        target_index = target_index%len(arr)
    return target_index if target_index >= 0 else len(arr)+target_index

def hasSingleCycle(arr):
    counter = i = 0
    while counter < len(arr):
        target_index = getTargetIndex(arr, i)
        i = target_index
        counter += 1

        if i == 0:
            break

    return counter == len(arr) and i == 0


# arr = [2,3,1,-4,-4,2]
# arr = [1,2,3,4]
# arr = [1,1,-5]
# arr = [-4]
# arr = [1,-1,1,-1]
# arr = [4,1,1,1]
print(hasSingleCycle(arr))


