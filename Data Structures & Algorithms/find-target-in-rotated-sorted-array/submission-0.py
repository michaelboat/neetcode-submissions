class Solution:
    def search(self, nums: List[int], target: int) -> int:

        # so since the array is sorted in ascending order, a
        # deflection point if there is one would be the point where 
        # a number is followed directly by a number less than in it
        # [a, b, c, d] [b, c] is a deflection point if b > c
        # [1, 2, 3, 4, 5] is rotated twice into -> [4, 5, 1, 2, 3]

        # find the deflection point and then perform binary 
        # search in the half that contains our target

        l, r = 0, len(nums)-1
        while l <= r:
            m = (l+r) // 2

            if nums[m] == target:
                return m
            
            if nums[l] <= nums[m]:
                if target < nums[l] or target > nums[m]:
                    l = m + 1
                else:
                    r = m - 1
            else:
                if target > nums[r] or target < nums[m]:
                    r = m -1
                else:
                    l = m + 1

        return -1
        