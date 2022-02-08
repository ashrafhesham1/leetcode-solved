class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res=0
        for i in range(len(s)):
            #res = 1 if res==0 else res
            cur=s[i]
            j=i+1
            while len(s[i:len(s)])>res and j < len(s) and s[j] not in cur:
                cur+=s[j]
                j+=1
            res=len(cur) if max(res,len(cur))==len(cur) else res
        return res