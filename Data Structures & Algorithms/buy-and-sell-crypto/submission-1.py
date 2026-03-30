class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowestBuy = prices[0]
        maxProfit = 0

        for price in prices:
            lowestBuy = min(lowestBuy, price)
            maxProfit = max(maxProfit, price - lowestBuy)

        return maxProfit