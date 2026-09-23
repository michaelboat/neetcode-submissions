from functools import cache, lru_cache
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:

        @lru_cache(maxsize=None)
        def helper(curr, idx):
            
            if curr == 0:
                return 1

            if curr < 0 or idx >= len(coins):
                return 0

            return helper(curr - coins[idx], idx) + helper(curr, idx+1)

        return helper(amount, 0)