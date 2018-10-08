def getMinimumCost(k, arr):
    arr = sorted(arr, reverse=True)
    arr_len = len(arr)
    purchase = 1
    summ = 0

    for i in range(arr_len):
        summ += purchase*arr[i]
        if (i%k)+1 == k:
            purchase += 1

    return summ

with open('input.txt') as f:
    content = f.readlines()
    n,k = [int(x) for x in content[0].strip().split()]
    arr = [int(x) for x in content[1].strip().split()]

    print(getMinimumCost(k, arr))