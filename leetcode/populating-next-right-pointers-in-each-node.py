class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None


def helper(root):
    if root.left and root.right:
        root.left.next = root.right

        if root.next:
            root.right.next = root.next.left

        helper(root.left)
        helper(root.right)

def connect(root):
    if not root:
        return

    helper(root)


node = TreeLinkNode(-1)
node.left = TreeLinkNode(0)
node.right = TreeLinkNode(1)

node.left.left = TreeLinkNode(2)
node.left.right = TreeLinkNode(3)

node.right.left = TreeLinkNode(4)
node.right.right = TreeLinkNode(5)

node.left.left.left = TreeLinkNode(6)
node.left.left.right = TreeLinkNode(7)
node.left.right.left = TreeLinkNode(8)
node.left.right.right = TreeLinkNode(9)

node.right.left.left = TreeLinkNode(10)
node.right.left.right = TreeLinkNode(11)
node.right.right.left = TreeLinkNode(12)
node.right.right.right = TreeLinkNode(13)



print(connect(node))

print(node.left.right.right.next.val)