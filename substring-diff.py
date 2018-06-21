import sys

def solve(mid, s1_len, memo, k, s1, s2):
    for i in range(mid,s1_len+1):
        for j in range(mid, s1_len+1):
            delta = memo[i][j]-memo[i-mid][j-mid]

            if delta <= k:
                return True
    return False
                

def substringDiff(k, s1, s2):
    s1_len = len(s1)
    s2_len = len(s2)
    memo = [[0]*(s2_len+1) for i in range(s1_len+1)]

    for i in range(s1_len):
        for j in range(s2_len):
            if s1[i] == s2[j]:
                memo[i+1][j+1] = memo[i][j]
            else:
                memo[i+1][j+1] = memo[i][j] + 1


    low = 0
    hight = s1_len
    mid = 0

    while low < hight:
        mid = (hight+low)//2 + 1

        if solve(mid, s1_len, memo, k, s1, s2):
            low = mid 
        else:
            hight = mid - 1
    return low 


with open('input.txt') as f:
    content = f.readlines()
    t = int(content[0].strip())

    for i in range(t):
        k,s1,s2 = content[i+1].strip().split()
        k = int(k)
        print(substringDiff(k, s1, s2))

