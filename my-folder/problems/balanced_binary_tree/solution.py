# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # 計算高度同時，檢查是否對稱(葉節點只會計算一次高度，減少計算量)
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root: return True
        return self.Depth(root) >= 0

    def Depth(self, root):
        if not root: return 0
        Left_depth = self.Depth(root.left)
        Right_depth = self.Depth(root.right)
        if abs(Left_depth - Right_depth) > 1 or Right_depth < 0 or Left_depth < 0:
            return -1
        return max(self.Depth(root.left), self.Depth(root.right)) + 1
    