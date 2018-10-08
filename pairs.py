from collections import defaultdict
def pairs(k, arr):
    vals = defaultdict(int)
    arr_len = len(arr)
    arr = sorted(arr)

    for i in arr:
        vals[k+i] += True
    pairsCount = 0

    for i in range(arr_len):
        if vals[arr[i]]:
            pairsCount += vals[arr[i]]

    return pairsCount

print(pairs(2, [1,3,5,8,6,4,2]))

