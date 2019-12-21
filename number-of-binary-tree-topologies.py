def numberOfBinaryTreeTopologies(n):
    dp = {}
    dp[0] = 0
    dp[1] = 1
    dp[2] = 2

    for i in range(3, n+1):
        dp[i] = 0
        for x in range(0, i):
            right_items = x or 1
            left_items = i-1-x or 1

            dp[i] += (dp[left_items]*dp[right_items])
    return dp[n]

n = 5
print(numberOfBinaryTreeTopologies(n))

