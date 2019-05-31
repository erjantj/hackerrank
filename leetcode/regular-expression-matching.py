def helper(s, p, dp, i, j):
    if i < -1 or j < -1:
        return False

    key = ('%d:%d')%(i,j)
    if key in dp:
        return dp[key]

    result = False
    if j-1>=0 and p[j] == '*':
        result = helper(s,p,dp,i,j-2) or helper(s,p,dp,i,j-1)
        if p[j-1] == '.':
            result = result or helper(s,p,dp,i-1,j)
        elif i >=0:
            result = result or (helper(s,p,dp,i-1,j) and p[j-1] == s[i])
    elif j>=0 and i >=0 and (p[j] == '.' or s[i] == p[j]):
        result = helper(s,p,dp,i-1,j-1)

    dp[key] = result
    return result

    
def isMatch(s, p):
    dp = {}
    dp['-1:-1'] = True

    result = helper(s,p,dp,len(s)-1,len(p)-1)
    return result


# s = "aa"
# p = "a"

# s = "aa"
# p = "a*"

# s = "aab"
# p = "c*a*b"

# s = "a"
# p = "c*a*"

# s = "mississippi"
# p = "mis*is*p*."

# s = "c"
# p = "c*a*"


print(isMatch(s,p))
