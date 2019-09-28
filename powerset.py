def helper(array, i, result, tmp_result):
    if i >= len(array):
        result.append([item for item in tmp_result if item is not None])
        return

    tmp_result.append(array[i])
    helper(array, i+1, result, tmp_result)
    tmp_result.pop()
    helper(array, i+1, result, tmp_result)

def powerset(array):
    if not array:
        return [[]]

    result = []
    helper(array, 0, result, [])
    return result

array = [1,2,3]
print(powerset(array))