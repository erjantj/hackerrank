def kadanesAlgorithm(arr):
    if not arr:
        return 0
    l = r =0
    max_sum = curr_sum = arr[0]
    r = 1
    while r < len(arr):
        if curr_sum + arr[r] > 0:
            curr_sum += arr[r]
        else:
            l = r
            curr_sum = arr[l]
        r += 1

        max_sum = max(max_sum, curr_sum)
    return max_sum
    
arr = [3,5,-9,1,3,-2,3,4,7,2,-9,6,3,1,-5,4]
# arr = [4,-5,1,3,6,-9,2,7,4,3,-2,3,1,-9,5,3]

# arr = [1,3,5,-7,3,5,-7,3,2,4,6]
# arr = [-1,-2,-3,-4]
# arr = [-4]
# arr = [14,5,-11,5,5]
print(kadanesAlgorithm(arr))