import sys


class Solution:
    def myAtoi(self, s: str) -> int:

        s = s.strip()
        
        if not s : return 0

        sign, start = 1, 0
        if s[0] == '-' or s[0] == '+':
            start = min(1,len(s)-1)
            if s[0] == '-':
                sign = -1

        nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

        if s[start] not in nums : return 0

        end = start
        while end < len(s) - 1 :
            if s[end + 1] not in nums:
                break

            end += 1

        num = int(s[start:end + 1]) * sign
        return min(num, 2147483647) if num >= 0 else max(num, -2147483648)