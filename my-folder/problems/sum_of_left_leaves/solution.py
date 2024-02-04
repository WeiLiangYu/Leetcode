# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.left_sum = 0
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if not root:
            return self.left_sum
        else:
            if root.left:
                self.sumOfLeftLeaves(root.left)
                if not root.left.left and not root.left.right:
                    self.left_sum += root.left.val
            if root.right:
                self.sumOfLeftLeaves(root.right)
        return self.left_sum # 確保有回傳
