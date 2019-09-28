def helper(array, i, result, tmp_array):
    if len(tmp_array) == len(array):
        result.append([item for item in tmp_array])
        return 

    for j in range(len(array)):
        if array[j] is not None:
            tmp_array.append(array[j])
            array[j] = None
            helper(array, j, result, tmp_array)
            array[j] = tmp_array.pop()

def getPermutations(array):
    if not array:
        return []
    
    result = []
    helper(array, 0, result, [])
    return result

array = [1,2,3]
print(getPermutations(array))