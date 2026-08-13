class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        def backtrack(i:int):
            
            nonlocal curr_sum
            if curr_sum == target:
                res.append(curr[:])
                return
            if curr_sum > target or i >= len(candidates):
                return

            for j in range(i, len(candidates)):
                if j > i and candidates[j] == candidates[j-1]:
                    continue
            
                curr.append(candidates[j])
                curr_sum += curr[-1]
                backtrack(j+1)
                curr_sum -= curr[-1]
                curr.pop()
                #backtrack(i+1)

        
        curr_sum = 0
        curr, res = [], []
        candidates.sort()
        backtrack(0)

        return res
        