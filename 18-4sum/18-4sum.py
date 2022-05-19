class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:

        def ksum(nums: List[int], target: int, k:int) -> List[List[int]] :
            res = []

            if not nums :
                return res
            limit = target // k
            if nums[0] > limit or nums[-1] < limit :
                return res

            if k == 2 :
                return twoSum(nums, target)

            for i in range(len(nums)):
                if i == 0 or nums[i - 1] != nums[i]:
                    for subset in ksum( nums[i + 1:], target - nums[i], k - 1 ):
                        res.append([nums[i]] + subset)
            return res
        def twoSum(nums: List[int], target: int ) -> List[List[int]] :
            res = []
            l, r = 0, len(nums)-1
            while r > l :
                sum = nums[l] + nums[r]
                if sum > target or ( r < len(nums) - 1 and nums[r] == nums[r + 1]) :
                    r -= 1
                elif target > sum or ( l > 0 and nums[l] == nums[l - 1]):
                    l += 1
                else :
                    res.append([nums[l],nums[r]])
                    r -= 1
                    l += 1
            return res

        nums.sort()
        return ksum(nums,target,4)

s = Solution()
s.fourSum([1,0,-1,0,-2,2],0)