class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        def dfs(subsetSum, n):
            if subsetSum == 0:
                return True

            if n == 0 or subsetSum < 0:
                return False

            return dfs(subsetSum-nums[n], n-1) or dfs(subsetSum, n-1)

    
        ln = len(nums)
        sigma = sum(nums)  
        if sigma%2 == 1:
            return False  
        
        return dfs(sigma/2, ln-1)