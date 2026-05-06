class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if len(t) > len(s):
            return ""

        res = []
        j = 0
        myset = Counter(t)
        for i in range(len(s)):
            j = i
            while sum(myset.values()) > 0 and j < len(s):
                if s[j] in myset and myset[s[j]] > 0:
                    myset[s[j]] -= 1
                j += 1

            if sum(myset.values()) == 0:
                print(s[i:j])
                res.append(s[i:j])
            
            myset = Counter(t)

        if res:
            return min(res, key=len)

        return ""
            

        