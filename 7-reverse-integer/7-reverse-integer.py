class Solution:
    def reverse(self, x: int) -> int:

        isNeg = False
        if x < 0 :
            x *= -1
            isNeg = True

        reversedX=0
        while x :
            reversedX += x % 10
            reversedX *= 10
            x //= 10

        reversedX = reversedX //10
        if reversedX.bit_length() > 31 :
            return 0
        return reversedX if not isNeg else reversedX*-1