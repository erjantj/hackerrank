def search(nums, target):
    l = 0
    r = len(nums) - 1
    middle = 0

    for i in range(1, len(nums)):
        if nums[i] < nums[i-1]:
            middle = i


    found = False
    while l <= r:
        if nums[middle] == target:
            l = middle 
            found = True
            break
        if nums[middle] < target and target <= nums[r]:
            l = middle + 1
        else:
            r = middle - 1

        middle = (r+l)//2 

    if not found :
        return -1

    return l


nums = [2,4,5,6,0,1,2]
target = 2

print(search(nums, target))

