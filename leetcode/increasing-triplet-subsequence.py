import sys
def increasingTriplet(nums):
    if not nums:
        return False

    if len(nums) < 3:
        return False

    triplet = [sys.maxsize,sys.maxsize,sys.maxsize]

    for i in range(len(nums)):
        for k in range(3):
            if triplet[k] >= nums[i]:
                triplet[k] = nums[i]
                
                if k >= 2:
                    return True
                break
    return False
                



# nums = []
# nums = [1,2]
# nums = [1,2,3]
# nums = [5,4]
# nums = [5,4,3]
# nums = [5,3,4]
# nums = [0,0,0,0]
# nums = [1,2,3,4,5]
# nums = [5,4,3,2,1]
# nums = [10,8,5,6,2,3,4,9]
# nums = [10,8,5,6,2,3,4,1,5]
# nums = [10,8,5,6,2,1,5]
# nums = [10,8,1,4,3,5,6]
# nums = [5,1,5,5,2,5,4]
# nums = [5,2,5,5,3,3,4,1,5,4]
# nums = [5,2,5,5,1,5,2,5,4]
# nums = [2,5,1,6]
# nums = [5,6,1,2,3]

print(increasingTriplet(nums))