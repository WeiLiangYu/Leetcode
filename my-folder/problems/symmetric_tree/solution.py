# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root: return True 
        return self.Sym(root.left, root.right)
    def Sym(self, p:Optional[TreeNode], q:Optional[TreeNode]) -> bool:
        if not p and not q: return True #2 None
        if not p or not q: return False #1 None
        if p.val != q.val: return False
        return self.Sym(p.left,q.right) and self.Sym(p.right,q.left) ## True and True = True

        