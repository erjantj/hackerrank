import sys

def findPositionVal(nums1, nums2, i1, len1, i2, len2, k):
    print(nums1[i1:i1+len1], nums2[i2:i2+len2], k)
    if len1 == 0 and len2 > 0:
        return nums2[i2+k-1]
    if len2 == 0 and len1 > 0:
        return nums1[i1+k-1]
    if k == 1:
        return min(nums1[i1],nums2[i2])

    mid1 = min(len1, k//2)
    mid2 = min(len2, k//2)

    print(mid1, mid2)
    if nums1[i1+mid1-1] < nums2[i2+mid2-1]:
        return findPositionVal(nums1, nums2, i1+mid1, len1-mid1, i2, len2, k-mid1)
    else:
        return findPositionVal(nums1, nums2, i1, len1, i2+mid2, len2-mid2, k-mid2)

def findMedianSortedArrays(nums1, nums2):
    if not nums1 and not nums2:
        return 0

    n = len(nums1)
    m = len(nums2)

    i1 = (n+m-1)//2+1
    i2 = (n+m)//2+1

    return (findPositionVal(nums1, nums2, 0, len(nums1), 0, len(nums2), i1) +
        findPositionVal(nums1, nums2, 0, len(nums1), 0, len(nums2), i2))//2


# [3,4,5]
# [6,7,8,9,10]


# k = 2

# # ka = k//2 = 1
# # kb = k//2 = 1



# nums1 = [1,2,3,4,5]
# nums2 = [6,7,8,9,10]

nums1 = [1,2]
nums2 = [3,4]
print(findPositionVal(nums1, nums2, 0, len(nums1), 0, len(nums2), 4))
# print(findMedianSortedArrays(nums1, nums2))



