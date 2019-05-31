def helper(arr, l, r, sums):
    tmp_max_sum = 0
    max_len = max(l,r)

    for i in range(len(sums)-max_len):
        l_sum = sums[i+l]-sums[i]
        for j in range(i+l, len(sums)-r):
            r_sum = sums[j+r]-sums[j]   
            if l_sum+r_sum > tmp_max_sum:
                tmp_max_sum = l_sum+r_sum

    return tmp_max_sum

def maxSumTwoNoOverlap(arr, l, m):
    if (l+m) > len(arr):
        return 0


    max_sum = 0
    sums = [0]

    for i in range(len(arr)):
        sums.append(sums[i]+arr[i])

    return max(helper(arr, l, m, sums), helper(arr, m, l, sums))


# A = [3,8,2,3,2,1,8,9,0]
# L = 4
# M = 2

# A = [0,6,5,2,2,5,1,9,4]
# L = 1
# M = 2

# A = [2,1,5,6,0,9,5,0,3,8]
# L = 4
# M = 3


# A = [2,1,5,6,0,9,5,0,3,8]
# L = 7
# M = 3
print(maxSumTwoNoOverlap(A,L,M))


# 3,8,2,3,2,1,8,9,0
# ^
