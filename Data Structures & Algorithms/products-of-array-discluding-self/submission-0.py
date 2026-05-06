class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # keep track of negative and zero indices
        zeroes = []
        negatives = []
        toReturn = [0] * len(nums)
        
        prod = 1
        for i,num in enumerate(nums):
            if num < 0:
                negatives.append(i)
                prod = prod * abs(num)
                continue
            elif num == 0:
                zeroes.append(i)
                continue
            prod = prod * num
        
        # check for num of negative
        if len(negatives) % 2 != 0:
            prod = prod * -1

        if len(zeroes) > 1:
            return toReturn

        for i,num in enumerate(nums):
            if len(zeroes) >= 1:
                if i in zeroes:
                    toReturn[i] = prod
                continue
            
            else:
                num_to_add = int(prod/num)
                toReturn[i] = num_to_add

        # return 
        return toReturn



