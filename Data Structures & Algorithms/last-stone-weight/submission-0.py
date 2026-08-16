class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:


        minHeap = [-1*num for num in stones]
        heapq.heapify(minHeap)

        while len(minHeap) >= 2:

            x = heapq.heappop(minHeap)
            y = heapq.heappop(minHeap)
            diff = x - y
            
            if diff == 0:
                continue
            heapq.heappush(minHeap, diff)
        return -minHeap[0] if minHeap else 0
        