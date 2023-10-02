# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# BFS
from collections import deque
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        res = deque([]) # 答案

        # 初始化
        queue = deque([root])
        
        while queue:
            level_val = []
            for _ in range(len(queue)):
                node = queue.popleft() # 取出左第一個node
                level_val.append(node.val) # 將node值加入此level的value陣列

                # 檢查左右子節點，並加入queue
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            res.appendleft(level_val) # 將當層節點值加入res陣列的前方
        
        return list(res)


             