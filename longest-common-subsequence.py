def backtrack(dp, s1, s2):
    result = []
    i = len(s1)
    j = len(s2)
    while i > 0 and j > 0:
        if dp[i-1][j] == dp[i][j]:
            i -= 1
        elif dp[i][j-1] == dp[i][j]:
            j -= 1
        else:
            result.append(s1[i-1])
            i -= 1
            j -= 1
    return list(reversed(result))

def longestCommonSubsequence(s1, s2):
    if s1 == s2:
        return list(s1)
    dp = [[0 for _ in range(len(s2)+1)] for _ in range(len(s1)+1)]
    for i in range(1, len(s1)+1):
        for j in range(1, len(s2)+1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1]+1
            else:
                dp[i][j] = max(dp[i][j-1], dp[i-1][j])
    return backtrack(dp, s1, s2)


s1 = 'XWZ'
s2 = 'DWDZS'
print(longestCommonSubsequence(s1,s2))