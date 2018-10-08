
def maxSubsetSum(arr):
    arr_len = len(arr)

    if arr_len == 1:
        return arr[0]

    if arr_len == 2:
        return max(arr[0], arr[1])
    
    dp = [0]*arr_len
    dp[0] = arr[0]
    dp[1] = max(arr[0], arr[1])
    maxx = max(arr[0], arr[1])
    
    for i in range(2, arr_len):
        maxx = max(maxx, (dp[i-2]+arr[i]), arr[i])
        dp[i] = maxx
    return dp[arr_len-1]

with open('input.txt') as f:
    content = f.readlines()
    n = int(content[0].strip())
    arr = [int(x) for x in content[1].strip().split()]

    print(maxSubsetSum(arr))
