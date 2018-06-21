import sys
def count_ops(N):
    c = N//5
    N %= 5
    c += N // 2
    N %= 2
    c += N
    return c

def makeSort(arr):
    return sorted(arr)

p = [1,2,5]

with open('input.txt') as f:
    content = f.readlines()
    t = int(content[0].strip())

    k = 1
    for i in range(t):
        n = int(content[k].strip())        
        k+=1

        arr = [int(x) for x in content[k].strip().split()]        
        k+=1

        arr = makeSort(arr)
        minn = arr[-2]+1
        maxx = arr[-1]+1

        memo = {}

        steps = 0
        for i in range(1, len(arr)):
            if arr[i]-arr[0] not in memo:
                memo[arr[i]-arr[0]] = 0
            memo[arr[i]-arr[0]] += count_ops(arr[i]-arr[0]);

        print(memo)
        print(steps)

