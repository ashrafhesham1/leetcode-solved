class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        dupHash = {}
        for i,num in enumerate(nums):
            if num not in dupHash :
                dupHash[num] = [i]
            else:
                for j in dupHash[num] :
                    if abs(i-j) <= k : return True
                dupHash[num].append(i)
        return False