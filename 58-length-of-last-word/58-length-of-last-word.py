class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        word = False
        length = 0
        for i in range(len(s)-1,-1,-1):
            if s[i] == ' ' and word:
                break
            elif s[i] != ' ' :
                word =True
            if word :
                length += 1
        return length