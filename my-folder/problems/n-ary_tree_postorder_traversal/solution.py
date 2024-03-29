"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        self.res = deque([])
        self.dfs(root)
        return self.res
    def dfs(self, root):
        if not root:
            return
        self.res.appendleft(root.val)
        if len(root.children) > 0:
            
            for _ in range(len(root.children)):
                self.dfs(root.children.pop())