# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        self.res = 0
        self.dfs(root)
        return self.res
    def dfs(self, root):
        if not root:
            return 0,0
        left, lcount = self.dfs(root.left) # 總和與數量
        right, rcount = self.dfs(root.right)
        if root.val == (root.val + left + right)//(lcount + rcount + 1): # 整除
            self.res += 1 
        # print(root.val + left + right)
        return root.val+left+right, lcount+rcount+1
