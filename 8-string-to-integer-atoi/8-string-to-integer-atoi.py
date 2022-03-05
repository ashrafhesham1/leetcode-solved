class Solution:
    def myAtoi(self, s: str) -> int:
        
        maxInt = 2147483647
        minInt = -2147483648

        s = s.strip()

        index,sign=0,1
        if s and ( s[0] == '-' or s[0] == '+' ):
            index = min(1,len(s))
            if s[0] == '-' :
                sign = -1

        res=0
        while index < len(s) :

            digit = ord(s[index]) - ord('0')

            if digit >= 0 and digit <= 9 :
                res = res*10 + digit
                index += 1
            else:break

        if  sign == 1 : return min(res*sign, maxInt) 
        else : return max(res*sign, minInt)