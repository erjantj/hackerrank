import sys
from heapq import *

def dijkstra(edges, start, end):
    g = {}
    
    for l,r,c in edges:
        g[l] = []

    for l,r,c in edges:
        g[l].append((c,r))


    openSet = [(0,start,None)] # (cost, node, from_node)
    closedSet = set()
    mins = {start: 1}

    while openSet:
        (cost,node, from_node) = heappop(openSet)

        if node not in closedSet:
            closedSet.add(node)
            if node == end: 
                return cost

            for cost_to, connected_node in g.get(node, ()):
                if connected_node in closedSet: 
                    continue

                prevCost = mins.get(connected_node, None)
                nextCost = cost + cost_to
                
                if prevCost is None or nextCost < prevCost:
                    mins[connected_node] = nextCost
                    heappush(openSet, (nextCost, connected_node, node))

    return sys.maxsize


edges = [
    ("A", "B", 7),
    ("A", "D", 5),
    ("B", "C", 8),
    ("B", "D", 9),
    ("B", "E", 7),
    ("C", "E", 5),
    ("D", "E", 15),
    ("D", "F", 6),
    ("E", "F", 8),
    ("E", "G", 9),
    ("F", "G", 11)
]


print edges
print "A -> E:"
print dijkstra(edges, "A", "E")