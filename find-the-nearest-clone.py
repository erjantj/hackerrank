import sys
from heapq import *

def dijkstra(graph, start, val, colors):
    openSet = [(0, start,None)] # (cost, node, from_node)
    closedSet = set()
    mins = {start: 1}

    while openSet:
        cost, node, from_node = heappop(openSet)

        if node not in closedSet:
            closedSet.add(node)
            if node != start and colors[node-1] == val: 
                return cost

            for connected_node in graph.get(node, ()):
                if connected_node in closedSet: 
                    continue

                prevCost = mins.get(connected_node, None)
                nextCost = cost + 1
                
                if prevCost is None or nextCost < prevCost:
                    mins[connected_node] = nextCost
                    heappush(openSet, (nextCost, connected_node, node))

    return sys.maxsize

def buildGraph(graph_from, graph_to):
    graph = {}

    for i in range(len(graph_from)):
        graph[graph_from[i]] = graph.get(graph_from[i], [])
        graph[graph_from[i]].append(graph_to[i])

    for i in range(len(graph_to)):
        graph[graph_to[i]] = graph.get(graph_to[i], [])
        graph[graph_to[i]].append(graph_from[i])

    return graph

def countColors(colors, val):
    count = 0
    nodesToVisit = []
    for i in range(len(colors)):
        if colors[i] == val:
            count += 1
            nodesToVisit.append(i+1)

    return count, nodesToVisit

def findShortest(graph_nodes, graph_from, graph_to, colors, val):
    graph = buildGraph(graph_from, graph_to)
    colorsToVisitCount, nodesToVisit = countColors(colors, val)
    
    if colorsToVisitCount == 1:
        return -1

    minCost = sys.maxsize
    for node in nodesToVisit:
        tmpMin = dijkstra(graph, node, val, colors)
        if tmpMin < minCost:
            minCost = tmpMin
    
    if minCost == sys.maxsize:
        return -1

    return minCost


graph_nodes = 5
graph_from = [1, 1, 4, 4]
graph_to = [2, 3, 2, 5] 
colors = [1, 2, 2, 1, 2] 
val = 2

print(findShortest(graph_nodes, graph_from, graph_to, colors, val))

# 1/1---2/2---4/2---5/1
#   \--3/2

