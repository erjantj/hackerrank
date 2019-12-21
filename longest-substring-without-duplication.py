def longestSubstringWithoutDuplication(string):
    if not string:
        return ''
    indexes = {}
    max_range = (0,0)
    i = 0
    for j in range(len(string)):
        if string[j] in indexes:
            i = max(indexes[string[j]] + 1, i)
        indexes[string[j]] = j
        if j - i > max_range[1]-max_range[0]:
            max_range = (i,j)
    return string[max_range[0]:max_range[1]+1]

string = 'abba'

print(longestSubstringWithoutDuplication(string))