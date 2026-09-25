from functools import lru_cache
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        

        # callseye
        # adfscye
        # aye, cye
        @lru_cache(maxsize=None)
        def helper(i, j):

            if i >= len(text1) or j >= len(text2):
                return 0

            idx = -1
            for k in range(j, len(text2)):
                if text1[i] == text2[k]:
                    idx = k
                    break

            c1 = helper(i+1, j)
            c2 = 0
            if idx != -1:
                c2 = 1 + helper(i+1, k+1)


            return max(c1, c2) 

        return helper(0, 0)

            
        