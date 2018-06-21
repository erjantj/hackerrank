import sys
def mysumm(a):
    summ = a[0]
    summ2 = a[0]

    for i in a[1:]:
        summ += i
        summ2 = max(summ2+i, summ2, i)

    return (summ, summ2)

def max_sum(n,a, summ):

    i = 0
    realSumm = 0
    for i in range(n):
        realSumm = max(a[i], realSumm + a[i])
        summ = max(summ, realSumm)

    return summ

    
with open('input.txt') as f:
    content = f.readlines()
    t = int(content[0].strip())
    
    i = 1
    for k in range(t):
        n = int(content[i].strip())
        i+=1
        a = [int(x) for x in content[i].strip().split()]
        i+=1
        
        summ, summ2 = mysumm(a)

        result = max_sum(n, a, summ)

        print(result, summ2)
        print()
