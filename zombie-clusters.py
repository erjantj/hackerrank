def bfs(graph, start, nodeVisited):
    openSet = [start]
    colsedSet = set()

    while openSet:
        node = openSet.pop(0)

        if node not in colsedSet:

            colsedSet.add(node)
            nodeVisited[node] = True

            for connectedNode in graph.get(node, []):
                if connectedNode in colsedSet:
                    continue

                if connectedNode not in openSet:
                    openSet.append(connectedNode)

def buildGraph(zombies):
    graph = {}
    for i in range(len(zombies)):
        graph[i] = graph.get(i, [])
        for j in range(len(zombies[i])):
            if zombies[i][j] == '1':
                graph[i].append(j)

    return graph

def zombieCluster(zombies):
    graph = buildGraph(zombies)
    n = len(zombies)
    nodesToVisit = set()
    nodeVisited = {}
    clusters = 0

    for i in range(n):
        nodesToVisit.add(i)
        nodeVisited[i] = False
    
    for node in nodesToVisit:
        if not nodeVisited[node]:
            bfs(graph, node, nodeVisited)
            clusters += 1

    return clusters

zombies = ['1100', '1110', '0110', '0001']

print(zombieCluster(zombies))