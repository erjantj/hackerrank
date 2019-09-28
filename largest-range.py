def helper(nums_index, num):
    curr_range = []
    if num-1 not in nums_index:
        curr_range = [num,num]
    else:
        prev_range = helper(nums_index, num-1)
        curr_range = [prev_range[0], num]
    nums_index.remove(num)
    return curr_range

def largestRange(array):
    if not array:
        return [-1,-1]
    
    max_range = [1,0]
    nums_index = set(array)

    for num in array:
        if num not in nums_index:
            continue
        curr_range = helper(nums_index, num)
        print(num, curr_range)
        if curr_range[1]-curr_range[0] > max_range[1]-max_range[0]:
            max_range = curr_range
    return max_range

array = [1,11,3,0,15,5,2,4,10,7,12,6]
# array = [1]
print(largestRange(array))