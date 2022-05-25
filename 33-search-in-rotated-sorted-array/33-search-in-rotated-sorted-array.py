class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        def _binarySearch(nums: list[int], start: int, end: int, target: int):
            if start > end :
                return -1

            mid = (start + end) // 2 
            if nums[mid] == target :
                return mid
            elif nums[mid] > target :
                return _binarySearch(nums, start, mid - 1, target)
            else:
                return _binarySearch(nums, mid + 1, end, target)
            
        if len(nums) == 1 :
            return 0 if target == nums[0] else -1
        
        # determine the pivot position
        pivot = 0
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                pivot = i 
                break
        
        # determine in  which sub array the target may exist 
        # binary search for the target
        if target >= nums[0] and target <= nums[pivot]:
            return _binarySearch(nums, 0, pivot, target)
        elif target >= nums[pivot + 1] and target <= nums[len(nums) - 1]:
            return _binarySearch(nums, pivot + 1, len(nums) - 1, target)
        else:
            return -1
        
        # return