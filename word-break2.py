def helper(s, words, start, memo):
    if start in memo:
        print(start)
        return memo[start]
    arr = []
    for word in words:
        if s[start:].startswith(word):
            if start+len(word) >= len(s):
                arr.append(word)
            else:
                wordsBefore = helper(s, words, start+len(word), memo)
                for wordBefore in wordsBefore:
                    arr.append(' '.join([word,wordBefore]))
    memo[start] = arr

    return arr

def wordBreak(s, wordDict):
    if not s:
        return []

    if not wordDict:
        return []

    words = set(wordDict)
    memo = {}
    print(helper(s, words, 0, memo))


# s = "applepenapple"
# wordDict = ["apple", "pen"]

# s = "catsanddog"
# wordDict = ["cats", "dog", "sand", "and", "cat"]

# s = "aaaaa"
# wordDict = ["a","aa","aaa", "aaaa", "aaaaa"]

# s = "catsanddog"
# wordDict = ["cat", "cats", "and", "sand", "dog"]

# s = "donpineapplepen"
# wordDict = ["apple","don","applepen","pine","pineapple","donpine", "pen"]

# s = "a"
# wordDict = []

s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
wordDict = ["a","aa","aaa"]

print(wordBreak(s, wordDict))

