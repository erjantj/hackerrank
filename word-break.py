def helper(s, words, start, memo):

    if start == len(s):
        return True
    
    matches = False        
    for end in range(len(s), start, -1):
        if end in memo:
            matches = memo[end]
        elif s[start:end] in words:
            print(s[start:end], (start, end))
            # print(memo)
            matches = matches or helper(s, words, end, memo)
            memo[end] = matches

        if matches:
            break

    return matches

def wordBreak(s, wordDict):
    if not s:
        return True

    if not wordDict:
        return False

    words = set(wordDict)
    memo = {}

    return helper(s, words, 0, memo)



s = "applepenapple"
wordDict = ["apple", "pen"]

# s = "catsandog"
# wordDict = ["cats", "dog", "sand", "and", "cat"]

# s = "aaaaa"
# wordDict = ["a","aa","aaa"]

s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab"
wordDict = ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]

print(wordBreak(s, wordDict))