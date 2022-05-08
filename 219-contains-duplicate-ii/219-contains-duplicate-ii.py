class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        dupHash = {}
        for i,num in enumerate(nums):
            if num not in dupHash :
                dupHash[num] = i
            else:
                if abs(i-dupHash[num]) <= k : return True
                dupHash[num] = i
        return False