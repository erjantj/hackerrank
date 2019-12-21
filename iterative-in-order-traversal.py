class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None

def callback(node):
    print('callback', node.value)      

def iterativeInOrderTraversal(tree, callback):
    if not tree:
        return 

    prev = None
    curr = tree

    while curr:
        if curr.left and prev == curr.parent:
            # go left
            prev = curr
            curr = curr.left
        else:
            if not curr.right or prev != curr.right:
                callback(curr)

            if curr.right and prev != curr.right:
                # go right
                prev = curr
                curr = curr.right
            else:
                prev = curr
                curr = curr.parent

def getNodes(count):
    nodes = {}
    for i in range(count):
        nodes[i+1] = Node(i+1)
    return nodes

def addNodeChildren(node, left_node, right_node):
    node.left = left_node
    node.right = right_node
    if left_node:
        left_node.parent = node
    if right_node:
        right_node.parent = node

nodes = getNodes(9)

# addNodeChildren(nodes[1], nodes[2], nodes[3])
# addNodeChildren(nodes[2], nodes[4], nodes[5])
# addNodeChildren(nodes[3], nodes[7], nodes[8])
# addNodeChildren(nodes[4], None, nodes[6])
# addNodeChildren(nodes[8], nodes[9], None)

# addNodeChildren(nodes[1], None, nodes[3])
# addNodeChildren(nodes[3], None, nodes[8])
# addNodeChildren(nodes[8], nodes[9], None)

print(iterativeInOrderTraversal(nodes[1], callback))

