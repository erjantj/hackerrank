def getFarest(graph, n, x):
    s = [(0,x)]
    closedSet = [False]*(n+1)

    dist = 0
    farest = 0
    parent = 0

    while s:
        (cost,node) = s.pop()
        k = 0
        if k < n and not closedSet[node]:
            closedSet[node] = True
            k += 1

            for cost_to, connected_node  in graph.get(node, ()):
                nextCost = cost + cost_to

                if dist < nextCost and connected_node != x:
                    dist = nextCost
                    farest = connected_node
                    parent = node
                s.append((nextCost, connected_node))

    return (dist, farest, parent)

def addNode(graph, n, farest, weight):
    n += 1
    graph[farest].append((weight, n))
    return n

def deleteNode(graph, n, farest, parent):
    for i in range(len(graph[parent])):
        cost, node = graph[parent][i]
        if node == farest:
            n -= 1
            del graph[parent][i]
    return n

def doOne(graph, n, x, weight):
    dist, farest, parent = getFarest(graph, n, x)
    return addNode(graph, n, farest, weight)

def doTwo(graph, n, x, weight):
    return addNode(graph, n, x, weight)

def doThree(graph, n, x):
    dist, farest, parent = getFarest(graph, n, x)
    return deleteNode(graph, n, farest, parent)

def doFour(graph, n, x):
    dist, farest, parent = getFarest(graph, n, x)
    return dist

def cyclicalQueries(w, m, n):
    result = []
    graph = {}

    for i in range(1,n+1):
        graph[i] = []

    for i in range(1,n):
        graph[i].append((w[i-1], i+1))

    graph[n].append((w[m], 1))

    k = 3
    for i in range(m):
        query=x=weight = None
        line = [int(x) for x in content[k].strip().split()]
        
        if len(line) == 3:
            query,x,weight = line
        else:
            query,x = line
        k+=1

        if query == 1:
            n = doOne(graph, n, x, weight)
        if query == 2:
            n = doTwo(graph, n, x, weight)
        if query == 3:
            n = doThree(graph, n, x)
        if query == 4:
            result.append(doFour(graph, n, x))

        print(graph)
    return result

with open('input.txt') as f:
    content = f.readlines()
    n = int(content[0].strip())

    w = [int(x) for x in content[1].strip().split()]

    m = int(content[2].strip())

    print(cyclicalQueries(w, m, n))