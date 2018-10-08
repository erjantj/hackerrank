import sys

def minimumMoves(grid, startX, startY, goalX, goalY):
    dot = '.'
    cross = 'X'

    scores = [[sys.maxsize for j in range(len(grid[i]))] for i in range(len(grid))]
    queue = [(startX, startY)]
    cost = 0
    scores[startX][startY] = cost

    while queue:
        point = queue.pop(0)
        cost = scores[point[0]][point[1]]
        if point == (goalX, goalY):
            break
            
        for direction in [range(point[1]+1, len(grid[0])), range(point[1]-1, -1, -1)]:
            for j in direction:
                if grid[point[0]][j] == 'X':
                    break
                if scores[point[0]][j] == sys.maxsize:
                    scores[point[0]][j] = cost + 1
                    queue.append((point[0],j))

        for direction in [range(point[0]+1, len(grid)), range(point[0]-1, -1, -1)]:
            for i in direction:
                if grid[i][point[1]] == 'X':
                    break
                if scores[i][point[1]] == sys.maxsize:
                    scores[i][point[1]] = cost + 1
                    queue.append((i,point[1]))

    for row in scores:
        print(row)
    return cost

with open('input.txt') as f:
    content = f.readlines()
    n = int(content[0].strip())
    grid = []

    for i in range(n): 
        line = content[i+1].strip()
        grid.append(list(line))

    startX, startY, goalX, goalY = [int(x) for x in content[n+1].strip().split()]
    print(minimumMoves(grid, startX, startY, goalX, goalY))