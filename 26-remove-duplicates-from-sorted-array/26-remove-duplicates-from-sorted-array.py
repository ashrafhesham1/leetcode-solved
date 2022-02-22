class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        last = nums[0]
        k=len(nums)

        for i in range(1,k):
            if nums[i] == last :
                nums[i] = float('inf')
                k-=1
            else:
                last = nums[i]

        nums.sort()
        
        return k