class Solution:
    def searchInsertHelper(self,nums,start,end,target):
        if target < nums[start]:
            return start
        elif target > nums[end] :
             return end+1
        else:
            mid = (start + end) // 2

            if nums[mid] == target :
                return mid
            elif nums[mid] > target and nums[ mid - 1 ] < target:
                return mid
            elif nums[mid] < target and nums[ mid + 1 ] > target:
                return mid + 1
            elif nums[mid] > target :
                return self.searchInsertHelper(nums,start,mid,target)
            else:
                return self.searchInsertHelper(nums,mid+1,end,target)

    def searchInsert(self, nums: list[int], target: int) -> int:
        return self.searchInsertHelper(nums,0,len(nums)-1,target)