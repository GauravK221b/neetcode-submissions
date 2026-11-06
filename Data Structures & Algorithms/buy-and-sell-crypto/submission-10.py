class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        maxp = 0
        for r in range(len(prices)):
            if prices[r] > prices[l]:
                maxp =max(maxp, prices[r]-prices[l])
            else:
                buy = prices[r]
                l = r

        return maxp

