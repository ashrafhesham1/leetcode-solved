class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:

            triplets = []
            nums = sorted(nums)

            for i in range(len(nums)):
                if i != 0 and nums[i-1] == nums[i] :
                    continue

                l, r = i+1 , len(nums)-1
                while r > l :
                    triplet = nums[i] + nums[l] + nums[r]
                    if triplet > 0 :
                        r -= 1
                    elif triplet < 0 :
                        l +=1
                    else:
                        triplets.append([nums[i],nums[l],nums[r]])
                        l += 1
                        while nums[l] == nums[l-1] and l < r :
                            l +=1
            return triplets