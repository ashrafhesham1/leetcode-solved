class Solution:
    def nextPermutation(self, nums: list[int]) -> None:
        pivot = 0
        for i in range(len(nums)-1,0,-1):
            if nums[i-1] < nums [i] :
                pivot = i 
                break
        if pivot == 0 : 
            nums.sort()
            return 
        
        nextLarger = len(nums) - 1
        while nums[nextLarger] <= nums[pivot - 1] :
            nextLarger -= 1
        
        nums[pivot - 1], nums[nextLarger] = nums[nextLarger], nums[pivot - 1]
        nums[pivot :] = reversed(nums[pivot :])
        
        return