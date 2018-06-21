import sys

def countArray(n,k,x):
    memo = [[0]*(k+1) for i in range(n+1)]
    memo[1][1] = 1

    for i in range(2, n+1):
        for j in range(1, k+1):
            memo[i][j] = sum(memo[i-1]) - memo[i-1][j]
    
    print(memo)
    return memo[n][x]

with open('input.txt') as f:
    content = f.readlines()
    n,k,x = [int(x) for x in content[0].strip().split()]

    result = countArray(n,k,x)

    print(result)
    
