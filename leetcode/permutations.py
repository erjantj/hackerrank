def helper(nums, freqs, tmp, result, depth = 0):
    if depth == len(nums):
        result.append(list(tmp))
        return 

    for i in range(len(nums)):
        if freqs[i] >= 1:
            tmp[depth] = nums[i]
            freqs[i] -= 1
            helper(nums, freqs, tmp, result, depth+1)
            freqs[i] += 1

def permute(nums):
    result = []
    freqs = [1]*len(nums)
    tmp = [0]*len(nums)

    helper(nums, freqs, tmp, result)

    return result

nums = [1,2,3]
print(permute(nums))


# [1,2,3],
# [1,3,2],
# [2,1,3],
# [2,3,1],
# [3,1,2],
# [3,2,1]

#     1
#    / \
#   2 - 3
#  