from heapq import heappush,heappop

def mergeStones(stones,K):
    prefix_sums = [0, stones[0]]
    for i in range(1,len(stones)):
        prefix_sums.append(prefix_sums[i] + stones[i])

    heap = []
    for i in range(0,len(stones)-K+1):
        heappush(heap, (prefix_sums[i+K]-prefix_sums[i], (i+k-1, i)))

    print(heappop(heap))
    print(heappop(heap))
    print(heappop(heap))

stones = [3,2,4,1]
k = 2

print(mergeStones(stones, k))