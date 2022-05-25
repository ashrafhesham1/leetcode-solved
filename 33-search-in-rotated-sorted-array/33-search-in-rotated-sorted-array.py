class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        
        while l <= r :
            mid = (l + r) // 2
            if nums[mid] == target :
                return mid
            
            # left portion
            if nums[mid] >= nums[l]:
                if nums[mid] < target or target < nums[l] :
                    l = mid + 1
                else :
                    r = mid - 1
            
            # right portion
            else :
                if nums[mid] > target or target > nums[r] :
                    r = mid - 1
                else :
                    l = mid + 1
        
        return -1
                    