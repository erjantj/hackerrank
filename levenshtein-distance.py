def levenshteinDistance(str1, str2):
    if not str1:
        return len(str2)
    if not str2:
        return len(str1)
    
    if len(str2) < len(str1):
        str1, str2 = str2, str1

    dp = [0 for i in range(len(str1)+1)]
    
    for i in range(len(str1)):
        dp[i+1] = dp[i] + 1
    
    prev_row = dp[:]
    for i in range(1, len(str2)+1):
        dp[0] += 1
        for j in range(1, len(str1)+1):
            if str2[i-1] == str1[j-1]:
                dp[j] = prev_row[j-1]
            else:
                dp[j] = min(dp[j], dp[j-1], prev_row[j-1])+1
        prev_row = dp[:]
            
    return dp[len(str1)]
    

# str1 = 'abc'
# str2 = 'yabd'


str1 = 'abc'
str2 = 'bcaa'


print(levenshteinDistance(str1, str2))