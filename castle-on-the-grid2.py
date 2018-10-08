import sys
from collections import deque

def minimumMoves(grid, startX, startY, goalX, goalY, n):
    dist = [n * [sys.maxsize] for _ in range(n)]
    dist[startX][startY], grid[goalX][goalY] = 0, '*'

    queue = deque([(startX, startY)])

    while queue:
        x0, y0 = queue.popleft()
        d = dist[x0][y0]
        print((x0, y0), d)

        if grid[x0][y0] == '*':
            break
        for nbr in [range(x0+1, n), range(x0-1, -1, -1)]:
            for x in nbr:
                if grid[x][y0] == 'X':
                    break
                if dist[x][y0] == sys.maxsize:
                    dist[x][y0] = d + 1
                    queue.append((x, y0))
        for nbr in [range(y0+1, n), range(y0-1, -1, -1)]:
            for y in nbr:
                if grid[x0][y] == 'X':
                    break
                if dist[x0][y] == sys.maxsize:
                    dist[x0][y] = d + 1
                    queue.append((x0, y))

        print()
        for row in dist:
            for point in row:
                if point == sys.maxsize:
                    print('.', ' ', end='')
                else:
                    print(point, ' ', end='')
            print()
    return d

with open('input.txt') as f:
    content = f.readlines()
    n = int(content[0].strip())
    grid = []

    for i in range(n): 
        line = content[i+1].strip()
        grid.append(list(line))

    startX, startY, goalX, goalY = [int(x) for x in content[n+1].strip().split()]
    print(startX, startY, goalX, goalY)
    print(minimumMoves(grid, startX, startY, goalX, goalY, n))