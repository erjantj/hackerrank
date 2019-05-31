class Node:
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors

def helper(node, visited):
    copyNode = Node(node.val, [])
    visited[node.val] = copyNode

    for neighbor in node.neighbors:
        if not neighbor.val in visited:
            copyNeighbor = helper(neighbor, visited)
        copyNode.neighbors.append(visited[neighbor.val])

    return copyNode

def cloneGraph(node):
    if not node:
        return None

    visited = {}
    copyNode = helper(node, visited)

    return copyNode


node1 = Node(1, [])
node2 = Node(2, [node1])
node3 = Node(3, [node2])
node4 = Node(4, [node1, node3])

node1.neighbors.append(node2)
node1.neighbors.append(node4)
node2.neighbors.append(node3)
node3.neighbors.append(node4)

copyNode = cloneGraph(node1);

print(copyNode.neighbors[0].neighbors[0].val)

