class Solution:
    def generateParenthesis(self, n: int) -> List[str]:


        def backtrack(l:int, r:int):

            if l == r == n:
                res.append("".join(curr))
                return

            if l < n:
                curr.append('(')
                backtrack(l+1, r)
                curr.pop()

            if l > r:
                curr.append(')')
                backtrack(l, r+1)
                curr.pop()

        res, curr = [], []
        backtrack(0, 0)
        return res

        