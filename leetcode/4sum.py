def fourSum(nums, s):
    nums = sorted(nums)
    quadriplets_set = set()

    for i in range(len(nums)):
        threeSum = s-nums[i]
        for j in range(i+1, len(nums)):
            twoSum = threeSum-nums[j]
            index = {}
            for k in range(j+1, len(nums)):
                d = twoSum-nums[k]

                if nums[k] in index and index[nums[k]] < k:
                    quadriplets_set.add((nums[i],nums[j],nums[index[nums[k]]], nums[k]))

                index[d] = k


    quadriplets = []
    for q in quadriplets_set:
        quadriplets.append([q[0],q[1],q[2],q[3]])

    return quadriplets


#       0 1 2 3 4 5 6 7 8
# nums = [1, 0, -1, 0, -2, 2]
# target = 0

nums = [0,0,0,0,0,0]
target = 0

print(fourSum(nums, target))