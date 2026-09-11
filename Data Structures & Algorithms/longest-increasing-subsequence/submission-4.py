class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # return the lenght of hte strictlry increasing
        # subsequence

        ln = len(nums)

        if not nums:
            return 0
        if ln == 1:
            return 1
        
        dp = [1] * ln

        for i in range(1, ln):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[j]+1, dp[i])

        print(dp)
        return max(dp)