class Solution:
    def exploreMHT(self, parent, graph, result, n):
        if len(graph[parent]) == 0:
            return 0

        depth = n
        for node in graph[parent]:
            depth = min(depth, self.exploreMHT(node, graph, result, n))

        return depth+1
        
    def findMinHeightTrees(self, n, edges):
        graph = {}
        result = []

        for node in range(n):
            graph[node] = []

        for node, parent in edges:    
            graph[parent].append(node)

        for node in range(n):
            self.exploreMHT(node, graph, result, n)

        return result

n = 9
edges = [[1,0],[2,1],[3,1],[6,5],[6,4],[6,0],[7,6],[8,7],[9,2]]
print(Solution().findMinHeightTrees(n, edges))
        