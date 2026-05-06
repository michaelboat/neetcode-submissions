import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
    
        # if you think about it really, the highest
        # rate at which koko can eat the bananas is at the 
        # rate of the max(piles) and the slowest(disregarding the h:int is 1)
        # then we binary search to the optimal rate
       
        low = 1              # minimum conceivable speed
        high = max(piles)    # maximum needed speed (eat largest pile in 1 hour)
        res = high           # worst-case valid answer — will narrow down

        while low <= high:
            mid = (low + high) // 2

            # calculate hours needed at speed mid
            hrs = 0
            for pile in piles:
                hrs += math.ceil(pile / mid)  # cleaner than a nested while loop

            if hrs <= h:
                # mid is valid — record it, then search LEFT for something slower
                res = mid
                high = mid - 1
            else:
                # mid is too slow — search RIGHT for something faster
                low = mid + 1

        return res

        

            


    