"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        depth = 0
        if not root:
            return 0
        d = deque([root])
        while d:
            print("1")
            depth += 1
            dlen = len(d)
            for _ in range(dlen):
                node = d.popleft()
                if node.children:
                    d.extend(node.children)
                
        return depth
                