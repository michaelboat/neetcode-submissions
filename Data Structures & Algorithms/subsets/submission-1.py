class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        # find all possible combinations essentially

        res, curr = [], []
        def backtrack(i:int):

            res.append(curr[:])

            for j in range(i, len(nums)):
                curr.append(nums[j])
                backtrack(j+1)
                curr.pop()


        backtrack(0)
        return res