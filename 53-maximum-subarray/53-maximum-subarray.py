class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        if len(nums) == 1 :
            return nums[0]
        maxSum= nums[len(nums)-1]
        for i in range (len(nums)-2,-1,-1):
            nums[i] = max(nums[i],nums[i]+nums[i+1])
            maxSum = max(nums[i],maxSum)
        return maxSum