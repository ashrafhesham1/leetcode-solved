class Solution:
    def alphanum(self,s: str):
        newS = ''
        for i in s:
            if i.isalnum():
                newS+=i.lower()

        return newS

    def isPalindrome(self, s: str) -> bool:
        s = self.alphanum(s)
        i,j = 0,len(s)-1
        while j > i :
            if s[i]!=s[j]:
                return False
            i+=1
            j-=1
        return True