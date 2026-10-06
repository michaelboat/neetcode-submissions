class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        
        xor_total = 0

        curr = []

        def backtrack(i:int):
            nonlocal xor_total
            xor = 0
            for num in curr[:]:
                xor ^= num

            xor_total += xor

            for j in range(i, len(nums)):
                curr.append(nums[j])
                backtrack(j+1)
                curr.pop()

        backtrack(0)

        return xor_total

