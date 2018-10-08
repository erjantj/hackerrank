def helper(s, i, j, dp = {}):
    if i >= j:
        return (False, i, j)

    if dp.get((i,j), None):
        return dp[i][j]

    if not s:
        return ''

    if len(s) == 2:
        if passs[0]==s[1]:
            print(i, j)
            return (True, i, j)
        else:
            return (False, i, j)

    if len(s) == 3 :
        if s[0]==s[2]:
            print(i, j)
            return (True, i, j)
        else:
            return (False, i, j)

    if s[i] == s[j-1]:
        prev = helper(s, i+1, j-1, dp)
        print(s[i:j])
        if prev[0] == True:
            print(i, j)
            return (True, i, j)
    else:
        prevA = helper(s, i+1, j, dp)
        prevB = helper(s, i, j-1, dp)

        print(s[i:j])

        if prevA[2]-prevA[1] > prevB[2]-prevB[1]:
            return prevA
        else:
            return prevB

    return (False, i,j)

def longestPalindrome(s):
    print(helper(s, 0, len(s)))
    return ''

#    012345678
s = "aacdefcaa"
print(longestPalindrome(s))
