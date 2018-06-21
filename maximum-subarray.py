import sys
def mysumm(a):
    summ = a[0]
    summ2 = a[0]

    for i in a[1:]:
        summ += i
        summ2 = max(summ2+i, summ2, i)

    return (summ, summ2)

def max_sum(i,n,a,summ,memo):

    key = '%s-%s'%(i,n-1)
    if key in memo:
        return memo[key]

    key = '%s-%s'%(i+1,n)
    if key in memo:
        return memo[key]

    if n == 0:
        if a[i] > 0 :
            memo['summ2'] += a[i]
        return a[i]

    if i > n-1:
        if a[n-1] > 0 :
            memo['summ2'] += a[n-1]
        return a[n-1]

    print(a[i:n], '=',summ)
    memo[key] = max(
        summ, 
        max_sum(i+1, n, a, (summ-a[i]), memo),
        max_sum(i, n-1, a, (summ-a[n-1]), memo)
    )

    return memo[key]

    
with open('input.txt') as f:
    content = f.readlines()
    t = int(content[0].strip())
    
    i = 1
    for k in range(t):
        n = int(content[i].strip())
        i+=1
        a = [int(x) for x in content[i].strip().split()]
        i+=1
        
        memo = {'summ2': 0}
        summ, summ2 = mysumm(a)

        key = '%s-%s'%(0,n)
        memo[key] = summ

        result = max_sum(0, n, a, summ, memo)

        print(result, summ2)
        print()
