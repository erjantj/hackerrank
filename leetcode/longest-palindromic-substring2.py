def helper(l, r, s):
    if s[l] == s[r]:
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return (l,r)
    return (0,0)
    
def longestPalindrome(s):
    if not s:
        return ""

    tmp = 0
    start = 0
    end = 0

    # len 2
    for i in range(len(s)-1):
        l,r = helper(i,i+1,s)
        if r-l > tmp:
            start = l
            end = r
            tmp = r-l

    # len > 3
    for i in range(len(s)):
        l,r = helper(i,i,s)
        if r-l > tmp:
            start = l
            end = r
            tmp = r-l

    return s[start+1: end]

#    012345678
s = "afasd"
print(longestPalindrome(s))
