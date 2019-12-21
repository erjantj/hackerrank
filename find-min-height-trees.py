class Solution:
    def exploreNodePaths(self, root, from_node, graph, visited, maxPath):
        if root in visited:
            return maxPath[root]

        print(root)
        visited.add(root)

        path = 0
        for node in graph[root]:
            if node == from_node:
                continue
            path = max(path, self.exploreNodePaths(node, root, graph, visited, maxPath))

        return path + 1


    def findMinHeightTrees(self, n, edges):
        # if n == 0:
        #     return []

        graph = {}
        maxPath = {}
        visited = set()

        for node in range(n):
            graph[node] = []
            maxPath[node] = 0

        for node1, node2 in edges:
            graph[node1].append(node2)
            graph[node2].append(node1)

        for node in range(n):
            self.exploreNodePaths(node, None, graph, visited, maxPath)
            print(node, maxPath)


n = 6
edges = [[0,3],[1,3],[2,3],[3,4],[4,5]]

# n=4
# edges = [[1, 0], [1, 2], [1, 3]]

print(Solution().findMinHeightTrees(n, edges))