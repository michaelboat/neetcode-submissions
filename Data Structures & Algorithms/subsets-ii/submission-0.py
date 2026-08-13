class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        def backtrack(i:int):

            #if i == len(nums):
            res.append(curr[:])
            #   return

            for j in range(i, len(nums)):
                if j > i and nums[j] == nums[j-1]:
                    continue
                curr.append(nums[j])
                backtrack(j+1)
                curr.pop()
                #backtrack(j+1)


        res, curr = [], []
        nums.sort()
        backtrack(0)
        return res

        