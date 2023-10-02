# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
## BFS
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        if not root: return []

        # 初始; queue = [node] = Level1的元素 = 3
        queue = deque([root])

        while queue: # 重複次數: Tree的最大層數
            level_val = [] # 當層的值
            for _ in range(len(queue)):
                node = queue.popleft()
                level_val.append(node.val) # 儲存當層左邊的元素值

                if node.left: 
                    queue.append(node.left) # 將下層左子節儲存，至下一回圈處理
                if node.right:
                    queue.append(node.right)
            res.append(level_val)
        return res
 