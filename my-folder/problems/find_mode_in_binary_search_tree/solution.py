# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.count = dict()
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        self.dfs(root)
        res = []
        max_val = 0
        for val in self.count.values():
             max_val = max(max_val, val)
        # max_val = max(self.count.values())
        for key in self.count: 
            if self.count[key] == max_val:
                res.append(key)
        return res
    def dfs(self, root):
        if not root:
            return
        # dfs
        self.dfs(root.left)
        self.countNumbers(root)
        self.dfs(root.right)
        
    def countNumbers(self, node):
        if node.val in self.count:
            self.count[node.val] += 1
        else:
            self.count[node.val] = 1

