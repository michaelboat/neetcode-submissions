from functools import cache, lru_cache
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:


        # 2^(n)
        @lru_cache(maxsize=None)
        def helper(curr, idx):

            if idx == len(nums):
                return 1 if curr == target else 0 

            return helper(curr + nums[idx], idx + 1) + helper(curr - nums[idx], idx + 1)

        return helper(0, 0)
        