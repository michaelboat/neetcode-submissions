class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        digit_map = {
            '2': "abc", '3': "def", '4': "ghi",
            '5': "jkl", '6': "mno", '7': "pqrs",
            '8': "tuv", '9': "wxyz"
        }
        

        def dfs(i:int):

            if len(curr) == len(digits):
                res.append("".join(curr[:]))
                return 

            for char in digit_map[digits[i]]:
                #if char not in curr:
                curr.append(char)
                   # break
                dfs(i+1)
                curr.pop()

        if len(digits) <= 0:
            return []
        res, curr = [], []
        dfs(0)
        return res