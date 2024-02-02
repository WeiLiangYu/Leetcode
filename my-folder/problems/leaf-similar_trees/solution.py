# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        # seq_1 = self.leafSeq(seq=[], root=root1)
        # seq_2 = self.leafSeq(seq=[], root=root2)
        # return seq_1 == seq_2
        seq_1 = []
        seq_2 = []
        self.leafSeq(seq=seq_1, root=root1)
        self.leafSeq(seq=seq_2, root=root2)
        return seq_1 == seq_2

    def leafSeq(self, seq, root):
        if not root:
            return 
        else:
            if not root.right and not root.left:
                seq.append(root.val)
            if root.left:
                self.leafSeq(seq, root.left)
            if root.right:
                self.leafSeq(seq, root.right)
        # return seq
