import sys

def helper(nums1, start1, nums2, start2, k):
    print()
    print(nums1[start1:], nums2[start2:], k)

    if start1 > len(nums1) - 1:
        return nums2[start2 + k - 1]

    if start2 > len(nums2) - 1: 
        return nums1[start1 + k - 1]

    if k == 1:
        return min(nums1[start1], nums2[start2])
    
    mid1 = sys.maxsize
    mid2 = sys.maxsize

    if start1 + k//2 - 1 < len(nums1):
        mid1 = nums1[start1 + k//2 - 1] 
        print(nums1[start1:], start1 + k//2 - 1, nums1[start1 + k//2 - 1])

    if start2 + k//2 - 1 < len(nums2):
        mid2 = nums2[start2 + k//2 - 1]        
        print(nums2[start2:], start2 + k//2 - 1, nums2[start2 + k//2 - 1])
    
    print('mid1=', mid1)
    print('mid2=', mid2)

    if mid1 < mid2:
        # Check: nums1Right + nums2Left 
        return helper(nums1, start1 + k//2, nums2, start2, k - k//2) 
    else:
        # Check: nums2Right + nums1Left
        return helper(nums1, start1, nums2, start2 + k//2, k - k//2) 

    
def findMedianSortedArrays(nums1, nums2):
    m = len(nums1)
    n = len(nums2)

    l = (m + n + 1) // 2
    r = (m + n + 2) // 2

    return (helper(nums1, 0, nums2, 0, l) + helper(nums1, 0, nums2, 0, r)) / 2

# nums1 = [1, 2]
# nums2 = [3, 4, 5, 6]

nums1 = [1,2,4,5]
nums2 = [6]

# nums1 = [3,5,6]
# nums2 = [2,4,7,8,9]

# nums1 = [2,3,4]
# nums2 = [5,6,7,8,9]


print(findMedianSortedArrays(nums1, nums2))

# 2,3,4,5,6,7,8,9
#       ^ ^
# k = 4/2 = 2
# 1)      
# 3,5,6
# 2,4,7,8,9

# 2,3,4,5,6,7,8,9
#       ^   ^

# 2)
# 5,6
# 2,4,7

# 2,4,5,6,7
#   ^ ^


# 3)
# 5
# 4,7

# 4,5,7
#   ^ 


