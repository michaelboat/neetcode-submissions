class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        # we can sort the input to get rid of 
        # duplicate combinations
        res, curr = [], []
        nums.sort()
        #print(nums)
        def backtrack(i:int, curr_sum:int):

            if curr_sum == target:
                res.append(curr[:])
                return

            if curr_sum > target:
                return

            for j in range(i, len(nums)):
                curr.append(nums[j])
                curr_sum += nums[j]
                backtrack(j, curr_sum)
                curr.pop()
                curr_sum -= nums[j]

        
        backtrack(0, 0)
        return res
