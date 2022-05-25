class Solution:
    def search(self, nums: list[int], target: int) -> int:
        
        def _binarySearch(nums: list[int], start: int, end: int, target: int):
            if start > end :
                return -1
            
            mid = (start + end) // 2
            
            if target == nums[mid] :
                return mid

            #left portion
            if nums[mid] >= nums[start]:
                if nums[mid] < target or target < nums[start] :
                    return _binarySearch(nums, mid + 1, end, target)
                else :
                    return _binarySearch(nums, start, mid - 1, target)

            
            # right portion
            else :
                if nums[mid] > target or target > nums[end] :
                    return _binarySearch(nums, start, mid - 1, target)
                else :
                    return _binarySearch(nums, mid + 1, end, target)
        
        return _binarySearch(nums,0,len(nums) - 1, target)