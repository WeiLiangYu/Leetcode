# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:

        def dp(root) -> List[int]:
            if not root: return [0,0]

            # [偷下左樹節點,不偷下左樹節點]
            left = dp(root.left)
            #  [偷下右樹節點,不偷下右樹節點]
            right = dp(root.right)

            # 偷當前節點 = 節點值 + 不偷下左下右節點值
            steal = root.val + left[1] + right[1]
            # 不偷當前節點 = max(偷下左值,不偷下左值) + max(偷下右值,不偷下右值)
            nosteal = max(left) + max(right)

            # [偷當前節點值,不偷當前節點值]
            return [steal, nosteal]
        # max(偷 root 值, 不偷 root 值)
        return max(dp(root))


            
        