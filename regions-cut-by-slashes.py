class Solution:
    def dfs(self, node, graph, visited, n, result, fromNode = None):
        if node in visited and visited[node] == 2:
            return

        if node in visited and visited[node] == 1:
            result[0] += 1
            return
        visited[node] = 1

        for nextNode in graph[node]:
            if nextNode != fromNode:
                self.dfs(nextNode, graph, visited, n, result, node)
        visited[node] = 2

    def constructGraph(self, grid, n):
        graph = {}
        for i in range(n):
            for j in range(n):
                graph[(i,j)] = []

        for i in range(n-1):
            for j in range(n-1):
                coor1 = None
                coor2 = None
                if grid[i][j] == '/':
                    coor1 = (i,j+1)
                    coor2 = (i+1,j)
                elif grid[i][j] == '\\':
                    coor1 = (i,j)
                    coor2 = (i+1,j+1)

                if coor1 and coor2:
                    graph[coor1].append(coor2)
                    graph[coor2].append(coor1)

            graph[(0,i)].append((0,i+1))
            graph[(0,i+1)].append((0,i))
            graph[(n-1,i)].append((n-1,i+1))
            graph[(n-1,i+1)].append((n-1,i))
            graph[(i, 0)].append((i+1, 0))
            graph[(i+1, 0)].append((i, 0))
            graph[(i, n-1)].append((i+1, n-1))
            graph[(i+1, n-1)].append((i, n-1))

        return graph

    def regionsBySlashes(self, grid):
        n = len(grid) + 1
        graph = self.constructGraph(grid, n)
        result = [0]
        visited = {}
        for i in range(n):
            for j in range(n):
                if not (i,j) in visited:
                    self.dfs((i,j), graph, visited, n, result)
        return result[0]


# grid = [
#   " /",
#   "/ "
# ]

# grid = [
#   "\\ ",
#   "/ "
# ]

# grid = [
#   " /",
#   "  "
# ]

# grid = [
#   "\\/",
#   "/\\"
# ]

# grid = [
#   "//",
#   "/ "
# ]


# grid = [
#     "/ /",
#     "\\/\\",
#     "/\\ "
# ] # 6

# grid = [
#     "/\\ ",
#     "\\/\\",
#     " \\/ "
# ] # 2

grid = [
    "\\/\\ ",
    " /\\/",
    " \\/ ",
    "/ / "
]

# grid = [
#     "\\/\\ ",
#     "    ",
#     "    ",
#     "    "
# ]

# grid = [
#     "/\\ ",
#     "\\/ ",
#     " \\ "
# ] # 2

print(Solution().regionsBySlashes(grid))


