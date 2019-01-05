import sys

def helper(nums1, nums2, start1, start2, k):
    if start1 > len(nums1) - 1:
        return nums2[start2+k-1]
    if start2 > len(nums2) - 1:
        return nums1[start1+k-1]

    if k == 1:
        return min(nums1[start1], nums2[start2])

    k1 = sys.maxsize
    k2 = sys.maxsize

    if start1+k//2-1 < len(nums1):
        k1 = nums1[start1+k//2-1]
    if start2+k//2-1 < len(nums2):
        k2 = nums2[start2+k//2-1]

    if k2 < k1:
        return helper(nums1, nums2, start1, start2+k//2, k-k//2)
    else:
        return helper(nums1, nums2, start1+k//2, start2, k-k//2)

def findMedianSortedArrays(nums1, nums2):
    len1 = len(nums1)
    len2 = len(nums2)

    start1 = 0
    start2 = 0
    k1 = (len1+len2+1)//2
    k2 = (len1+len2+2)//2

    return (helper(nums1, nums2, start1, start2, k1)+helper(nums1, nums2, start1, start2, k2))/2

# nums1 = [1, 2]
# nums2 = [3, 4, 5, 6]

nums1 = [1,2,4,5]
nums2 = [6]

# nums1 = [3,5,6]
# nums2 = [2,4,7,8,9]

# nums1 = [2,3,4]
# nums2 = [5,6,7,8,9]
 
# nums1 = []
# nums2 = [1]


print(findMedianSortedArrays(nums1, nums2))

# 2,3,4,5,6,7,8,9  k & k-1 
#       ^ ^

# k = 3/2 = 1
# 1)      
# 3,5,6
# 2,4,7,8,9

# 2,3,4,5,6,7,8,9
#         ^ ^

# k = 2/2 = 1
# 2)
# 6
# 7,8,9

# 2,4,5,6,7
#   ^ ^


# 3)
# 5
# 4,7

# 4,5,7
#   ^ 


