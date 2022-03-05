class Solution:
    def maxArea(self, height: list[int]) -> int:
        
        l, r = 0, len(height) - 1
        maximum = 0
        
        while r > l :
            
            cur = (r - l) * min(height[r],height[l])
            maximum = max(maximum,cur)
            
            if height[r] > height [l] : l += 1
            else: r -= 1
        
        return maximum