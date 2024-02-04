# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.res = 0
    def findTilt(self, root: Optional[TreeNode]) -> int:
        self.nodesum(root)
        return self.res
    def nodesum(self, root):
        if not root:
            return 0
        else:
            right = self.nodesum(root.left)
            left = self.nodesum(root.right)
            self.res += abs(right-left)
            return root.val + right + left
