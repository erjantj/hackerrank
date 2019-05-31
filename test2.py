def gardenNoAdj(n,paths):
    print(n, paths)

    neighbours = {}

    for i in range(n):
        neighbours[i+1] = []

    for g1,g2 in paths:
        neighbours[g1].append(g2)
        neighbours[g2].append(g1)

    result = [0 for i in range(n)]
    for i in range(n):
        g = i + 1
        color_set = set([1,2,3,4])
        g_neighbours = neighbours[g]

        for neighbour in g_neighbours:
            if result[neighbour-1] > 0 and result[neighbour-1] in color_set:
                color_set.remove(result[neighbour-1])

        for candidate in color_set:
            break

        result[i] = candidate

    return result

N = 6
paths = [
    [1,2],
    [2,3],
    [3,4],
    [4,5],
    [5,6],
    [1,6],
    [2,6],
]
print(gardenNoAdj(N, paths))