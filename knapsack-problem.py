def knapsackProblem(items, capacity):
    if not capacity or not items:
        return [0,[]]

    dp = [[0 for _ in range(len(items)+1)] for _ in range(capacity+1)]
    indexes = []
    sums = {}
    for i in range(1,capacity+1):
        for j in range(1, len(items)+1):
            dp[i][j] = dp[i][j-1]
            w = items[j-1][1]
            v = items[j-1][0]

            if items[j-1][1] <= i:
                summ = dp[i-w][j-1]+v
                if summ > dp[i][j]:     
                    dp[i][j] = summ

    for row in dp:
        print(row)

    i = capacity
    j = len(items)
    while i>=0 and j>=0:
        if dp[i-1][j] == dp[i][j]:
            i-=1
        elif dp[i][j-1] == dp[i][j]:
            j-=1
        else:
            indexes.append(j-1)
            i -= items[j-1][1]
            j-=1

    return [dp[capacity][len(items)], list(reversed(indexes))]

# items =  [[10,10],[2,2],[4,3],[5,6],[6,7]]
# items =  [[3,4],[4,4],[-1,1]]
items = [[1,2],[4,3],[5,6],[6,7]]
capacity = 5
print(knapsackProblem(items, capacity))