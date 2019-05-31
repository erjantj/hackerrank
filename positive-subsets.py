def helper(arr, tmp_max_sum, result, index):
    if index >= len(arr):
        if tmp_max_sum > 0:
            result[0] += 1
        return 
    
    helper(arr, tmp_max_sum, result, index+1)
    tmp_max_sum += arr[index]
    helper(arr, tmp_max_sum, result, index+1)
    tmp_max_sum -= arr[index]

def positive_subsets(arr):
    if not arr: 
        return 0

    result = [0]
    tmp_max_sum = 0
    
    helper(arr, tmp_max_sum, result, 0)

    return result[0]


arr = [-2,-1,2]
print(positive_subsets(arr))