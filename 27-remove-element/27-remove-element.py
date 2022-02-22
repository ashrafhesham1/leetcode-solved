class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        k=len(nums)

        for i in range(k):
            if nums[i]==val :
                nums[i]=float('inf')
                k-=1

        nums.sort()
        return k