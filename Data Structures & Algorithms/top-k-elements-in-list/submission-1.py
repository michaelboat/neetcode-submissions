from collections import deque, Counter
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        
        #some_list = [(value, key) for key, value in frequency.items()]
        max_heap = []
        for num in count.keys():
            heapq.heappush(max_heap, (count[num], num)) 

            if len(max_heap) > k:
                heapq.heappop(max_heap)
                
        toReturn = []
        for i in range(k):
            toReturn.append(max_heap[i][-1])

        return toReturn


