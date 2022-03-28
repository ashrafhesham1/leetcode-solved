class Solution:
    def maxProfit(self, prices: list[int]) -> int:

        i, j = 0, 1
        maxProf = 0

        while j < len(prices) :

            if prices[j]>prices[i] :
                prof = prices[j]-prices[i]
                maxProf = max(prof,maxProf)
            else:
                i = j

            j += 1

        return maxProf