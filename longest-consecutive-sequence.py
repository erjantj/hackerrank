def longestConsecutive(nums):
    if not nums:
        return 0

    nums_index = {}
    for i in range(len(nums)):
        nums_index[nums[i]] = 0

    for num,count in nums_index.items():
        if num-1 not in nums_index:
            tmp_num = num + 1
            nums_index[num] = 1
            while tmp_num in nums_index:
                nums_index[num] += 1
                tmp_num += 1

    return max(nums_index.values())


# nums = [100, 4, 200, 1, 3, 2]
# nums = [21,5,6,1,7,2,8,9,3,10,20]
# nums = [1,2,0,1]
nums = [1,2]
# nums = [1,3,5,2,4]
print(longestConsecutive(nums))