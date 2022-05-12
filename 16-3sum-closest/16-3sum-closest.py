class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        nums.sort()
        distance = float('inf')
        for i in range(len(nums)-2):
            l, r = i+1, len(nums)-1
            new_target = target - nums[i]
            while l < r :
                sum = nums[l] + nums[r]
                if abs(distance) > abs(new_target - sum) :
                    distance = (new_target - sum)
                if sum == new_target :
                    return target
                if sum < new_target :
                    l += 1
                else:
                    r -= 1
        return target - distance