class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        def backtrack(n:int):

            if n == len(nums):
                res.append(curr[:])
                return

            for i in range(len(nums)):
                if nums[i] not in curr:
                    curr.append(nums[i])
                    backtrack(n+1)
                    curr.pop()

        res, curr = [], []
        backtrack(0)

        return res