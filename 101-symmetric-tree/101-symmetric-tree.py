# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def isSymmetric(self, root: TreeNode) -> bool:
        return self.isMirrorTree(root.left,root.right)

    def isMirrorTree(self, p: TreeNode, q: TreeNode) -> bool:

        if not p and not q :
            return True

        if ( not p or not q ) or p.val != q.val :
            return False

        return self.isMirrorTree(p.right,q.left) and self.isMirrorTree(p.left,q.right)