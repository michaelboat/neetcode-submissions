class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        res = []

        def backtrack(i:int):

            if i == len(nums):
                res.append(curr[:])
                return

            curr.append(nums[i])
            backtrack(i+1)
            curr.pop()
            backtrack(i+1)

        curr = []
        backtrack(i=0)

        return res