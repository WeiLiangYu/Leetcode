# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root: # 節點為 None
            return targetSum == None
        
        # 葉節點
        if not root.left and not root.right:
            return targetSum == root.val
        
        # 節點，使用遞歸檢查左與右的節點和
        return self.hasPathSum(root.left, targetSum - root.val) or self.hasPathSum(root.right, targetSum - root.val)
            
        