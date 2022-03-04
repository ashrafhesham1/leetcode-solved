# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def isBalanced(self, root: TreeNode) -> bool:

        def helper (root):

            if not root :
                return [True, 0]

            left, right = helper(root.left), helper(root.right)
            isBalanced = left[0] and right[0] and abs(left[1]-right[1]) <= 1
            
            return [ isBalanced, max(left[1],right[1]) + 1 ]
        
        return helper(root)[0]