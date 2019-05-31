def isMatch(s: str, p: str):
    dp = [[False for j in range(len(s)+1)] for i in range(len(p)+1)]

    s = "."+s
    p = "."+p

    for i in range(0, len(p)):
        for j in range(0, len(s)):
            if i == 0 and j == 0:
                dp[i][j] = True
            elif s[j] == p[i] or p[i] == '?':
                if i>0 and j>0:
                    dp[i][j] = dp[i-1][j-1]
            elif p[i] == '*':
                if i > 0:
                    dp[i][j] = dp[i][j] or dp[i-1][j]
                if j > 0:
                     dp[i][j] = dp[i][j] or dp[i][j-1]
            
    for row in dp:
        print(row)
    return dp[len(p)-1][len(s)-1]


s = "a"
p = "*a"

# s = "a"
# p = "*a"

print(isMatch(s, p))