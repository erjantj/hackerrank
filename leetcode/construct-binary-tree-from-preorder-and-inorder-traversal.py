class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def helper(preorder, inorder, i_index, i_start, i_end, index):
    if i_start == i_end:
        return (TreeNode(inorder[i_start]), index)

    head_val = preorder[index]
    head = TreeNode(head_val)
    in_index = i_index[head_val]

    # left
    if in_index - 1 >= i_start:
        left_node, index = helper(preorder, inorder, i_index, i_start, in_index - 1, index + 1)
        head.left = left_node

    # right
    if in_index + 1 <= i_end:
        right_node, index = helper(preorder, inorder, i_index, in_index + 1, i_end, index + 1)
        head.right = right_node

    return (head, index)


def buildTree(preorder, inorder):
    if not preorder:
        return None

    p_index = {}
    i_index = {}        

    for i in range(len(preorder)):
        p_index[preorder[i]] = i

    for i in range(len(inorder)):
        i_index[inorder[i]] = i

    i_start = 0
    i_end = len(inorder) - 1

    head, index = helper(preorder, inorder, i_index, i_start, i_end, 0)

    return head


preorder = []
inorder =  []

tree = buildTree(preorder, inorder)