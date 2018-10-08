def lengthOfLongestSubstring(s):
    dp = [[1, [s[i]]] for i in range(len(s))]

    if not s:
        return 0
    if len(s)==1:
        return 1

    maxx = 0
    for i in range(1, len(s)):
        prevCount, prevSet = dp[i-1]
        tmpCount = prevCount+1
        tmpSet = prevSet

        if s[i] not in prevSet:
            tmpSet.append(s[i])
        else:
            tmpSet = []
            tmpCount = dp[i][0]
            duplicateFound = False
            for j in range(len(prevSet)):
                if prevSet[j] == s[i]:
                    duplicateFound = True
                    continue
                if duplicateFound:
                    tmpSet.append(prevSet[j])
                    tmpCount += 1
            tmpSet.append(s[i])

        if tmpCount > maxx:
            maxx = tmpCount
            
        dp[i][0] = tmpCount
        dp[i][1] = tmpSet

    return maxx

s = "abrcbklgabr"

print(lengthOfLongestSubstring(s))