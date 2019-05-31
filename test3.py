def helper(a,k,n,result,i):
    if i >= n:
        return 0

    if result[i] > -1:
        return result[i]
    
    maxx = a[i]
    max_sum = a[i]
    for j in range(i,min(i+k,n)):
        if a[j] > maxx:
            maxx = a[j]

        prev_sum = helper(a,k,n,result, j+1)
        max_sum = max(max_sum, (maxx*(j-i+1)+prev_sum))

    result[i] = max_sum
    return result[i]

def maxSumAfterPartitioning(a, k):
    n = len(a)
    if not a:
        return 0
    if k == 1:
        return sum(a)

    result = [-1 for i in range(n)]

    return helper(a,k,n,result,0)


a = [2,3]
k = 1

print(maxSumAfterPartitioning(a,k))