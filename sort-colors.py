def sortColors(nums):
    i = j = 0
    for k in range(len(nums)):
        print(nums, 'k=', k, 'i=', i, 'j=', j)
        v = nums[k]
        nums[k] = 2
        if v < 2:
            nums[j] = 1
            j += 1
        if v == 0:
            nums[i] = 0
            i += 1

        print(nums, 'k=', k, 'i=', i, 'j=', j)
        print()

    return nums

# def sortColors(nums):
#     if not nums:
#         return nums
#     n = len(nums)
#     i0 = 0
#     i2 = n-1

#     for i in range(n):
#         # print(nums, 'i=', i, 'i0=',i0,'i2=',i2)
#         if i > i2:
#             break

#         if nums[i0] == 0:
#             i0 = i

#         if nums[i] == 1:
#             continue
#         elif nums[i] == 0:
#             nums[i] = 1
#             nums[i0] = 0
#             i0 += 1
#         elif nums[i] == 2:
#             nums[i] = 1

#             while i2 >= i0 and nums[i2] == 2:
#                 i2 -= 1

#             if nums[i2] == 0:
#                 nums[i0] = 0
#                 i0 += 1
#             nums[i2] = 2

#     return nums

nums = [2,0,2,1,1,0]
##nums = []
# nums = [0]
# nums = [1]
# nums = [2]

# nums = [0,0,0,0,0,0,0]
# nums = [1,1,1,1,1,1,1]
# nums = [2,2,2,2,2,2,2]


# nums = [2,2,2,2,0,0,0]
# nums = [2,2,2,2,1,1,1]
# nums = [2,2,0,0,0,2,1]

# nums = [0,1,2,0,1,2,0,1,2,0,1,2,0]

# nums = [0,1,2,0,1,2,0,1,2,0,1,2,0,1,2,0,1,2,0,1,2,0,1,2,0,1,2,0,1,2]
# nums = [2,1,0,2,1,0,2,1,0,2,1,0,2,1,0,2,1,0,2,1,0,2,1,0,2,1,0,2,1,0]
# nums = [2,1,1,2,2,1,1,2,2,1,1,2,2,1,1,2,2,1,1,2,2,1,1,2,2,1,1,2,2,1,1,2,2,1,1,2]
print(sortColors(nums))