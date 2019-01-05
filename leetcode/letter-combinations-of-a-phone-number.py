def letterCombinations(digits):
    if not digits:
        return []

    pad = {
        2: ['a','b','c'],
        3: ['d','e','f'],
        4: ['g','h','i'],
        5: ['j','k','l'],
        6: ['m','n','o'],
        7: ['p','q','r','s'],
        8: ['t','u','v'],
        9: ['w','x','y','z']
    }
    
    dp = [pad[int(digits[0])]]
    for i in range(1, len(digits)):
        tmp = []
        d = int(digits[i])
        for j in range(len(pad[d])):
            for k in dp[i-1]:
                tmp.append(k+pad[d][j])
        dp.append(tmp)

    return dp[-1]

digits = ''
print(letterCombinations(digits))

