class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i in range(len(prices)):
            for j in range(i+1, len(prices)):
                buy = prices[i]
                sell = prices[j]- buy
                profit = max(profit, sell)
        
        return profit