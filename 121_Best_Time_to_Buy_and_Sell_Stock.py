class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        l = 0
        for r in range(1,len(prices)):
            profit = max(profit, (prices[r] - prices[l]))

            if prices[r] < prices[l]:
                l = r
        return profit
