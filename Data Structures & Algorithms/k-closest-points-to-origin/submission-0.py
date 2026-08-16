class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        maxHeap = []
        for i in range(len(points)):
            dist = math.sqrt(points[i][0]**2 + points[i][1]**2)
            heapq.heappush(maxHeap, [-1*dist, points[i][0], points[i][1]])
            if len(maxHeap) > k:
                heapq.heappop(maxHeap)
        
        res = []
        while maxHeap:
            dist, p1, p2 = heapq.heappop(maxHeap)
            res.append([p1, p2])

        return res

        