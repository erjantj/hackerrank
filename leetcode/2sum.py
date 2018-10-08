def twoSum(nums, value):
    index = {}
    visited = {}
    for i in range(len(nums)):
        index[value-nums[i]] = nums[i]
        visited[value-nums[i]] = False
        visited[nums[i]] = False


    sums = []
    for i in range(len(nums)):
        if index.get(nums[i], None) and not visited.get(nums[i], True):
            sums.append([nums[i], index[nums[i]]])
            visited[nums[i]] = True
            visited[index[nums[i]]] = True
    return sums



nums = [1,2,3,4,6,8,10]
print(twoSum(nums, 10))






