# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int: 
        #TreeNode已在參數裡 -> 輸出Function為maxDepth(root)，並非root.maxDepth()
        if root == None:  # if not root:
            return 0
        else :
            return max(self.maxDepth(root.left),self.maxDepth(root.right)) + 1 # 1:計算迴圈次數