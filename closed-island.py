class Solution:
    def isBorderPoint(self, rows, columns, point):
        if point[0] > 0 and point[1] > 0 and point[0] < rows-1 and point[1] < columns-1:
            return False
        return True

    def getPointNeighbours(self, grid, rows, columns, point):
        neighbours = []
        shifts = [(0,1), (1,0), (0,-1), (-1,0)]
        for shift in shifts:
            rowShift = point[0] + shift[0]
            colShift = point[1] + shift[1]

            if rowShift >= 0 and rowShift < rows and colShift >= 0 and colShift < columns and grid[rowShift][colShift] == 0:
                neighbours.append((rowShift, colShift))

        return neighbours

    def isClosedIsland(self, grid, rows, columns, visited, startPoint):
        open_set = [startPoint]
        isTouchesBorder = False

        while open_set:
            point = open_set.pop()

            if point in visited:
                continue
            visited.add(point)

            if self.isBorderPoint(rows, columns, point):
                isTouchesBorder = True

            neighbours = self.getPointNeighbours(grid, rows, columns, point)
            for neighbour in neighbours:
                open_set.append(neighbour)

        return not isTouchesBorder

    def closedIsland(self, grid):
        if not grid:
            return 0

        rows = len(grid)
        columns = len(grid[0])
        islands_count = 0
        visited = set()

        for row in range(rows):
            for col in range(columns):
                if grid[row][col] == 0 and (row, col) not in visited:
                    if self.isClosedIsland(grid, rows, columns, visited, (row, col)):
                        islands_count += 1

        return islands_count

grid = [[1,1,1,1,1,1,1,0],[1,0,0,0,0,1,1,0],[1,0,1,0,1,1,1,0],[1,0,0,0,0,1,0,1],[1,1,1,1,1,1,1,0]]
# grid = [
#     [0,0,1,0,0],
#     [0,1,0,1,0],
#     [0,1,1,1,0]
# ]
# grid = []
# grid = [
# [1,1,1,1,1,1,1,1,1,1],
# [1,1,0,0,1,1,1,1,1,1],
# [1,1,0,1,0,1,1,1,1,1],
# [1,1,0,1,1,1,1,1,1,1],
# [0,0,0,1,1,1,1,1,1,1],
# [1,1,1,1,1,1,1,1,1,1],
# [1,1,1,1,1,1,1,1,1,1],
# [1,1,1,1,1,1,1,1,1,1]

# ]
print(Solution().closedIsland(grid))
        