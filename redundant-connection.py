class Node:
    def __init__(self, data):
        self.rank = 0
        self.data = data
        self.parent = None
        
class Solution:

    def makeSet(self, point):
        node = Node(point)
        node.parent = node

        return node

    def union(self, node1, node2):
        node1 = self.findSet(node1)
        node2 = self.findSet(node2)
        if node2.rank > node1.rank:
            node1, node2 = node2, node1

        node2.parent = node1
        node1.rank += 1

        return node1

    def findSet(self, node):
        parentNode = node.parent
        while node != parentNode:
            parentNode = node
            node = node.parent

        return node

    def findRedundantConnection(self, edges):
        if not edges:
            return []

        sets = {}
        for p1, p2 in edges:
            if p1 not in sets:
                sets[p1] = self.makeSet(p1)
            if p2 not in sets:
                sets[p2] = self.makeSet(p2)

        for p1, p2 in edges:
            if self.findSet(sets[p1]) == self.findSet(sets[p2]):
                return [p1,p2]
            self.union(sets[p1], sets[p2])

        return []

edges = [[1,2], [1,3], [2,3]]
edges = [[1,2], [2,3], [3,4], [1,4], [1,5]]
edges = [[1,2]]
edges = [[1,4],[3,4],[1,3],[1,2],[4,5]]
print(Solution().findRedundantConnection(edges))
        