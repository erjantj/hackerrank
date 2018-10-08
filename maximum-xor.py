class Trie(object):
    def __init__(self, data = None):
        self.data = data
        self.left = None
        self.right = None

def add(root, digit):
    binary_digit = '{:032b}'.format(digit)

    node = root
    for b in binary_digit:
        if node.left and node.left.data == b:
            node = node.left
        elif node.right and node.right.data == b:
            node = node.right
        else:
            new_node = Trie(b)
            if b == '0':
                node.left = new_node
            elif b == '1':
                node.right = new_node
            node = new_node

def findMaxXor(root, digit):
    invert = False
    binary_digit = '{:032b}'.format(digit)
    node = root

    max_binary = ''

    for b in binary_digit:
        if b == '1':
            invert = True
            if node.left:
                node = node.left
            elif node.right:
                node = node.right

        elif b == '0':
            if node.right:
                invert = True
                node = node.right
            elif node.left:
                node = (node.right if invert and node.right else node.left)

        max_binary += node.data

    return int(max_binary, 2)^digit

def maxXor(arr, queries):
    trie = Trie()

    for i in arr:
        add(trie, i)

    maxs = []

    for i in queries:
        maxs.append(findMaxXor(trie, i))

    return maxs

arr = [1,3,5,7] 
queries = [17,6]

print(maxXor(arr, queries))
