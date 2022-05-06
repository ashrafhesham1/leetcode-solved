class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        nums.sort()
        for i in range((len(nums)//2)+1):
            if nums[i] == nums[i+(len(nums)//2)]:
                return nums[i]
        return None