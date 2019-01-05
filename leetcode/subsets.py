def helper(nums, result, tmp, depth = 0):
    if depth == len(nums):
        result.append([x for x in tmp if x is not None])
        return

    tmp[depth] = None
    helper(nums, result, tmp, depth + 1)
    tmp[depth] = nums[depth]
    helper(nums, result, tmp, depth + 1)
        
def subsets(nums):
    result = []
    tmp = [None]*len(nums)
    helper(nums, result, tmp)
    return result
    

nums = [1,2,3]
print(subsets(nums))

          #        []               
          #     /     \
          #   []       [1]           1
          #  /  \     /   \
          # []   [2] [1]   [1,2]     2
