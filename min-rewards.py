def minRewards(scores):
    if not scores:
        return 0

    rewards = [1 for _ in range(len(scores))]
    for i in range(1, len(scores)):
        if scores[i] > scores[i-1]:
            rewards[i] = rewards[i-1] + 1
    for i in range(len(scores)-2, -1, -1):
        if scores[i] > scores[i+1] and rewards[i+1]+1 > rewards[i]:
            rewards[i] = rewards[i+1]+1

    return sum(rewards)

# scores = [8,4,2,1,3,6,7,9,5]    
# scores = [8,4,2,1,3,2,7,9,5]    
# scores = [3,5,2,3,4,10,2,9,3]
# scores = [3,5,2,3,4,10,2,9,3,5]
# scores = [0,4,24,11,12,24]
# scores = [1,2,3,4]
# [1,2,2,1,2]
# scores = [2, 20, 13, 12, 11, 8, 4, 3, 1, 5, 6, 7, 9, 0]
print(minRewards(scores))

