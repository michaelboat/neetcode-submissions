class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        # maintain a min-heap with k largest integers
        # i.e or min in this min-heap becomes our k-th largest
        self.k = k
        self.minHeap = nums
        heapq.heapify(self.minHeap)
        # pop until you have k largest integers
        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)

    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val)
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        return self.minHeap[0]