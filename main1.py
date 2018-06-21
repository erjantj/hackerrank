def parseInput(f):
    return [f(x) for x in input().split()]

#!/bin/python3

import sys
from collections import defaultdict
from math import factorial
MOD=1000000007

if __name__ == "__main__":
    s = input().strip()
    n=len(s)
    dp=[defaultdict(int) for i in range(n)]
    for i in range(n):
        dp[i][s[i]]+=1
        if i > 0:
            for key,val in dp[i-1].items():
                dp[i][key]+=val

    q = int(input().strip())
    for a0 in range(q):
        l, r = input().strip().split(' ')
        l, r = [int(l)-1, int(r)-1]
        dif=defaultdict(int)
        for key,val in dp[r].items():
            dif[key]+=val

        if l > 0:
            for key,val in dp[l-1].items():
                dif[key]-=val

        evens=[]
        odds=[]
        for key,val in dif.items():
            if val % 2:
                odds.append(val)
            else:
                evens.append(val)
        total=sum(evens)//2
        for number in odds:
            total+=(number-1)//2
        answer=factorial(total)
        for number in evens:
            answer//=factorial(number//2)
        
        for number in odds:
            answer//=factorial((number-1)//2)
            
        if odds:
            answer*=len(odds)
        print(answer % MOD)