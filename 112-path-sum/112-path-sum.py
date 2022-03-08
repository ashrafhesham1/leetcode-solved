# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        if not root : return root
        def dfs(root,target,cur):
            if root and not root.left and not root.right :
                if cur + root.val == target :
                    return True
                else:
                    return False
            
            res = False
            if root.left : res = res or dfs(root.left, target, cur + root.val)
            if root.right : res = res or  dfs(root.right, target, cur + root.val)
            
            return res
        
        return dfs(root,targetSum,0)