class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        val = 1
        for i in range( len(digits)-1 ,-1 ,-1 ) :
            newDigit = digits[i] + val
            if newDigit < 10 :
                digits[i]=newDigit
                val = 0
                break
            else:
                digits[i] = 0
        return ( [val] + digits if val != 0 else digits )