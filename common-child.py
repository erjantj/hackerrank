def commonChild(s1, s2):
    s_len = len(s1)
    dp = [[0]*(s_len+1) for i in range(s_len+1)]

    for i in range(s_len+1):
        for j in range(s_len+1):
            if i == 0 or j == 0 :
                dp[i][j] = 0
            elif s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j],dp[i][j-1])

    return dp[s_len][s_len]

with open('input.txt') as f:
    content = f.readlines()
    s1 = content[0].strip()
    s2 = content[1].strip()
    print(commonChild(s1,s2))
