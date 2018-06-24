def minuteToWinIt(a, k):
    memo = {}
    a_len = len(a)

    maxSame = 0

    for i in range(a_len):
        first = a[i]-i*k
        if first not in memo:
            memo[first] = 0
        memo[first] += 1

        if memo[first] > maxSame:
            maxSame = memo[first]
    
    return a_len-maxSame

k = 2
print(minuteToWinIt([3,4,5,7,9,85], k))