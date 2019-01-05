def uniquePaths(m, n):
    if not m or not n:
        return 0
    if m == 1 or n == 1:
        return 1

    grid = [[0 for i in range(m)] for j in range(n)]

    grid[0][0] = 0
    grid[0][1] = 1
    grid[1][0] = 1
    open_set = [(0,1),(1,0)]

    while open_set:
        point = open_set.pop(0)
        if point[1]-1 >= 0:
            grid[point[0]][point[1]] += grid[point[0]][point[1]-1]
        if point[0]-1 >= 0:
            grid[point[0]][point[1]] += grid[point[0]-1][point[1]]

        if point[1]+1 < m and (point[0],point[1]+1) not in open_set:
            open_set.append((point[0],point[1]+1))
        
        if point[0]+1 < n and grid[point[0]+1][point[1]] not in open_set:
            open_set.append((point[0]+1,point[1]))

    cost = 0
    if m-2 >= 0:
        cost += grid[n-1][m-2]
    if n-2 >= 0:
        cost += grid[n-2][m-1]

    return cost

m=2
n=10
print(uniquePaths(m,n))