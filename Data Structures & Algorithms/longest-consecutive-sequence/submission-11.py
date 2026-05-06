class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        my_set = set(nums)
        if len(nums) <= 0:
            return 0

        prev = True
        #passed_first = False
        longest = []
        curr = 0
        max_1 = max(nums)+1
        min_1 = min(nums)
        print(max_1, min_1)
        print(my_set)
        for i in range(min_1, max_1):
            if i in my_set and (prev or curr ==0):
                print(i, end=' ')
                curr += 1
                prev = True
                passed_first = True
            else:
                #if passed_first:
                longest.append(curr)
                curr = 0
                prev = False
            longest.append(curr)
        
        return max(longest)

