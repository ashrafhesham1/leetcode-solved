class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        maxSum = nums[0]
        curSum = 0

        for num in nums :
            if curSum < 0 :
                curSum = 0
            curSum += num
            maxSum = max(maxSum,curSum)

        return maxSum