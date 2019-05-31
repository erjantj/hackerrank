import sys 

def coinChange(coins, amount):
    if amount == 0:
        return 0

    if not coins and amount > 0:
        return -1

    dp = [sys.maxsize]*(amount+1)
    dp_used = [{} for x in range(amount+1)]
    dp[0] = 0

    for i in range(len(coins)):
        for j in range(coins[i],amount+1):
            next_val = 1+dp[j-coins[i]]
            next_used = dict(dp_used[j-coins[i]])
            prev_val = dp[j]

            if next_val < prev_val and (next_used.get(coins[i], 0) + 1) <= counts[i]:
                dp[j] = next_val
                dp_used[j] = next_used
                dp_used[j][coins[i]] = next_used.get(coins[i], 0) + 1

    if dp[amount] >= sys.maxsize:
        return -1

    print(dp_used)
    return dp[amount]

coins = [4,3, 1]
counts = [1,2, 2]
amount = 9

# coins = [294,128,316,466,108,463,321,490]
# amount = 7130

# coins = [112,149,215,496,482,436,144,397,500,189]
# amount = 8480

# coins = [7,2]
# amount = 9

# coins = [123,233,133,100,126]
# amount = 1034

print(coinChange(coins, amount))


# 8 2
# 6 2
# 4 2
# 2 2
# 0 2 1