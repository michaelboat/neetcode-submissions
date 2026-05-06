class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ct = 0
        myset = set()
        j = 0
        for i in range(len(s)):
            while s[i] in myset:
                myset.remove(s[j])
                j += 1

            myset.add(s[i])
            ct = max(ct, i-j+1)

        return ct


            




        