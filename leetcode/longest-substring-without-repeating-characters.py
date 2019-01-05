def lengthOfLongestSubstring(s):
    if  not s:
        return 0
    
    maxx = 0
    tmp_max = 0
    start = 0
    letter_last_index = {}

    for i in range(len(s)):
        start = max(start, letter_last_index.get(s[i], 0))
        if s[start] == s[i] and i != start:
            start += 1

        tmp_max = i - start + 1

        if tmp_max > maxx:
            maxx = tmp_max

        letter_last_index[s[i]] = i
    return maxx

s = "aaba"
# s = "tmmzuxt"
# s = "wobgvwrovw"

print(lengthOfLongestSubstring(s))