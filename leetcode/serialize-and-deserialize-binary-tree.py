class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def serialize_helper(root, arr):
    arr.append(str(root.val))
    if root.left:
        serialize_helper(root.left, arr)
    else:
        arr.append('*')

    if root.right:
        serialize_helper(root.right, arr)
    else:
        arr.append('*')

def serialize(root):
    if not root:
        return ""

    arr = []
    serialize_helper(root, arr)
    s = '|'.join(arr)

    return s

def deserialize_helper(arr, index = 0):
    if arr[index] == '*':
        return None

    node = TreeNode(int(arr[index]))
    if index+1 < len(arr):
        node.left = deserialize_helper(arr, index + 1)

    if index+4 < len(arr):
        node.right = deserialize_helper(arr, index + 4)

    return node

def deserialize(data):
    if not data:
        return None

    arr = data.split('|')
    return deserialize_helper(arr)
    
tree = None 

# TreeNode(1)
# tree.left = TreeNode(2)
# tree.right = TreeNode(3)
# tree.right.left = TreeNode(4)
# tree.right.right = TreeNode(5)

s = serialize(tree)
tree_new = deserialize(s)

print(s)
print(tree_new)