# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        d = deque([root])
        value = []
        while d:  
            dlen = len(d)
            for i in range(dlen):
                node = d.popleft()
                # print(node)
                value.append(node.val)
                if node.left:
                    d.append(node.left)
                if node.right:
                    d.append(node.right)      
        value.sort(reverse=True)
        cur = None
        for i in range(len(value)):
            if i == 0:
                cur = TreeNode(val=value[i])
            else:
                cur = TreeNode(val=value[i], right=cur)
        return  cur