class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = ''
        carry = 0
        a,b = a[::-1],b[::-1]

        for i in range( max( len(a), len(b) ) ) :
            digitA = int(a[i]) if i < len(a) else 0
            digitB = int(b[i]) if i < len(b) else 0
            digitSum = digitA + digitB + carry
            curRes = digitSum % 2
            carry = digitSum // 2
            res = str(curRes) + res

        return '1'+res if carry else res