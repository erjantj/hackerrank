def findParent(parent,v):
    if parent[v] != v:
        parent[v] = findParent(parent, parent[v])
    return parent[v]

def union(parent1, parent2, parent):

    parent[parent2] = parent1


def buildGraph(g_from, g_to, g_weight, n):
    graph = []
    nodes = []
    parent = {}

    for i in range(n):
        nodes.append(i+1)
        parent[i+1] = i+1

    for i in range(len(g_from)):
        graph.append((g_weight[i], g_from[i], g_to[i]))
        graph.append((g_weight[i], g_to[i], g_from[i]))

    return (graph, nodes, parent)


def findSpecialTreeSum(g_from, g_to, g_weight, n):
    graph, nodes, parent = buildGraph(g_from, g_to, g_weight, n)
    graph.sort()
    
    summ = 0
    for weight, v1, v2 in graph:
        parent1 = findParent(parent, v1)
        parent2 = findParent(parent, v2)
        if parent1 != parent2:
            union(parent1, parent2, parent)
            summ += weight

    return summ

n = 4
g_from = [1, 1, 4, 2, 3, 3] 
g_to = [2, 3, 1, 4, 2, 4] 
g_weight = [5, 3, 6, 7, 4, 5]

print(findSpecialTreeSum(g_from, g_to, g_weight, n))