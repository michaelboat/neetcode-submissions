class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        result = [0] * len(temperatures)
        stack = [] # contains a pair of values
        
        for i,temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                t, idx = stack.pop()
                result[idx] = (i - idx)
            stack.append((temp, i))

        return result