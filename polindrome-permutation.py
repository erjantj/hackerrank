def isPolindromePermutation(s):
    if not s:
        return True

    s = s.lower()
    index = {}
    s_len = 0
    for c in s:
        if c != ' ':
            if not c in index:
                index[c] = 0

            index[c] += 1
            s_len += 1

    lonely = 0
    for c,count in index.items():
        if count%2 >= 1:
            lonely += 1

    if s_len%2==1 and lonely == 1:
        return True
    if s_len%2==0 and lonely == 0:
        return True

    return False
s = 'azAZ'
print(isPolindromePermutation(s))


# ('azAZ', True)]
