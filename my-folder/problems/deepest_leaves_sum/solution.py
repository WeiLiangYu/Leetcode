# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        d = deque([root])
        while d:
            dlen = len(d)
            sum = 0
            for _ in range(dlen):
                node = d.pop()
                sum += node.val
                if node.left:
                    d.appendleft(node.left)
                if node.right:
                    d.appendleft(node.right)
        return sum
                