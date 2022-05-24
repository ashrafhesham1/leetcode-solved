class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        dividendAbs, divisorAbs = abs(dividend), abs(divisor)
        posLimit, negLimit = (2**31) -1, (-2**31)

        res = 0
        while divisorAbs <= dividendAbs :
            temp = divisorAbs
            step = 1
            while temp <= dividendAbs :
                dividendAbs -= temp
                res += step
                temp += temp
                step += step
                

        if (dividend < 0 and divisor > 0) or (dividend > 0 and divisor < 0) : 
            res = -res
        
        return min(posLimit,max(negLimit,res))