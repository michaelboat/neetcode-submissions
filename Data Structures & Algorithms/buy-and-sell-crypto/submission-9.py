class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        if len(prices) <= 1:
            return 0

        max_profit = 0
        j = 0
        for i in range(1, len(prices)):
            profit = prices[i] - prices[j]
            if profit > 0:
                max_profit = max(max_profit, profit)
            else:
                j = i
            
        return max_profit


            

            





        