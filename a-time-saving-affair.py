import sys
from heapq import *

with open('input.txt') as f:
    content = f.readlines()

    def dijkstra(graph, connectedCount, start, end, k):
        minCost = sys.maxsize
        openSet = [(0,start,None)] # (cost, node, from_node)
        closedSet = set()
        mins = {start: 1}

        while openSet:
            (cost,node, from_node) = heappop(openSet)

            if node not in closedSet:
                if connectedCount[node] >  1:
                    connectedCount[node] -= 1
                else:
                    closedSet.add(node)

                for cost_to, connected_node in graph.get(node, ()):
                    if connected_node in closedSet: 
                        continue

                    prevCost = mins.get(connected_node, None)
                    nextCost = cost + cost_to

                    if connected_node != end and (nextCost//k)%2 == 1:
                        nextCost += k-nextCost%k

                    if prevCost is None or nextCost < prevCost:
                        mins[connected_node] = nextCost
                        heappush(openSet, (nextCost, connected_node, node))

                if node == end:
                    if cost < minCost:
                        minCost = cost
        
        return minCost


    def leastTimeToInterview(n, k, m):
        currColor = 0

        x = 3
        graph = {}
        edges = []
        connectedCount = {}

        for i in range(m):
            l,r,c = [int(u) for u in content[x].strip().split()]
            x += 1
            
            edges.append((l,r,c))
            graph[l] = []
            graph[r] = []
            connectedCount[l] = 0
            connectedCount[r] = 0

        for l,r,c in edges:
            graph[l].append((c,r))
            graph[r].append((c,l))
            connectedCount[l] += 1
            connectedCount[r] += 1

        return dijkstra(graph, connectedCount, 1, n, k)


    n = int(content[0].strip())
    k = int(content[1].strip())
    m = int(content[2].strip())

    print(leastTimeToInterview(n, k, m))
    