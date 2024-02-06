# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        d = deque([root])
        ans = []
        while d:
            row = 0
            dlen = len(d)
            for i in range(dlen):
                node = d.popleft()
                row += node.val
                if node.left:
                    d.append(node.left)
                if node.right:
                    d.append(node.right)
            ans.append(row/dlen)
        return ans
        