class Solution:
    def maxArea(self, heights: List[int]) -> int:

        max_water = 0
        j = len(heights) - 1
        i = 0
        while i < len(heights) - 1:
            h = heights[i]
            curr_height = heights[j]
            if h <= heights[j]:
                curr_height = h

            print(curr_height, h)
            curr_area = (j - i)*curr_height

            if curr_area >= max_water:
                max_water = curr_area

            if h <= heights[j]:
                i += 1
            else:
                j -= 1
        
        return max_water