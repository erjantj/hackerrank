from collections import defaultdict

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def traverse(self, root, levels, index):
        if not root:
            return 

        levels[index] += root.val
        self.traverse(root.left, levels, index+1)
        self.traverse(root.right, levels, index+1)

    def maxLevelSum(self, root):
        levels = defaultdict(int)
        self.traverse(root, levels, 1)

        maxLevel = 1
        maxSum = levels[maxLevel]

        for level, summ in levels.items():
            if summ > maxSum:
                maxSum = summ
                maxLevel = level

        return maxLevel


root = TreeNode(9)
root.left = TreeNode(7)
root.right = TreeNode(3)

# root.left.left = TreeNode(7)
# root.left.right = TreeNode(8)

print(Solution().maxLevelSum(root))