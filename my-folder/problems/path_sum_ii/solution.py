# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        # 無節點
        if not root: return []
        self.targetSum = targetSum # 全class通用參數
        res = [] # 儲存正確的PATH、初始化
        path = [root.val]
        self.dfs(root, res, root.val, path)
        return res

    def dfs(self, root, res: List[str], sum: int, path: List[int]):
        if not root.left and not root.right and sum == self.targetSum: # 葉節點
            return res.append(path)
        if root.left:
            # 使用 append 會使 path 不初始化
            self.dfs(root.left, res, sum + root.left.val, path + [root.left.val])
        if root.right:
            self.dfs(root.right, res, sum + root.right.val, path + [root.right.val])
            
