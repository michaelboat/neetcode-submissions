class Solution:
    def numDecodings(self, s: str) -> int:
        
        ln = len(s)
        dp = [0] * (ln+1)
        dp[0] = 1
        dp[1] = 1 if s[0] >= "1" else 0

        for i in range(2, ln+1):
            if s[i-1] >= "1":
                dp[i] = dp[i-1]

            if s[i-2:i] >= "10" and s[i-2:i] <= "26":
                #print(i-2, s[i-2:i])
                dp[i] += dp[i-2]

        print(dp)
        return dp[-1]


        