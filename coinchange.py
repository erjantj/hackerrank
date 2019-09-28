import sys

def numberOfWaysToMakeChange(n, denoms):
    if not n or not denoms:
        return 0
    
    dp = [sys.maxsize for _ in range(n+1)]
    dp[0] = 0

    for i in range(len(denoms)):
        for j in range(n+1):
            dp[j] = min(dp[j], dp[j-denoms[i]]+1)

    print(dp)
    return dp[n]
        

n = 8
denoms = [1,3,5]

print(numberOfWaysToMakeChange(n, denoms))

