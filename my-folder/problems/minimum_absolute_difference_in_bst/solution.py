# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inOrder(self, node):
        if not node:
            return
        self.inOrder(node.left)
        if self.prv:
            self.min = min(self.min, abs(node.val - self.prv.val))
        self.prv = node
        self.inOrder(node.right)

    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        self.prv = None
        self.min = float('inf')
        self.inOrder(root)
        return self.min