import sys
from math import factorial

memo = {}
e = {}
maxKey = 1
freqs = []
mod = 10 ** 9 +7
factors = []

def getFreqs(l,r):
    leftIndex = l-1
    rightIndex = r-1

    leftBlock = [0]*26
    rightBlock = []

    if leftIndex > 0:
        leftBlock = freqs[leftIndex-1]
    rightBlock = freqs[rightIndex]

    sub_freqs = []
    for i in range(26):
        f = rightBlock[i] - leftBlock[i]
        if f:
            sub_freqs.append(f)

    return tuple(sub_freqs)

def polindromes(l,r):
    if l == r:
        return 1

    ff = getFreqs(l,r)
    if ff in e:
        return e[ff]

    k = 0
    num = 0
    d = 1
    for f in ff:
        fi = 0
        if f%2 == 0:
            fi = f//2
        else:
            fi = (f-1)//2
            k +=1   
        num += fi

        if fi in memo:
            fact = memo[fi]
        else:
            fact = factorial(fi)
            memo[fi] = fact
        d *= fact

    if num != 0:
        if num in memo:
            numFact = memo[num]
        else:
            numFact = factorial(num)
            memo[num] = numFact
        num = numFact

    result = num//d
    if k > 0:
        result = result*k
    if result == 0:
        result = k

    e[ff] = result%mod 
    return e[ff]

with open('input2.txt') as f:
    content = f.readlines()
    s = content[0].strip()
    n = int(content[1].strip())
    s_len = len(s)

    freqs = [0]*s_len
    tmp_freq = [0]*26
    factors = [0]*s_len
    for i in range(s_len):
        c = s[i]
        tmp_freq[ord(c)-97] += 1
        freqs[i] = tmp_freq.copy()
        # factors[i] = factorial(i)
    # for i in range(2, n+2):
    #     l,r = [int(x) for x in content[i].strip().split()]
    #     print(polindromes(l,r))
        
