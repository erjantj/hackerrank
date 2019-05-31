def removeDuplicates(nums):
    k = 0
    prev_item = None
    count = 0
    
    for i in range(len(nums)):
        nums[k] = nums[i]

        if prev_item != nums[k]:
            count = 0
        count += 1
        
        prev_item = nums[k]
        if count <= 2:
            k += 1
    return k

nums = [0,0,1,1,1,1,1,1,2,2,2,3,3,3,3,3,4,5,5,5]
# nums = [0,0,1,1,2,2,3,3]
# nums = [0,1,2,3,4,5]
# nums = []
# nums = [0,0,0,0,0]
# nums = [1,1,1,1,1]
# nums = [1,1,1,1,1,1,1,1,1,1,1,1,1]
# nums = [1,1,1,1,1,1,2,2,2,2,2,2,2,2,2,2]
# nums = [1,1,1,1,1,1,2,2,2,2,2,2,2,2,2,2,3]
# nums = [0,0,0,1,1,1,3,3,4,4,4,5,5,5]

length = removeDuplicates(nums)

print(nums[:length])


