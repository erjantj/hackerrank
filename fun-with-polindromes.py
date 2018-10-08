def getScore(s):
    s_len = len(s)
    l = [[1 for x in range(s_len+1)] for _ in range(s_len+1)]
    maxx = 1
    maxx2 = 0
    maxxRanges = []

    for threshold in range(2, s_len+1):
        for i in range(s_len-threshold+1):
            j = i+threshold-1
            if s[i] == s[j] and threshold == 2:
                l[i][j] = 2
            elif s[i] == s[j]:
                l[i][j] = l[i+1][j-1] + 2
            else:
                l[i][j] = max(l[i][j-1], l[i+1][j]);

            if l[i][j] > maxx:
                maxx = l[i][j]
                maxxRanges.append((i,j))

    
    maxProduct = 0
    for i in range(len(maxxRanges)-1, -1, -1):
        maxxRange = maxxRanges[i]
        maxx = l[maxxRange[0]][maxxRange[1]]

        if s[0:maxxRange[0]] and s[maxxRange[1]+1:s_len]:
            maxx2 = max(l[0][maxxRange[0]-1], l[maxxRange[1]+1][s_len])
        elif s[0:maxxRange[0]]:
            maxx2 = l[0][maxxRange[0]-1]
        elif s[maxxRange[1]+1:s_len]:
            maxx2 = l[maxxRange[1]+1][s_len-1]
        tmpProduct = 1
        if maxx*maxx2:
            tmpProduct = maxx*maxx2

        if tmpProduct > maxProduct:
            maxProduct = tmpProduct

    for row in l:
        print(row)
    return maxProduct

s = 'abbbdbbad'
print(getScore(s))