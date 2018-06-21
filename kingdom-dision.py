import sys
import pprint

modd = 1000000007 

graph = {}
tree = {}
parent = {1:0}
memo = {}

def dfs(graph, size):
	openSet = [1]
	visited = [False]*size

	while len(openSet) > 0 :
		node = openSet[0]
		del openSet[0]
		visited[node] = True

		for connectedNode in graph[node]:
			if not visited[connectedNode]:
				if node not in tree:
					tree[node] = []
				tree[node].append(connectedNode)
				parent[connectedNode] = node
				openSet.append(connectedNode)


def solve(root, color, ally):
	if memo[root][color][ally] != None:
		return  memo[root][color][ally]

	# if leaf
	if root not in tree:
		if ally:
			memo[root][color][ally] = 1
		if not ally:
			memo[root][color][ally] = 0
		return memo[root][color][ally]

	count=invalid=1

	for node in tree[root]:
		if node != parent[root]:
			count *= solve(node, 1-color, False) + solve(node, color, True)
			invalid *= solve(node, 1-color, False)
			count %= modd
			invalid %= modd

	if not ally:
		count = count - invalid

	memo[root][color][ally] = count%modd

	return memo[root][color][ally]

with open('input.txt') as f:
	content = f.readlines()
	n = int(content[0].strip())
	
	for i in range(1,n):
		nodeA, nodeB = [int(x) for x in content[i].strip().split()]
		memo[nodeA] = {0:{True: None, False: None},1:{True: None, False: None}}
		memo[nodeB] = {0:{True: None, False: None},1:{True: None, False: None}}

		if nodeA not in graph:
			graph[nodeA] = []
		if nodeB not in graph:
			graph[nodeB] = []

		graph[nodeA].append(nodeB)
		graph[nodeB].append(nodeA)

	dfs(graph, n+1 )
	result = solve(1, 0, False) * 2
	pprint.pprint(memo)
	print(result%modd)
