# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def mergeIntoTree (self,left,right,nums):

        if right < left :
            return None

        mid = ( right + left ) // 2
        root = TreeNode(nums[mid])
        root.left = self.mergeIntoTree(left,mid-1,nums)
        root.right = self.mergeIntoTree(mid+1,right,nums)

        return root

    def sortedArrayToBST(self, nums: list[int]) -> TreeNode:
        return self.mergeIntoTree(0,len(nums)-1,nums)