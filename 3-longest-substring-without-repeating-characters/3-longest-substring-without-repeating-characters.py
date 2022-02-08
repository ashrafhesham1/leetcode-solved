class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest=0
        exist=set()
        left=0
        for right in range (len(s)):
            while s[right] in exist:
                exist.remove(s[left])
                left+=1
            exist.add(s[right])
            longest=max(longest,right-left+1)
        return longest