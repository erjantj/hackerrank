from collections import deque

class Solution:
    def bfs(self, openSet, grid, n):
        level = -1
        shifts = [(0,1), (1,0), (0,-1), (-1,0)]
        visited = set()

        while openSet:
            size = len(openSet)
            for _ in range(size):
                point = openSet.popleft()

                for shift in shifts:
                    x = point[0] + shift[0]
                    y = point[1] + shift[1]

                    if x >= 0 and y >= 0 and x < n and y < n and grid[x][y] == 0 and (x,y) not in visited:
                        openSet.append((x,y))
                        visited.add((x,y))
            level += 1

        return level


    def maxDistance(self, grid):
        if not grid:
            return 0

        n = len(grid)
        openSet = deque([])

        for x in range(n):
            for y in range(n):
                if grid[x][y] == 1:
                    openSet.append((x,y))

        if not openSet or len(openSet) == n**2:
            return -1

        return self.bfs(openSet, grid, n)


grid = [[1,0,1],[0,0,0],[1,0,1]]
grid = [[1,0,0],[0,0,0],[0,0,0]]
grid = [[1,1,0,1,0,0],[1,1,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]]
grid = [[0,0,1,1,1],[0,1,1,0,0],[0,0,1,1,0],[1,0,0,0,0],[1,1,0,0,1]]
# grid = [[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]]
# grid = [[1,1,1,1,1,1],[1,1,1,1,1,1],[1,1,1,1,1,1],[1,1,1,1,1,1],[1,1,1,1,1,1],[1,1,1,1,1,1]]
print(Solution().maxDistance(grid))