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
        return parent1.elements

    if parent1.elements < parent2.elements:
        parent1.parent = parent2
        parent2.elements += parent1.elements
        
        return parent2.elements
    else:
        parent2.parent = parent1
        parent1.elements += parent2.elements

        return parent1.elements

def findSet(node, map):
    currNode = node
    parent = currNode.parent

    while parent != currNode:
        currNode = parent
        parent = parent.parent

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
        print(q1,q2,groupMax)
        
        if maxx < groupMax:
            maxx = groupMax

        maxs.append(maxx)

    return maxs

# queries = [[1000000000,23],[11,3778],[7,47],[11,1000000000]]
# queries = [[1,2],[3,4],[1,3],[5,7],[5,6],[7,4]]
# queries = [[6,4],[5,9],[8,5],[4,1],[1,5],[7,2],[4,2],[7,6]]
queries = [[6,4],[7,2],[4,2],[7,6]]
print(maxCircle(queries))
# map = {}
# makeSet(1, map)
# makeSet(2, map)
# makeSet(3, map)
# makeSet(4, map)

# union(1, 2, map)
# union(1, 3, map)
# union(3, 4, map)

# parent = findSet(map[1], map)
# print(parent.data, parent.elements)



