# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if not root: return []
        res = [] # 儲存所有路徑的字串(string)
        self.way(root, res, str(root.val)) 
        return res
    
    def way(self, root, res:List[str], path:str): # path: "遞歸節點的值 -> " + "當前節點的值"
        if not root.left and not root.right: #None
            res.append(path) # res = ["root.val"]
        if root.left: # 左子節點存在
            self.way(root.left, res, path + "->" + str(root.left.val)) # 累積路徑+左子節點值
        if root.right: # 右子節點存在
            self.way(root.right, res, path + "->" + str(root.right.val)) # 累積路徑+右子節點值



        