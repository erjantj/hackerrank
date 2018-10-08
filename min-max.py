def maxMin(k, arr):
    arr = sorted(arr)
    arr_len = len(arr)
    minn = 10**9+7

    for i in range(k-1, arr_len):
        if arr[i]-arr[i-k+1] < minn:
            minn = arr[i]-arr[i-k+1]

    return minn

with open('input.txt') as f:
    content = f.readlines()
    n = int(content[0])
    k = int(content[1])
    arr = []
    for i in range(2, n+2):
        arr.append(int(content[i]))


    print(maxMin(k, arr))