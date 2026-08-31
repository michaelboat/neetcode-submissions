class Solution:
    def rob(self, nums: List[int]) -> int:

        if not nums:
            return 0

        ln = len(nums)
        if ln <= 2:
            return max(nums)
        # since house are arranged in a circle
        # you can find the answer by finding the maximum between robbing(optimally)
        # house 0 through ln-2, and 1 though ln-1
        # return the max between the two.

        ########## first cyle #############
        best, dp = 0, [0]*ln

        for i in range(ln-1):
            dp[i+1] = nums[i] + best
            best = max(dp[i], best)

        x = max(dp)
        ########## second cycle ############
        best, dp = 0, [0]*ln
        for i in range(1, ln):
            dp[i] = nums[i] + best
            best = max(dp[i-1], best)

        y = max(dp)

        return max(x, y)
            
            