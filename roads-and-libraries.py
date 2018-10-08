def bfs(graph, start, node_visited):
    openSet = [start]
    colsedSet = set()
    treeSize = 0

    while openSet:
        node = openSet.pop(0)

        if node not in colsedSet:

            colsedSet.add(node)
            node_visited[node] = True
            treeSize += 1

            for connected_node in graph.get(node, []):
                if connected_node in colsedSet:
                    continue

                if connected_node not in openSet:
                    openSet.append(connected_node)

    return treeSize

def buildGraph(cities):
    graph = {}

    for n_from,n_to in cities:
        graph[n_from] = graph.get(n_from, [])
        graph[n_to] = graph.get(n_to, [])
        graph[n_from].append(n_to)
        graph[n_to].append(n_from)

    return graph

def roadsAndLibraries(n, c_lib, c_road, cities):
    graph = buildGraph(cities)
    nodes = set()
    node_visited = {}

    for i in range(n):
        nodes.add(i+1)
        node_visited[i+1] = False

    minCost = 0
    for node in nodes:
        if not node_visited[node]:
            treeSize = bfs(graph, node, node_visited)

            tpmTreseSize = 0
            tmpCitiesLeft = treeSize
            tmpMinCost = treeSize*c_road+c_lib

            for i in range(1, treeSize+1):
                cost = tpmTreseSize*c_road + tmpCitiesLeft*c_lib
                if tpmTreseSize > 0:
                    cost += c_lib

                tmpMinCost = min(tmpMinCost, cost)

                tpmTreseSize = i
                tmpCitiesLeft = treeSize - (i+1)


            minCost += tmpMinCost

    return minCost

n = 5
c_lib = 6
c_road = 1
cities = [[1, 2], [1, 3], [1, 4]]

print(roadsAndLibraries(n, c_lib, c_road, cities))