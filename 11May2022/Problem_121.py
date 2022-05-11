#https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1 #left=buy, right = sell
        maxP = 0
        
        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                print(profit)
                maxP = max(maxP, profit)
                # print(maxP)
            else:
                l = r
            r += 1
        return maxP
        
        