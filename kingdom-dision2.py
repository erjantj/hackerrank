import sys
import pprint

modd = 1000000007 

graph = {}
tree = {}
parent = {1:0}
memo = {}
nodes = []

def dfs(graph, size):
	openSet = [1]
	visited = [False]*size

	while len(openSet) > 0 :
		node = openSet[0]
		del openSet[0]
		visited[node] = True
		nodes.append(node)

		for connectedNode in graph[node]:
			if not visited[connectedNode]:
				if node not in tree:
					tree[node] = []
				tree[node].append(connectedNode)
				parent[connectedNode] = node
				openSet.append(connectedNode)


def solve(size):
	color = 0
	ally = 0
	for i in range(size - 1, -1, -1):
		root = nodes[i]

		# if leaf
		if root not in tree:
			memo[root][color][True] = 1
			memo[root][1-color][True] = 1
			memo[root][color][False] = 0
			memo[root][1-color][False] = 0
		else:
			count=invalid=1

			for node in tree[root]:
				if node != parent[root]:
					count *= memo[node][1-color][False] + memo[node][color][True]
					invalid *= memo[node][1-color][False]
					count %= modd
					invalid %= modd

			memo[root][color][True] = count%modd
			memo[root][1-color][True] = memo[root][color][True]
			memo[root][color][False] = (count - invalid)%modd
			memo[root][1-color][False] = memo[root][color][False]

	return memo[1][color][ally]

with open('input.test.txt') as f:
	content = f.readlines()
	n = int(content[0].strip())
	
	for i in range(1,n):
		nodeA, nodeB = [int(x) for x in content[i].strip().split()]
		memo[nodeA] = {0:{True: None, False: 0},1:{True: None, False: None}}
		memo[nodeB] = {0:{True: None, False: 0},1:{True: None, False: None}}

		if nodeA not in graph:
			graph[nodeA] = []
		if nodeB not in graph:
			graph[nodeB] = []

		graph[nodeA].append(nodeB)
		graph[nodeB].append(nodeA)

	dfs(graph, n+1 )
	result = solve(n) * 2
	print(result%modd)
