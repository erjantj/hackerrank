import itertools
import collections

class Solution:
    def dfs(self, node, graph, result):
        if node not in graph:
            return
        while graph[node]:
            nextNode = graph[node].pop()
            self.dfs(nextNode, graph, result)

        result.append(node)

    def contructGraph(self, tickets):
        graph = {}
        for from_airport, to_airport in tickets:
            if from_airport not in graph:
                graph[from_airport] = []
            if to_airport not in graph:
                graph[to_airport] = []
            graph[from_airport].append(to_airport)

        for from_airport, to_airport in tickets:
            graph[from_airport] = list(reversed(sorted(graph[from_airport])))

        return graph
        
    def findItinerary(self, tickets):
        result = []
        graph = self.contructGraph(tickets)

        self.dfs('JFK', graph, result)
        return list(reversed(result))

# tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
# tickets = [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
# tickets = []
# tickets = [["MUC", "LHR"]]
# tickets = [["JFK", "LHR"]]
# tickets = [["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]]

# tickets = [["JFK","ATL"],["ATL","JFK"]]

# tickets = [["JFK","AAA"],["AAA","JFK"],["JFK","BBB"],["JFK","CCC"],["CCC","JFK"]]

# tickets =  [["JFK","ATL"],["ORD","PHL"],["JFK","ORD"],["PHX","LAX"],["LAX","JFK"],["PHL","ATL"],["ATL","PHX"]]

tickets = [["JFK","AAA"],["AAA","JFK"],["JFK","BBB"],["JFK","CCC"],["CCC","JFK"],["JFK","DDD"],["DDD","EEE"],["DDD","FFF"],["FFF","GGG"],["GGG","DDD"]]
print(Solution().findItinerary(tickets))
        