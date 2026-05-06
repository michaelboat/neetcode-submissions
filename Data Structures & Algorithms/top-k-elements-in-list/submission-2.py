from collections import deque, Counter
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # count = Counter(nums)
        
        # #some_list = [(value, key) for key, value in frequency.items()]
        # max_heap = []
        # for num in count.keys():
        #     heapq.heappush(max_heap, (count[num], num)) 

        #     if len(max_heap) > k:
        #         heapq.heappop(max_heap)
                
        # toReturn = []
        # for i in range(k):
        #     toReturn.append(max_heap[i][-1])

        # return toReturn

        count = Counter(nums)

        bucket = [[] for i in range(len(nums)+1)]
        for key, value in count.items():
            bucket[value].append(key)

        toReturn = []
        for i in range(len(bucket) - 1, 0, -1):
            if len(bucket[i]) > 0:
                for item in bucket[i]:
                    toReturn.append(item)
                    if len(toReturn) == k:
                        return toReturn  

        return toReturn 



