class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        for i,num in enumerate(nums):
            map[num] = i
        
        for i,num in enumerate(nums):
            difference = target - num
            if difference in map and map[difference] != i:
                return [i, map[difference]]


        