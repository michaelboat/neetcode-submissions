class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:

        nums.sort()
        cand1, cand2 = None, None
        ct1, ct2 = 0, 0

        for num in nums:
            if cand1 == num:
                ct1 += 1
            elif cand2 == num:
                ct2 += 1
            elif ct1 == 0:
                cand1 = num
                ct1 += 1
            elif ct2 == 0:
                cand2 = num
                ct2 += 1
            else:
                ct1 -= 1
                ct2 -= 1


        res = []
        for candidate in [cand1, cand2]:
            if nums.count(candidate) > len(nums)//3:
                res.append(candidate)

        return res