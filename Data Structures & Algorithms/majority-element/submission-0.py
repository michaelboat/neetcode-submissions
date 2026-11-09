class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        freqs = Counter(nums)

        for num in nums:
            if freqs[num] >= len(nums)//2:
                return num

        return -1
        