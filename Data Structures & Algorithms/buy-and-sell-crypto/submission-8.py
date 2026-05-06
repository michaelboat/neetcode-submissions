class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        if len(prices) <= 1:
            return 0
        buy, sell = prices[0], 0
        max_profit = 0

        i, j = 0, 1
        while j < len(prices):
            curr_buy = prices[i]
            curr_sell = prices[j]
            profit = prices[j] - prices[i]
            if profit < 0:
                i = j
            elif profit > max_profit:
                max_profit = profit
            j += 1
        return max_profit


            

            





        