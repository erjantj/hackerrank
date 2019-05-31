def helper(s, i, memo):
    if i >= len(s):
        return 1
        
    if s[i] == '0':
        return 0

    key = s[i:]
    # if key in memo:
    #     return memo[key]

    val = 0
    count = 0

    for k in range(i, len(s)):
        print('work')
        val = val*10 + int(s[k])
        if val <= 26:
            count += helper(s, k+1, memo)
        else:
            break

    memo[key] = count
    return memo[key]

def numDecodings(s: str):
    if not s:
        return 0

    memo = {}
    return helper(s, 0, memo)

# s = '0'
s = "4757562545844617494555774581341211511296816786586787755257741178599337186486723247528324612117156948"
# s = "2222"
print(numDecodings(s))
