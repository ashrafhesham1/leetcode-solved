class Solution:
    def get_next(self,n: int):
        sum = 0
        while n :
            n, d = divmod(n,10)
            sum += d ** 2
        return sum

    def isHappy(self, n: int) -> bool:
        slow, fast = n, self.get_next(n)
        while fast != 1 and slow != fast:
            slow = self.get_next(slow)
            fast = self.get_next(self.get_next(fast))
        
        return fast==1