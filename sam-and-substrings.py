import sys
modd = 1000000007 

def substrings(n):
    memo = {}
    s = int(n[0])
    memo[0] = s
    prev = s
    n_len = len(n)

    for i in range(1, n_len):
        s = int(n[i])
        memo[i] = (s + memo[i-1]*10+s*i)%modd
        prev = (prev + memo[i])%modd

    return prev%modd

with open('input.txt') as f:
    content = f.readlines()
    n = content[0].strip()
    result = substrings(n)

    print(result)