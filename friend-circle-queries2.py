class Node(object):
    def __init__(self, data):
        self.data = data
        self.parent = self
        self.elements = 1
        
def makeSet(data, map):
    node = Node(data)
    map[data] = node

    return node

def union(data1, data2, map):
    node1 = map[data1]
    node2 = map[data2]

    parent1 = findSet(node1, map)
    parent2 = findSet(node2, map)


    if parent1.data == parent2.data:
        return

    parent1.elements += parent2.elements
    parent2.elements = parent1.elements

    parent2.parent = parent1

    return parent1.elements

def findSet(node, map, elements = None):
    parent = node.parent
    if not elements:
        elements = node.elements
    if parent == node:
        return parent

    parent = findSet(node.parent, map, elements+1)
    node.parent = parent
    node.elements = parent.elements

    return parent

def maxCircle(queries):
    map = {}
    maxx = 0
    maxs = []

    for query in queries:
        q1,q2 = query
        if not map.get(q1, None):
            makeSet(q1, map)
        if not map.get(q2, None):
            makeSet(q2, map)
        groupMax = union(q1, q2, map)
        
        if maxx < groupMax:
            maxx = groupMax

        maxs.append(maxx)

    return maxs

queries = [[1000000000,23],[11,3778],[7,47],[11,1000000000]]
# queries = [[1,2],[3,4],[1,3],[5,7],[5,6],[7,4]]
# print(maxCircle(queries))
map = {}
makeSet(1, map)
makeSet(2, map)
makeSet(3, map)
makeSet(4, map)

union(1, 2, map)
union(1, 3, map)
union(3, 4, map)

parent = findSet(map[1], map)
print(parent.elements)


