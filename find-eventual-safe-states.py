class Solution:
    def dfs(self, node, graph, visited, result):
        if node in visited:
            return visited[node]
        visited[node] = False
        
        safe = True
        for nextNode in graph[node]:
            safe = safe and self.dfs(nextNode, graph, visited, result)

        if safe:
            visited[node] = True
            result.append(node)
            
        return visited[node]

    def eventualSafeNodes(self, graph):
        visited = {}
        result = []
        for node in range(len(graph)):
            self.dfs(node, graph, visited, result)

        return sorted(result)

graph = [[1,2],[2,3],[5],[0],[5],[],[]]
# graph = [[],[0,2],[0],[2],[3],[]]
# graph = [[],[0],[0,3],[2],[3],[]]
print(Solution().eventualSafeNodes(graph))
        