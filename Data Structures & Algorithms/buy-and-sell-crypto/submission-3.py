class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 1
        maxProfit = 0
        profit = 0

        while r < len(prices):
            if prices[r] > prices[l]:
                profit = prices[r] - prices[l]
            else:
                l = r
            maxProfit = max(profit, maxProfit)
            r += 1
        
        return maxProfit