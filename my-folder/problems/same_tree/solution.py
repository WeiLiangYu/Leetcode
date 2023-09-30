# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q: # if p == None and q == None: 最後一層的值都不存在時
            return True
        elif not p or not q: #其中一邊到最底層
            return False
        if p.val != q.val : 
            return False #當層的值不相等
        return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right) # Flase and True = Flase