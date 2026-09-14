class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # let's optimize
        def dfs(subsetSum, n):
            if subsetSum == 0:
                return True

            if n == 0 or subsetSum < 0:
                return False

            if dp[n][subsetSum] is not None:
                return dp[n][subsetSum]

            dp[n][subsetSum] = dfs(subsetSum-nums[n], n-1) or dfs(subsetSum, n-1)
            return dp[n][subsetSum]

    
        ln = len(nums)
        sigma = sum(nums)  
        if sigma%2 == 1:
            return False  

        dp = [[None] * ((sigma//2)+1) for i in range(ln)]
        
        return dfs(int(sigma/2), ln-1)



