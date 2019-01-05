def searchRange(nums, target):
    l = start = 0
    r = end = len(nums) - 1
    found = False

    while l <= r:
        middle = (l+r)//2
        if nums[middle] == target:
            l = middle
            found = True
            break
        elif nums[middle] < target:
            l = middle + 1
        else:
            r = middle - 1

    if not found:
        return [-1,-1]

    start = l
    while nums[start] == target and start >= 0:
        start -= 1
    start += 1

    end = l
    while end < len(nums) and nums[end] == target:
        end += 1
    end -= 1

    return [start, end]



nums = [5,5,5,5]
target = 5
print(searchRange(nums, target))
