class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        map = {}
        for num in nums:
            if num in map:
                map[num] += 1
                return True
            map[num] = 0
        return False
        