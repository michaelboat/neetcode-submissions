class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # so we are looking for the longest substring with k distinct 
        # characters
        # use a sliding window approach
        chars = {}
        # s = k + 1 # s for no. of substitutions(as it relates to k)
        ct = 0
        j = 0

        for i in range(len(s)):
            chars[s[i]] = chars.get(s[i], 0) + 1
            while i-j+1 - max(chars.values()) > k:
                chars[s[j]] -= 1
                j += 1
            
            ct = max(ct, i-j+1)

        return ct

        