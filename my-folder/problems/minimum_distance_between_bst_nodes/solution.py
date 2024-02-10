# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inOrder(self, root):
        # 中序遍歷，在BST會依照小到大排序
        if not root:
            return
        self.inOrder(root.left)
        if self.pre:
            self.min = min(self.min, abs(root.val - self.pre.val))
        self.pre = root
        self.inOrder(root.right)
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        self.min = float('inf') # 無限大
        # self.min = 100 # 無限大
        self.pre = None
        self.inOrder(root)
        return self.min