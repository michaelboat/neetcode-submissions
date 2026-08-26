class Solution:
    def rob(self, nums: List[int]) -> int:
        

        # reccurrence = nums[i] + max()
        ln = len(nums)
        dp = [0] * (ln+1)
        for i in range(ln):
            curr = 0
            for j in range(i):
                curr = max(curr, dp[j])
            dp[i+1] = nums[i] + curr

        print(dp)
        return max(dp)


        