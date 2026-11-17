class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        i, j = 0, len(nums)-1

        while i <= j:
            if nums[i] == val:
                temp = nums[j]
                nums[j]=nums[i]
                nums[i]=temp
                j -= 1
            else:
                i += 1

        return i
        