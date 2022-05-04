# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def _postorder(self, root: TreeNode, output: list):

        if root == None: return

        self._postorder(root.left,output)
        self._postorder(root.right,output)
        output.append(root.val)

        
        
    def postorderTraversal(self, root: TreeNode) -> list[int]:
        output = []
        self._postorder(root,output)
        return output