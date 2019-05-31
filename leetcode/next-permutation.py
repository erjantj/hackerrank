def bubbleSort(nums, start_index):
    sorted = False

    while not sorted:
        sorted = True
        for i in range(start_index+1, len(nums)):
            if nums[i-1] > nums[i]:
                sorted = False
                nums[i-1],nums[i] = nums[i],nums[i-1]

def nextPermutation(nums):
    if not nums or len(nums) == 1:
        return

    i = len(nums)-1
    max_val = nums[i]
    max_index = i
    while i>0 and max_val <= nums[i-1]:
        max_val = nums[i-1]
        max_index = i-1
        i-=1
    i-=1

    if i < 0 and nums[0] > nums[1]:
        bubbleSort(nums, 0)


    min_diff = max_val-nums[i]
    min_diff_index = max_index

    for j in range(i+1, len(nums)):
        if nums[j] == nums[i]:
            continue
        diff = nums[j]-nums[i]
        if diff >= 0 and diff<min_diff:
            min_diff = nums[j]-nums[i]
            min_diff_index = j

    nums[i],nums[min_diff_index] = nums[min_diff_index],nums[i]
    bubbleSort(nums, i+1)

nums = [5,1,1]
# nums = [1,2,3,4,5]
# nums = [3,2,1,4,5]
# nums = [2,3,5,4,1]
# nums = [4,2,3,5,1]
# nums = [2,4,5,3,1]
# nums = [1,5,]

print(nextPermutation(nums))
print(nums)