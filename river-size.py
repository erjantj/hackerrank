from collections import deque

def get_neighbours(matrix,point):
    shifts = [(1,0), (0,1), (-1,0), (0,-1)]
    neighbours = []
    for x,y in shifts:
        if point[0]+x >= 0 and point[0]+x < len(matrix) and \
           point[1]+y >= 0 and point[1]+y < len(matrix[0]) and \
           matrix[point[0]+x][point[1]+y] == 1:
            neighbours.append((point[0]+x, point[1]+y))
    return neighbours

def bfs(matrix, point, visited):
    size = 0
    open_set = deque([point])
    while open_set:
        p = open_set.popleft()
        
        if p in visited:
            continue
        size += 1
        visited.add(p)
        
        for neighbour in get_neighbours(matrix,p):
            open_set.append(neighbour)
            
    return size

def riverSizes(matrix):
    if not matrix:
        return []
    
    result = []
    visited = set()
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 1 and (i,j) not in visited:
                size = bfs(matrix, (i,j), visited)
                result.append(size)
                print((i,j), size)
    return result

matrix = [
    [1,0,0,1,0],
    [1,0,0,0,0],
    [0,0,1,0,0],
    [0,0,1,0,1],
    [1,0,1,0,1],
    [1,0,1,1,0],
]
print(riverSizes(matrix))