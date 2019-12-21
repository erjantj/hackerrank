def maxProfitWithKTransactions(prices, k):
    if not prices or k <= 0:
        return 0

    dp = [[0 for d in range(len(prices))] for t in range(k+1)]
    for t in range(1, k+1):
        max_profit = -prices[0]
        for d in range(1, len(prices)):
            dp[t][d] = max(dp[t][d-1], prices[d]+max_profit)
            max_profit = max(max_profit, -prices[d]+dp[t-1][d])

    return dp[k][len(prices)-1]

prices = [5,11,3,50,60,90]
k = 2

print(maxProfitWithKTransactions(prices, k))