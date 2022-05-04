# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def _preorder(self, root: TreeNode, output: list):

        if root == None: return

        output.append(root.val)
        self._preorder(root.left,output)
        self._preorder(root.right,output)
        
        
    def preorderTraversal(self, root: TreeNode) -> list[int]:
        output = []
        self._preorder(root,output)
        return output