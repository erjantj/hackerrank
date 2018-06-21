import sys

modd = 10**9+7

def countArray(n,k,x):
    fake = 3
    memo = [[0]*(fake+1) for i in range(n+1)]
    memo[1][1] = 1
    memo[1][2] = 0
    memo[1][3] = 0

    for i in range(2, n+1):
        for j in range(1, fake+1):
            endedWithX = 0
            if memo[i-1][j] > 0:
                endedWithX= memo[i-1][j]

            memo[i][j] = ((memo[i-1][1]+(memo[i-1][fake]*(k-1))%modd)) - endedWithX
    if x == 1:
        return memo[n][1]
    return memo[n][fake]

with open('input.txt') as f:
    content = f.readlines()
    n,k,x = [int(x) for x in content[0].strip().split()]

    result = countArray(n,k,x)

    print(result)
    
