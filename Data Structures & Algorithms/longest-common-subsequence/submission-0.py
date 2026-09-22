class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        M, N = len(text1), len(text2)
        dp = [[0] * (M+1) for _ in range(N+1)]

        for row in range(N-1, -1, -1):
            for col in range(M-1, -1, -1):
                if text2[row] == text1[col]:
                    dp[row][col] = 1 + dp[row+1][col+1]

                else:
                    dp[row][col] = max(dp[row+1][col], dp[row][col+1])


        return dp[0][0]