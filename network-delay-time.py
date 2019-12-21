import heapq

class Solution:
    def bfs(self, start, graph, costs, n):
        openSet = [(0, start)]
        visited = {}
        for node in range(1,n+1):
            visited[node]= float('inf')

        while openSet:
            cost, node = heapq.heappop(openSet)
            if cost >= visited[node]:
                continue
            visited[node] = cost

            for nextNode in graph[node]:
                heapq.heappush(openSet, (cost+costs[(node, nextNode)], nextNode))

        maxCost = max(visited.values())
        if len(visited) != n or maxCost == float('inf'):
            return -1

        return maxCost

    def constructGraph(self, times, n):
        graph = {}
        costs = {}

        for node in range(1, n+1):
            graph[node] = []

        for fromNode, toNode, weight in times:
            graph[fromNode].append(toNode)
            costs[(fromNode, toNode)] = weight

        return (graph, costs)

    def networkDelayTime(self, times,    n, k):
        if not times or not n:
            return -1

        graph, costs = self.constructGraph(times, n)
        return self.bfs(k, graph, costs, n)



times = [[2,1,1],[2,3,1],[3,4,1]]
n = 4
k = 2

# times = [[1,2,1],[2,3,2],[1,3,4]]
# n = 3
# k = 1

# times = [[1,2,1],[2,3,1],[1,3,3],[3,4,2], [4,1,1]]
# n = 4
# k = 1

# times = [[1,2,1]]
# n = 2
# k = 2
print(Solution().networkDelayTime(times, n, k))
        

    #     1
    #    /|
    #   2 |
    #  /  |
    # 3----
    # |
    # 4