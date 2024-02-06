# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if not root:
            return 0
        d = deque([root])
        sum = 0
        while d: 
            # dlen = len(d)
            # for _ in range(dlen):
            
            node = d.pop()
            if node:
                if node.val <= high and node.val >= low:
                    sum += node.val
                if node.val < high:
                    d.append(node.right)
                if node.val > low:
                    d.append(node.left)
        return sum