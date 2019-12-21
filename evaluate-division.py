class Solution:
    def dfs(self, node, end, from_node, graph, costs):
        if node not in graph or end not in graph:
            return False, -1.0
            
        value = 1.0 if from_node == None else costs[(from_node, node)]
        if node == end:
            return True, value

        found = False
        for nextNode in graph[node]:
            if nextNode == from_node:
                continue
            tmp_found, tmp_value = self.dfs(nextNode, end, node, graph, costs)
            found = found or tmp_found
            if found:
                return found, value*tmp_value

        return False, value


    def calcEquation(self, equations, values, queries):
        graph = {}
        costs= {}
        result = []

        for i in range(len(equations)):
            from_node, to_node = equations[i]
            if from_node not in graph:
                graph[from_node] = []
            if to_node not in graph:
                graph[to_node] = []
            graph[from_node].append(to_node)
            graph[to_node].append(from_node)

            costs[(from_node, to_node)] = values[i]
            costs[(to_node, from_node)] = 1/values[i]

        for start, end in queries:
            found, value = self.dfs(start, end, None, graph, costs)
            if found:
                result.append(value)
            else:
                result.append(-1.0)

        return result


# equations = [["a", "b"], ["b", "c"]]
# values = [2.0, 3.0]
# queries = [ ["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"], ["c","a"]]

equations = [["a", "b"], ["b", "c"],["a","d"]]
values = [2.0, 3.0, 3.0]
queries = [ 
    ["a", "a"],
    ["a", "b"], 
    ["a", "c"], 
    ["b", "a"], 
    ["a", "e"], 
    ["a", "a"], 
    ["x", "x"], 
    ["c","d"]
]

print(Solution().calcEquation(equations, values, queries))
        