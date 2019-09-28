def helper(string, l, r):
    while l >= 0 and r < len(string) and string[l] == string[r]:
        l -= 1
        r += 1
    l += 1
    r -= 1
    return (l,r,r-l+1)

def longestPalindromicSubstring(string):
    if not string or len(string) == 1:
        return string

    s = '_%s_'%(string)
    tmp_p = (0,0,1)
    max_p = (0,0,1)

    for i in range(1, len(string)-1):
        p1 = helper(string, i, i)
        p2 = helper(string, i, i+1)

        tmp_p = p1 if p1[2] > p2[2] else p2
        if tmp_p[2]>max_p[2]:
            max_p = tmp_p
    return string[max_p[0]:max_p[1]+1]


# string = 'abaxyzzyxf'
string = 'aaacabaca'
print(longestPalindromicSubstring(string))