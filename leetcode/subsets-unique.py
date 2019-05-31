def helper(nums, result, tmp, depth = 0):
    if depth == len(nums):
        a = []
        for x in tmp:
            if x != None:
                a.append(x)
        k = ",".join(str(x) for x in a)
        result[k] = a
        return

    tmp[depth] = None
    helper(nums, result, tmp, depth + 1)
    tmp[depth] = nums[depth]
    helper(nums, result, tmp, depth + 1)
        
def subsets(nums):
    nums.sort()
    result = {}
    tmp = [None]*len(nums)
    helper(nums, result, tmp)
    return [x for x in result.values()]
    

nums = [4,4,4,1,4]
print(subsets(nums))

