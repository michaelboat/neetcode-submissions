class Solution:
    def countSubstrings(self, s: str) -> int:

        res = 0
        ln = len(s)

        dp = [[False] * ln for _ in range(ln)]

        for i in range(ln):
            dp[i][i] = True
            res += 1

        for i in range(ln-1):
            if s[i] == s[i+1]:
                dp[i][i+1] = True
                res += 1

        for diff in range(2, ln):
            for i in range(ln-diff):
                j = i + diff
                if s[i] == s[j] and dp[i+1][j-1]:
                    dp[i][j] = True
                    res += 1

        return res
        