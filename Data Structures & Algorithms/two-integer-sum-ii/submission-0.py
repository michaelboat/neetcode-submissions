class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        #toReturn = []
        j = len(numbers) - 1
        i = 0
        while i < len(numbers):
            if numbers[i] + numbers[j] > target:
                j -= 1
                continue
            elif numbers[i] + numbers[j] < target:
                i += 1
                continue
            else:
                return [i+1, j+1]
            i += 1
        
        return []
        