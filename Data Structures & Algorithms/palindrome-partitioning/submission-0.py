class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        
        res, curr = [], []

        def isPal(s:str, l:int, r:int) -> bool:
            while l < r:
                if s[l] != s[r]:
                    return False
                l, r = l+1, r-1
            return True


        def backtrack(i:int):

            # base case
            if i == len(s):
                res.append(curr[:])
                return

            for j in range(i, len(s)):
                if isPal(s, i, j):
                    curr.append(s[i:j+1])
                    backtrack(j+1)
                    curr.pop()


        backtrack(0)
        return res