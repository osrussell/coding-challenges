from typing import List

"""
**UNFINISHED**

You are given an integer array prices where prices[i] is the price of a given stock on the ith day.
On each day, you may decide to buy and/or sell the stock. 
You can only hold at most one share of the stock at any time. 
However, you can buy it then immediately sell it on the same day.
Find and return the maximum profit you can achieve.

Method: Find stretches of increasing stock

"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        low = prices[0] # we know the length is at least 1
        profit = 0
        for i in range(1, len(prices)):
            if prices[i] < prices[i-1]: # if price is decreasing
                profit += prices[i-1] - low 
                low = prices[i]
        return profit

sol = Solution()
print(sol.maxProfit([1, 2, 3, 4, 5]))