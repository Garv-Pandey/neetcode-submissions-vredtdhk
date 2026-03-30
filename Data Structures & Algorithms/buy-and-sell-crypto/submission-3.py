class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0

        minPrice = prices[0]

        for p in prices:
            minPrice = min(p, minPrice)

            profit = max(profit, p-minPrice)

        return profit