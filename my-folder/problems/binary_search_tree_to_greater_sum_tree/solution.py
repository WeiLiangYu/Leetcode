# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        self.dfs(root, 0)
        return root
    def dfs(self, root, val):
        if not root:
            return val
        val = self.dfs(root.right, val)
        val += root.val # 兩邊都遞迴，但只加右邊值
        root.val = val

        return self.dfs(root.left, val)