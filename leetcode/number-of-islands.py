def explore(grid, start, visited):
    openSet = [start]
    while openSet:
        node = openSet.pop(0)
        if visited.get(node):
            continue

        visited[node] = True

        if node[0] + 1 < len(grid) and grid[node[0]+1][node[1]] == '1' and (not visited.get((node[0]+1, node[1]))):
            openSet.append((node[0]+1, node[1]))

        if node[0] - 1 >= 0 and grid[node[0]-1][node[1]] == '1' and (not visited.get((node[0]-1, node[1]))):
            openSet.append((node[0]-1, node[1]))

        if node[1] + 1 < len(grid[0]) and grid[node[0]][node[1]+1] == '1' and (not visited.get((node[0], node[1]+1))):
            openSet.append((node[0], node[1]+1))

        if node[1] - 1 >= 0 and grid[node[0]][node[1]-1] == '1' and (not visited.get((node[0], node[1]-1))):
            openSet.append((node[0], node[1]-1))

def numIslands(grid):
    if not grid:
        return 0

    visited = {}
    islands = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if (not visited.get((i,j))) and grid[i][j] == '1':
                islands += 1
                explore(grid, (i,j), visited)

    return islands

grid = [
['1','1','0','0','0'],
['1','1','0','0','0'],
['0','0','1','0','0'],
['0','0','0','1','1'],
]

grid = [
['1','1','1','1','0'],
['1','1','0','1','0'],
['1','1','0','0','0'],
['0','0','0','0','0'],
]

grid = [
['0','0','1','1','0'],
['1','0','1','0','0'],
['1','0','1','0','0'],
['1','1','1','1','0'],
]

print(numIslands(grid))