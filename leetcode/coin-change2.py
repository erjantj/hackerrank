import sys

def change(coins, amount, i, memo):
    if i >= len(coins):
        return sys.maxsize

    if amount < 0:
        return sys.maxsize

    if amount in memo:
        return memo[amount]

    ways = change(coins, amount - coins[i], i, memo) + 1
    print(amount, ways)
    memo[amount] = ways

    return ways

def coinChange(coins, amount):
    if amount == 0:
        return 0

    if not coins and amount > 0:
        return -1

    memo = {}
    memo[0] = 0

    change(coins, amount, 0, memo)
    print(memo)
    # dp = {}
    # dp[0] = 0

    # for i in range(len(coins)):
    #     for j in range(coins[i],amount+1):
    #         tmp_coins = 1+dp.get(j-coins[i], sys.maxsize)
    #         if dp.get(j,None):
    #             tmp_coins = min(dp[j], tmp_coins)

    #         if tmp_coins < sys.maxsize:
    #             dp[j] = tmp_coins

    # if not dp.get(amount, None):
    #     return -1

    # if dp[amount] >= sys.maxsize:
    #     return -1

    # return dp[amount]


# coins = [294,128,316,466,108,463,321,490]
# amount = 7130

# coins = [112,149,215,496,482,436,144,397,500,189]
# amount = 8480

coins = [2,7]
amount = 9


print(coinChange(coins, amount))


# 8 2
# 6 2
# 4 2
# 2 2
# 0 2 1