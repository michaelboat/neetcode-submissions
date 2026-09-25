from functools import cache, lru_cache
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:

        ln = len(coins)

        dp = [[0] * (amount+1) for _ in range(ln+1)]
        for i in range(ln+1):
            dp[i][-1] = 1

        for i in range(ln-1, -1, -1):
            for j in range(amount, -1, -1):

                #if coins[i] > j:
                dp[i][j] = dp[i+1][j]
                if j + coins[i] <= amount:
                    dp[i][j] += dp[i][coins[i] + j]

        return dp[0][0]

                




        